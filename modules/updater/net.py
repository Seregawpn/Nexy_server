"""
HTTP клиент для системы обновлений
Безопасные HTTPS запросы с проверкой сертификатов
"""

import urllib3
import os
import logging
from typing import Optional, Callable
import urllib3.exceptions

logger = logging.getLogger(__name__)

class UpdateHTTPClient:
    """HTTP клиент для обновлений с повышенной безопасностью"""

    def __init__(self, timeout: int = 30, retries: int = 3, ssl_verify: bool = True):
        """
        Инициализация HTTP клиента

        Args:
            timeout: Таймаут в секундах
            retries: Количество повторных попыток
            ssl_verify: Проверять SSL сертификат (False для self-signed)
        """
        # Отключаем предупреждения urllib3 для чистоты логов
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.ssl_verify = ssl_verify

        # Создаем отдельный HTTP клиент для обновлений с поддержкой редиректов
        pool_kwargs = {
            'retries': urllib3.Retry(
                total=retries,
                backoff_factor=0.5,
                status_forcelist=[500, 502, 503, 504],
                redirect=5  # Поддержка до 5 редиректов
            ),
            'timeout': urllib3.Timeout(total=timeout)
        }

        # Для self-signed сертификатов отключаем проверку
        if not ssl_verify:
            logger.warning("⚠️ SSL verification disabled - используется self-signed сертификат")
            pool_kwargs['cert_reqs'] = 'CERT_NONE'
            pool_kwargs['assert_hostname'] = False

        self.http = urllib3.PoolManager(**pool_kwargs)

        logger.info(f"HTTP клиент инициализирован: timeout={timeout}s, retries={retries}, ssl_verify={ssl_verify}")
    
    def get_manifest(self, url: str) -> dict:
        """
        Получение манифеста обновлений
        
        Args:
            url: URL манифеста (должен быть HTTPS)
            
        Returns:
            dict: Парсированный манифест (JSON или XML)
            
        Raises:
            ValueError: Если URL не HTTPS
            RuntimeError: Если HTTP статус не 200
        """
        # Проверяем HTTPS (исключения только для localhost в dev-режиме)
        if not url.startswith('https://') and not url.startswith('http://localhost') and not url.startswith('http://127.0.0.1'):
            raise ValueError("URL должен использовать HTTPS для безопасности (кроме localhost для тестирования)")
        
        logger.info(f"Запрос манифеста: {url}")
        
        try:
            response = self.http.request("GET", url)
            
            if response.status != 200:
                raise RuntimeError(f"HTTP {response.status}: {response.reason}")
            
            content = response.data.decode('utf-8')
            
            # Определяем формат по URL или содержимому
            if url.endswith('.xml') or content.strip().startswith('<?xml'):
                # Парсим XML (Sparkle appcast)
                manifest = self._parse_xml_manifest(content)
            else:
                # Парсим JSON
                import json
                manifest = json.loads(content)
            
            logger.info(f"Манифест получен: версия {manifest.get('version', 'неизвестная')}")
            return manifest
            
        except urllib3.exceptions.HTTPError as e:
            logger.error(f"Ошибка HTTP запроса: {e}")
            raise RuntimeError(f"Ошибка HTTP запроса: {e}")
        except Exception as e:
            # Проверяем, является ли это ошибкой парсинга
            if "json" in str(type(e)).lower() or "decode" in str(e).lower():
                logger.error(f"Ошибка парсинга JSON: {e}")
                raise RuntimeError(f"Неверный формат JSON: {e}")
            else:
                logger.error(f"Неожиданная ошибка: {e}")
                raise RuntimeError(f"Ошибка получения манифеста: {e}")
    
    def _parse_xml_manifest(self, xml_content: str) -> dict:
        """
        Парсинг XML манифеста (Sparkle appcast)
        
        Args:
            xml_content: XML содержимое
            
        Returns:
            dict: Нормализованный манифест
        """
        import xml.etree.ElementTree as ET
        
        try:
            root = ET.fromstring(xml_content)
            
            # Ищем первый item в channel
            item = root.find('.//item')
            if item is None:
                raise ValueError("Не найден item в XML манифесте")
            
            # Извлекаем данные
            title = item.find('title')
            description = item.find('description')
            pub_date = item.find('pubDate')
            enclosure = item.find('enclosure')
            
            # Получаем версию из sparkle:shortVersionString
            version = "1.0.0"  # По умолчанию
            if enclosure is not None:
                version_attr = enclosure.get('{http://www.andymatuschak.org/xml-namespaces/sparkle}shortVersionString')
                if version_attr:
                    version = version_attr
                
                # Получаем build номер (храним как строку, Sparkle допускает произвольные идентификаторы)
                build_attr = enclosure.get('{http://www.andymatuschak.org/xml-namespaces/sparkle}version')
                build = build_attr.strip() if build_attr else "0"
            else:
                build = "0"
            
            # Создаем нормализованный манифест
            download_url = enclosure.get('url') if enclosure is not None else None
            file_size = int(enclosure.get('length', 0)) if enclosure is not None else 0
            
            # Определяем тип файла по URL
            artifact_type = "pkg"  # По умолчанию для macOS
            if download_url:
                if download_url.endswith('.dmg'):
                    artifact_type = "dmg"
                elif download_url.endswith('.pkg'):
                    artifact_type = "pkg"
                elif download_url.endswith('.zip'):
                    artifact_type = "zip"
                # GitHub Releases часто используют прямые ссылки
                elif 'github.com' in download_url and 'releases/download' in download_url:
                    # Определяем тип по имени файла в URL
                    if '.dmg' in download_url:
                        artifact_type = "dmg"
                    elif '.pkg' in download_url:
                        artifact_type = "pkg"
                    elif '.zip' in download_url:
                        artifact_type = "zip"
            
            manifest = {
                'version': version,
                'build': build,
                'title': title.text if title is not None else f"Version {version}",
                'description': description.text if description is not None else f"Update to version {version}",
                'pubDate': pub_date.text if pub_date is not None else None,
                'download_url': download_url,
                'file_size': file_size,
                'minimum_system_version': enclosure.get('{http://www.andymatuschak.org/xml-namespaces/sparkle}minimumSystemVersion') if enclosure is not None else None,
                # Добавляем поле artifact для совместимости с существующим кодом
                'artifact': {
                    'type': artifact_type,
                    'url': download_url,
                    'size': file_size,
                    'sha256': None,  # В XML appcast обычно нет SHA256
                    'ed25519': None  # В XML appcast обычно нет Ed25519
                }
            }
            
            logger.info(f"XML манифест распарсен: версия {version}, build {build}")
            return manifest
            
        except ET.ParseError as e:
            logger.error(f"Ошибка парсинга XML: {e}")
            raise RuntimeError(f"Неверный формат XML: {e}")
        except Exception as e:
            logger.error(f"Ошибка обработки XML манифеста: {e}")
            raise RuntimeError(f"Ошибка обработки XML: {e}")
    
    def download_file(
        self,
        url: str,
        dest_path: str,
        expected_size: Optional[int] = None,
        on_progress: Optional[Callable[[int, Optional[int]], None]] = None,
    ):
        """
        Скачивание файла с проверкой размера
        
        Args:
            url: URL файла (должен быть HTTPS)
            dest_path: Путь для сохранения
            expected_size: Ожидаемый размер файла в байтах
            
        Raises:
            ValueError: Если URL не HTTPS
            RuntimeError: Если размер файла не совпадает
        """
        # Проверяем HTTPS (исключения только для localhost в dev-режиме)
        if not url.startswith('https://') and not url.startswith('http://localhost') and not url.startswith('http://127.0.0.1'):
            raise ValueError("URL должен использовать HTTPS для безопасности (кроме localhost для тестирования)")
        
        logger.info(f"Скачивание файла: {url} -> {dest_path}")
        
        try:
            with self.http.request("GET", url, preload_content=False) as response:
                if response.status != 200:
                    raise RuntimeError(f"HTTP {response.status}: {response.reason}")
                
                # Создаем директорию если нужно
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Скачиваем файл по частям
                with open(dest_path, "wb") as f:
                    downloaded = 0
                    for chunk in response.stream(1024 * 1024):  # 1MB chunks
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if on_progress:
                            try:
                                on_progress(downloaded, expected_size)
                            except Exception as callback_error:
                                logger.debug(f"download_file progress callback error: {callback_error}")

                        # Показываем прогресс каждые 10MB
                        if downloaded % (10 * 1024 * 1024) == 0:
                            mb_downloaded = downloaded / (1024 * 1024)
                            logger.info(f"Скачано: {mb_downloaded:.1f} MB")
            
            # Проверяем размер файла
            actual_size = os.path.getsize(dest_path)
            if expected_size and actual_size != expected_size:
                os.unlink(dest_path)  # Удаляем неполный файл
                raise RuntimeError(
                    f"Размер файла не совпадает: ожидалось {expected_size}, "
                    f"получено {actual_size} байт"
                )
            
            logger.info(f"Файл успешно скачан: {actual_size} байт")
            
        except urllib3.exceptions.HTTPError as e:
            logger.error(f"Ошибка HTTP запроса при скачивании: {e}")
            raise RuntimeError(f"Ошибка скачивания: {e}")
        except OSError as e:
            logger.error(f"Ошибка записи файла: {e}")
            raise RuntimeError(f"Ошибка записи файла: {e}")
    
    def test_connection(self, url: str) -> bool:
        """
        Тестирование соединения с сервером обновлений
        
        Args:
            url: URL для тестирования
            
        Returns:
            bool: True если соединение успешно
        """
        try:
            # Разрешаем https и http://localhost для локального тестового сервера,
            # чтобы поведение соответствовало get_manifest/download_file
            if not (url.startswith('https://') or url.startswith('http://localhost')):
                return False

            response = self.http.request("HEAD", url, timeout=10)
            return response.status == 200
            
        except Exception as e:
            logger.warning(f"Тест соединения неудачен: {e}")
            return False
