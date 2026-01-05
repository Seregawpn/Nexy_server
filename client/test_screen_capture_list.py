#!/usr/bin/env python3
"""
Тест получения списка приложений с разрешением Screen Capture.
Проверяем можно ли узнать есть ли наше приложение в списке.
"""

import subprocess
import os

def test_screen_capture_list():
    print("=" * 70)
    print("ПОИСК СПИСКА ПРИЛОЖЕНИЙ С РАЗРЕШЕНИЕМ SCREEN CAPTURE")
    print("=" * 70)
    
    # 1. ScreenCaptureKit - получить список разрешённых
    print("\n1. ScreenCaptureKit.SCShareableContent:")
    try:
        import objc
        from Foundation import NSRunLoop, NSDate
        
        SCShareableContent = objc.lookUpClass('SCShareableContent')
        
        # Этот API возвращает список доступного контента для захвата
        # Если приложение разрешено - вернёт список
        # Если нет - ошибка или пустой список
        
        result_holder = {'content': None, 'error': None}
        
        def completion_handler(content, error):
            result_holder['content'] = content
            result_holder['error'] = error
        
        # Вызываем async метод
        SCShareableContent.getShareableContentWithCompletionHandler_(completion_handler)
        
        # Ждём ответа (простой runloop)
        for _ in range(50):  # Макс 5 секунд
            NSRunLoop.currentRunLoop().runUntilDate_(
                NSDate.dateWithTimeIntervalSinceNow_(0.1)
            )
            if result_holder['content'] is not None or result_holder['error'] is not None:
                break
        
        if result_holder['error']:
            print(f"   ❌ Ошибка: {result_holder['error']}")
            print("   → Возможно Screen Capture НЕ разрешён")
        elif result_holder['content']:
            content = result_holder['content']
            windows = content.windows()
            displays = content.displays()
            applications = content.applications()
            
            print(f"   ✅ Получен контент!")
            print(f"   Дисплеев: {len(displays) if displays else 0}")
            print(f"   Окон: {len(windows) if windows else 0}")
            print(f"   Приложений: {len(applications) if applications else 0}")
            
            # Выводим несколько приложений
            if applications:
                print("\n   Приложения доступные для захвата:")
                for i, app in enumerate(applications[:5]):
                    bundle_id = app.bundleIdentifier()
                    name = app.applicationName()
                    print(f"     {i+1}. {name} ({bundle_id})")
                if len(applications) > 5:
                    print(f"     ... и ещё {len(applications) - 5}")
            
            print("\n   → ✅ Screen Capture GRANTED (мы видим контент)")
        else:
            print("   ⚠️ Нет ни контента, ни ошибки")
            
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    # 2. Проверка через CGWindowListCopyWindowInfo с deталями
    print("\n2. CGWindowListCopyWindowInfo с kCGWindowName:")
    try:
        from Quartz import (
            CGWindowListCopyWindowInfo,
            kCGWindowListOptionAll,
            kCGNullWindowID
        )
        
        windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
        
        # Проверяем можем ли мы видеть названия окон (требует Screen Capture)
        windows_with_names = 0
        for w in windows:
            name = w.get('kCGWindowName')
            if name:
                windows_with_names += 1
        
        print(f"   Всего окон: {len(windows)}")
        print(f"   Окон с названиями: {windows_with_names}")
        
        if windows_with_names > 0:
            print("   → ✅ Screen Capture вероятно GRANTED")
            # Показываем примеры
            print("\n   Примеры окон с названиями:")
            count = 0
            for w in windows:
                name = w.get('kCGWindowName')
                owner = w.get('kCGWindowOwnerName')
                if name and count < 3:
                    print(f"     - {owner}: '{name}'")
                    count += 1
        else:
            print("   → ⚠️ Нет окон с названиями - возможно нет разрешения")
            
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    # 3. TCC.db (информационно)
    print("\n3. TCC Database (~/Library/Application Support/com.apple.TCC/TCC.db):")
    tcc_path = os.path.expanduser("~/Library/Application Support/com.apple.TCC/TCC.db")
    print(f"   Путь: {tcc_path}")
    print(f"   Существует: {os.path.exists(tcc_path)}")
    
    # Попытка прочитать (обычно заблокировано SIP)
    try:
        import sqlite3
        conn = sqlite3.connect(tcc_path)
        cursor = conn.cursor()
        cursor.execute("SELECT client, service, auth_value FROM access WHERE service = 'kTCCServiceScreenCapture'")
        rows = cursor.fetchall()
        print(f"   ✅ Записи Screen Capture: {len(rows)}")
        for row in rows:
            print(f"     - {row[0]}: auth={row[2]}")
        conn.close()
    except Exception as e:
        print(f"   ❌ Не удалось прочитать: {e}")
        print("   (Это нормально - база защищена SIP)")
    
    print("\n" + "=" * 70)
    print("ВЫВОД")
    print("=" * 70)
    print("""
   Способы определить что Screen Capture GRANTED:
   
   1. ScreenCaptureKit.getShareableContent() успешно возвращает контент
      → Если ошибка - разрешения нет
      → Если есть контент - разрешение есть ✅
   
   2. CGWindowListCopyWindowInfo возвращает окна С ИМЕНАМИ
      → Без разрешения - окна без имён
      → С разрешением - видим имена окон ✅
   
   Эти способы позволяют ОПРЕДЕЛИТЬ что разрешение дано,
   даже если CGPreflightScreenCaptureAccess просто Bool!
    """)

if __name__ == "__main__":
    test_screen_capture_list()
