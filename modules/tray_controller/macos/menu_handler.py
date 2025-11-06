"""
macOS реализация меню трея
"""

import os
import rumps
import logging
from typing import List, Optional, Callable, Dict, Any
from ..core.tray_types import TrayMenuItem, TrayMenu, TrayStatus

logger = logging.getLogger(__name__)

class MacOSTrayMenu:
    """macOS реализация меню трея"""
    
    def __init__(self, app_name: str = "Nexy"):
        self.app_name = app_name
        self.app: Optional[rumps.App] = None
        self.menu_items: List[TrayMenuItem] = []
        self.status_callbacks: Dict[str, Callable] = {}
        # Ссылки на изменяемые пункты меню
        self._status_item: Optional[rumps.MenuItem] = None
        self._output_item: Optional[rumps.MenuItem] = None
        # UI таймер/очередь не используются на уровне модуля (обновления делает интеграция)
        # Callback для обработки завершения приложения
        self._quit_callback: Optional[Callable] = None
        # Путь к иконке для отложенной установки (после создания StatusItem)
        self._pending_icon_path: Optional[str] = None
        self._icon_timer: Optional[rumps.Timer] = None
    
    def create_app(self, icon_path: str) -> rumps.App:
        """Создать приложение с иконкой в трее"""
        try:
            logger.info(f"🔍 ДИАГНОСТИКА: create_app вызван с icon_path='{icon_path}'")
            logger.info(f"🔍 ДИАГНОСТИКА: os.path.exists(icon_path)={os.path.exists(icon_path) if icon_path else 'N/A'}")
            logger.info(f"🔍 ДИАГНОСТИКА: os.path.abspath(icon_path)='{os.path.abspath(icon_path) if icon_path else 'N/A'}'")
            logger.info(f"🔍 ДИАГНОСТИКА: Current working directory={os.getcwd()}")
            logger.info(f"🔍 ДИАГНОСТИКА: TMPDIR={os.environ.get('TMPDIR', 'NOT SET')}")

            # Проверяем статус NSApplication перед созданием rumps.App
            try:
                import AppKit
                nsapp = AppKit.NSApplication.sharedApplication()
                logger.info(f"🔍 ДИАГНОСТИКА: NSApplication instance exists: {nsapp is not None}")
                logger.info(f"🔍 ДИАГНОСТИКА: NSApplication activation policy: {nsapp.activationPolicy() if nsapp else 'N/A'}")
                logger.info(f"🔍 ДИАГНОСТИКА: NSApplication isActive: {nsapp.isActive() if nsapp else 'N/A'}")
            except Exception as e:
                logger.warning(f"⚠️ ДИАГНОСТИКА: Не удалось проверить NSApplication: {e}")

            # Создаем приложение
            # NOTE: StatusItem создаётся не здесь, а в app.run() -> initializeStatusBar()
            # поэтому retry здесь не нужен - он сделан на уровне coordinator перед app.run()
            self.app = rumps.App(
                name=self.app_name,
                quit_button=None  # Убираем стандартную кнопку выхода
            )
            logger.info(f"✅ ДИАГНОСТИКА: rumps.App создан успешно")

            # Включаем цветные иконки (отключаем шаблонный режим)
            try:
                self.app.template = False
                logger.info(f"✅ ДИАГНОСТИКА: template=False установлен")
            except Exception as e:
                logger.warning(f"⚠️ ДИАГНОСТИКА: Не удалось установить template=False: {e}")

            # Изначально меню заполняется интеграцией через TrayController._create_default_menu()
            # Здесь не создаём собственных пунктов меню, чтобы избежать дублирования и несинхронности.
            self.app.menu = []

            # ВАЖНО: НЕ устанавливаем иконку здесь!
            # StatusItem создаётся только внутри app.run() -> initializeStatusBar()
            # Сохраняем путь для отложенной установки через setup_delayed_icon_setting()
            if icon_path and os.path.exists(icon_path):
                logger.info(f"✅ ДИАГНОСТИКА: Иконка существует, сохраняем путь для отложенной установки")
                print("="*80)
                print(f"CRITICAL: Icon path saved for delayed setting: {icon_path}")
                print("="*80)
                self._pending_icon_path = icon_path
            else:
                logger.error(f"❌ ДИАГНОСТИКА: Иконка НЕ существует или путь пустой!")
                logger.error(f"❌ ДИАГНОСТИКА: icon_path='{icon_path}'")
                if icon_path:
                    # Проверяем содержимое директории
                    parent_dir = os.path.dirname(icon_path)
                    if os.path.exists(parent_dir):
                        logger.info(f"🔍 ДИАГНОСТИКА: Содержимое {parent_dir}:")
                        try:
                            files = os.listdir(parent_dir)
                            for f in files[:10]:  # Первые 10 файлов
                                logger.info(f"  - {f}")
                        except Exception as e:
                            logger.error(f"❌ ДИАГНОСТИКА: Ошибка чтения директории: {e}")
            
            # Добавляем метод applicationShouldTerminate если его нет
            if not hasattr(self.app, 'applicationShouldTerminate'):
                def applicationShouldTerminate(sender):
                    return True
                self.app.applicationShouldTerminate = applicationShouldTerminate
            
            # Настраиваем обработчик завершения приложения
            self._setup_quit_handler()
            
            return self.app
            
        except Exception as e:
            print(f"Ошибка создания приложения трея: {e}")
            return None
    
    def _setup_event_handlers(self):
        """Настроить обработчики событий"""
        if not self.app:
            return
        
        # Обработчики событий будут добавлены через rumps
    
    def add_menu_item(self, item: TrayMenuItem):
        """Добавить элемент меню"""
        if not self.app:
            return
        
        try:
            if item.separator:
                # Добавляем разделитель в меню приложения
                try:
                    self.app.menu.add(rumps.separator())
                except Exception:
                    pass
            else:
                # Создаем элемент меню
                menu_item = rumps.MenuItem(
                    title=item.title,
                    callback=item.action,
                    key=item.shortcut
                )
                
                if not item.enabled:
                    menu_item.state = 0  # Отключен
                
                # Добавляем в меню
                self.app.menu.add(menu_item)

                # Сохраняем ссылки на изменяемые элементы (по префиксу заголовка)
                try:
                    if isinstance(item.title, str):
                        if item.title.startswith("Status:"):
                            self._status_item = menu_item
                        elif item.title.startswith("Output:"):
                            self._output_item = menu_item
                except Exception:
                    pass
                
                # Если есть подменю
                if item.submenu:
                    self._add_submenu(menu_item, item.submenu)
            
            self.menu_items.append(item)
            
        except Exception as e:
            print(f"Ошибка добавления элемента меню: {e}")
    
    def _add_submenu(self, parent_item, submenu: TrayMenu):
        """Добавить подменю"""
        try:
            for sub_item in submenu.items:
                if sub_item.separator:
                    parent_item.add(rumps.separator())
                else:
                    sub_menu_item = rumps.MenuItem(
                        title=sub_item.title,
                        callback=sub_item.action,
                        key=sub_item.shortcut
                    )
                    
                    if not sub_item.enabled:
                        sub_menu_item.state = 0
                    
                    parent_item.add(sub_menu_item)
                    
                    # Рекурсивно добавляем подменю
                    if sub_item.submenu:
                        self._add_submenu(sub_menu_item, sub_item.submenu)
        
        except Exception as e:
            print(f"Ошибка добавления подменю: {e}")
    
    def update_menu(self, menu: TrayMenu):
        """Обновить меню"""
        if not self.app:
            return
        
        try:
            # Очищаем существующее меню
            self.app.menu.clear()
            self.menu_items.clear()
            
            # Добавляем новые элементы
            for item in menu.items:
                self.add_menu_item(item)
        
        except Exception as e:
            print(f"Ошибка обновления меню: {e}")
    
    def set_status_callback(self, event_type: str, callback: Callable):
        """Установить обработчик статуса"""
        self.status_callbacks[event_type] = callback
    
    def show_notification(self, title: str, message: str, subtitle: str = ""):
        """Показать уведомление"""
        if not self.app:
            return
        
        try:
            rumps.notification(
                title=title,
                subtitle=subtitle,
                message=message,
                sound=False
            )
        except Exception as e:
            print(f"Ошибка показа уведомления: {e}")

    def update_status_text(self, text: str):
        """Обновить текст статуса в меню."""
        if not self.app or not self._status_item:
            return
        try:
            self._status_item.title = f"Status: {text}"
        except Exception as e:
            print(f"Ошибка обновления статуса меню: {e}")
        
    def update_output_device(self, device_name: str):
        """Обновить название текущего устройства вывода в меню."""
        if not self.app or not self._output_item:
            return
        try:
            self._output_item.title = f"Output: {device_name}"
        except Exception as e:
            print(f"Ошибка обновления устройства в меню: {e}")
    
    def update_icon(self, icon_path: str):
        """Обновить иконку с retry механизмом"""
        if not self.app:
            logger.warning("⚠️ ДИАГНОСТИКА update_icon: self.app is None")
            return

        try:
            logger.info(f"🔍 ДИАГНОСТИКА update_icon: icon_path='{icon_path}'")
            logger.info(f"🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)={os.path.exists(icon_path)}")
            if os.path.exists(icon_path):
                logger.info(f"🔍 ДИАГНОСТИКА update_icon: размер файла={os.path.getsize(icon_path)} bytes")

            # Retry механизм для обновления иконки (на случай временных сбоев XPC)
            max_retries = 2
            retry_delay = 0.2
            import time

            for attempt in range(1, max_retries + 1):
                try:
                    self.app.icon = icon_path
                    logger.info(f"✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка {attempt})")
                    break
                except Exception as e:
                    logger.warning(f"⚠️ update_icon попытка {attempt} не удалась: {e}")
                    if attempt < max_retries:
                        time.sleep(retry_delay)
                    else:
                        raise  # Перебрасываем исключение после последней попытки

        except Exception as e:
            logger.error(f"❌ ДИАГНОСТИКА update_icon: Ошибка обновления иконки: {e}", exc_info=True)
    
    def setup_delayed_icon_setting(self):
        """Настроить отложенную установку иконки после создания StatusItem.

        ВАЖНО: Этот метод должен быть вызван ПЕРЕД app.run().
        StatusItem создаётся внутри app.run() -> initializeStatusBar(),
        поэтому мы используем Timer для установки иконки ПОСЛЕ его создания.
        """
        if not self.app or not self._pending_icon_path:
            logger.warning("⚠️ setup_delayed_icon_setting: app или pending_icon_path отсутствуют")
            return

        print("="*80)
        print("CRITICAL: Setting up delayed icon setting timer")
        print(f"CRITICAL: Icon path: {self._pending_icon_path}")
        print("="*80)

        attempt_count = [0]  # Используем список для изменяемой переменной в closure
        max_attempts = 5

        def try_set_icon(timer):
            """Попытка установить иконку с retry"""
            attempt_count[0] += 1
            try:
                print(f"🔄 CRITICAL: Delayed icon setting attempt {attempt_count[0]}/{max_attempts}")
                logger.info(f"🔄 Отложенная установка иконки, попытка {attempt_count[0]}/{max_attempts}")

                self.app.icon = self._pending_icon_path

                print(f"✅ CRITICAL: Icon set successfully on delayed attempt {attempt_count[0]}")
                logger.info(f"✅ Иконка установлена успешно на отложенной попытке {attempt_count[0]}")

                # Останавливаем таймер после успешной установки
                if self._icon_timer:
                    self._icon_timer.stop()
                    self._icon_timer = None

            except Exception as e:
                print(f"⚠️ CRITICAL: Delayed attempt {attempt_count[0]} failed: {e}")
                logger.warning(f"⚠️ Отложенная попытка {attempt_count[0]} не удалась: {e}")

                # Останавливаем таймер после максимального числа попыток
                if attempt_count[0] >= max_attempts:
                    print(f"❌ CRITICAL: All {max_attempts} delayed attempts failed!")
                    logger.error(f"❌ Все {max_attempts} отложенные попытки установки иконки не удались")
                    if self._icon_timer:
                        self._icon_timer.stop()
                        self._icon_timer = None

        # Создаём таймер с интервалом 0.2 секунды
        # Первая попытка будет через 0.2s после запуска app.run()
        self._icon_timer = rumps.Timer(try_set_icon, 0.2)
        self._icon_timer.start()
        logger.info("✅ Таймер отложенной установки иконки настроен")

    def run(self):
        """Запустить приложение"""
        if self.app:
            # Добавляем метод applicationShouldTerminate если его нет
            if not hasattr(self.app, 'applicationShouldTerminate'):
                def applicationShouldTerminate(sender):
                    return True
                self.app.applicationShouldTerminate = applicationShouldTerminate
            self.app.run()
    
    def set_quit_callback(self, callback: Callable):
        """Установить callback для обработки завершения приложения"""
        self._quit_callback = callback
    
    def _setup_quit_handler(self):
        """Настроить обработчик завершения приложения"""
        if not self.app:
            return
        
        # Переопределяем метод applicationShouldTerminate для предотвращения автоматического завершения
        original_should_terminate = self.app.applicationShouldTerminate
        
        def custom_should_terminate(sender):
            """Кастомный обработчик завершения приложения"""
            try:
                # Если есть callback, вызываем его
                if self._quit_callback:
                    self._quit_callback()
                # Возвращаем False чтобы предотвратить завершение
                return False
            except Exception as e:
                print(f"Ошибка в обработчике завершения: {e}")
                return True  # Разрешаем завершение в случае ошибки
        
        # Устанавливаем наш обработчик
        self.app.applicationShouldTerminate = custom_should_terminate
    
    def quit(self):
        """Завершить приложение"""
        if self.app:
            rumps.quit_application()

    
