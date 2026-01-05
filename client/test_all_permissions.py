#!/usr/bin/env python3
"""
Комплексный тест ВСЕХ разрешений macOS.
Проверяем какие API возвращают детерминированные значения.

Запуск: python3 test_all_permissions.py
"""

import ctypes
from ctypes import util

def test_all_permissions():
    print("=" * 70)
    print("КОМПЛЕКСНЫЙ ТЕСТ ВСЕХ РАЗРЕШЕНИЙ macOS TCC")
    print("=" * 70)
    
    # =========================================================================
    # 1. MICROPHONE (AVFoundation)
    # =========================================================================
    print("\n" + "=" * 70)
    print("1. MICROPHONE (AVFoundation.AVCaptureDevice)")
    print("=" * 70)
    
    try:
        import AVFoundation
        
        # AVAuthorizationStatus enum values:
        # 0 = AVAuthorizationStatusNotDetermined
        # 1 = AVAuthorizationStatusRestricted  
        # 2 = AVAuthorizationStatusDenied
        # 3 = AVAuthorizationStatusAuthorized
        
        auth_status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        )
        
        status_names = {
            0: "NOT_DETERMINED (пользователь ещё не видел диалог)",
            1: "RESTRICTED (ограничено политикой)",
            2: "DENIED (пользователь отклонил)",
            3: "AUTHORIZED (разрешено)",
        }
        
        print(f"Сырое значение: {auth_status}")
        print(f"Статус: {status_names.get(auth_status, 'Неизвестно')}")
        print(f"✅ ДЕТЕРМИНИРОВАННО: Можем различить все 4 состояния!")
        
    except ImportError as e:
        print(f"❌ AVFoundation недоступен: {e}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    # =========================================================================
    # 2. INPUT MONITORING (IOKit.IOHIDCheckAccess)
    # =========================================================================
    print("\n" + "=" * 70)
    print("2. INPUT MONITORING (IOKit.IOHIDCheckAccess)")
    print("=" * 70)
    
    try:
        iokit_path = util.find_library("IOKit")
        iokit = ctypes.CDLL(iokit_path)
        
        check_access = iokit.IOHIDCheckAccess
        check_access.argtypes = [ctypes.c_uint32]
        check_access.restype = ctypes.c_uint32  # ВАЖНО: uint32, не bool!
        
        # IOHIDRequestType
        kIOHIDRequestTypePostEvent = 0   # Для Accessibility
        kIOHIDRequestTypeListenEvent = 1  # Для Input Monitoring
        
        # IOHIDAccessType
        kIOHIDAccessTypeGranted = 0
        kIOHIDAccessTypeDenied = 1
        kIOHIDAccessTypeUnknown = 2
        
        result = check_access(kIOHIDRequestTypeListenEvent)
        
        status_names = {
            0: "GRANTED (разрешено)",
            1: "DENIED (отклонено)",
            2: "UNKNOWN (не определено)",
        }
        
        print(f"Сырое значение: {result}")
        print(f"Статус: {status_names.get(result, 'Неизвестно')}")
        print(f"✅ ДЕТЕРМИНИРОВАННО: Можем различить GRANTED/DENIED/UNKNOWN!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    # =========================================================================
    # 3. ACCESSIBILITY (ApplicationServices.AXIsProcessTrusted)
    # =========================================================================
    print("\n" + "=" * 70)
    print("3. ACCESSIBILITY (AXIsProcessTrusted / IOHIDCheckAccess PostEvent)")
    print("=" * 70)
    
    # Способ 1: AXIsProcessTrusted (только Bool)
    try:
        from ApplicationServices import AXIsProcessTrusted
        ax_result = AXIsProcessTrusted()
        print(f"AXIsProcessTrusted(): {ax_result}")
        print(f"  ⚠️ Возвращает только Bool - не различает DENIED от NOT_DETERMINED")
    except ImportError:
        print("AXIsProcessTrusted недоступен")
    
    # Способ 2: IOHIDCheckAccess с PostEvent (возвращает IOHIDAccessType!)
    try:
        result_post = check_access(kIOHIDRequestTypePostEvent)
        status_names = {
            0: "GRANTED (разрешено)",
            1: "DENIED (отклонено)",
            2: "UNKNOWN (не определено)",
        }
        print(f"\nIOHIDCheckAccess(PostEvent): {result_post}")
        print(f"  Статус: {status_names.get(result_post, 'Неизвестно')}")
        print(f"  ✅ МОЖЕМ использовать IOHIDCheckAccess(PostEvent) для Accessibility!")
        print(f"  Это даёт нам детерминированный статус!")
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
    
    # =========================================================================
    # 4. SCREEN CAPTURE (Quartz.CGPreflightScreenCaptureAccess)
    # =========================================================================
    print("\n" + "=" * 70)
    print("4. SCREEN CAPTURE (Quartz.CGPreflightScreenCaptureAccess)")
    print("=" * 70)
    
    try:
        from Quartz import CGPreflightScreenCaptureAccess
        result = CGPreflightScreenCaptureAccess()
        print(f"CGPreflightScreenCaptureAccess(): {result}")
        print(f"Тип: {type(result)}")
        print(f"⚠️ Возвращает только Bool - не различает DENIED от NOT_DETERMINED")
        
        # Проверим можно ли получить больше информации
        try:
            from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionAll, kCGNullWindowID
            # Попытка получить список окон - если не работает, возможно нет разрешения
            windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
            if windows:
                print(f"\nПроверка через CGWindowListCopyWindowInfo:")
                print(f"  Получено {len(windows)} окон")
                # Проверяем есть ли окна других приложений с деталями
                has_other_app_details = False
                for w in windows[:10]:  # Первые 10
                    owner = w.get('kCGWindowOwnerName', '')
                    if owner and owner != 'Python':
                        has_other_app_details = True
                        break
                if has_other_app_details:
                    print(f"  ✅ Screen Capture разрешён (видим окна других приложений)")
                else:
                    print(f"  ⚠️ Возможно нет доступа к деталям окон")
        except Exception as e:
            print(f"  CGWindowListCopyWindowInfo ошибка: {e}")
            
    except ImportError as e:
        print(f"❌ Quartz недоступен: {e}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    # =========================================================================
    # ИТОГОВАЯ ТАБЛИЦА
    # =========================================================================
    print("\n" + "=" * 70)
    print("ИТОГОВАЯ ТАБЛИЦА ДЕТЕРМИНИРОВАННОСТИ")
    print("=" * 70)
    print("""
| Разрешение       | API                           | Детерминированно? |
|------------------|-------------------------------|-------------------|
| Microphone       | AVAuthorizationStatus         | ✅ 4 состояния    |
| Input Monitoring | IOHIDCheckAccess(ListenEvent) | ✅ 3 состояния    |
| Accessibility    | IOHIDCheckAccess(PostEvent)   | ✅ 3 состояния    |
| Screen Capture   | CGPreflightScreenCaptureAccess| ❌ Только Bool    |
    """)
    
    print("ВЫВОД:")
    print("  - Microphone: ✅ УЖЕ работает правильно")
    print("  - Input Monitoring: 🐛 БАГИ в коде (c_bool вместо c_uint32)")
    print("  - Accessibility: 🔍 МОЖНО использовать IOHIDCheckAccess(PostEvent)!")
    print("  - Screen Capture: ❌ Действительно только Bool")

if __name__ == "__main__":
    test_all_permissions()
