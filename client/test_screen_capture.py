#!/usr/bin/env python3
"""
Тест альтернативных способов проверки Screen Capture permission.
Ищем способ различить DENIED от NOT_DETERMINED.
"""

def test_screen_capture_alternatives():
    print("=" * 70)
    print("ПОИСК АЛЬТЕРНАТИВ ДЛЯ SCREEN CAPTURE")
    print("=" * 70)
    
    # 1. CGPreflightScreenCaptureAccess (стандартный)
    print("\n1. CGPreflightScreenCaptureAccess:")
    try:
        from Quartz import CGPreflightScreenCaptureAccess
        result = CGPreflightScreenCaptureAccess()
        print(f"   Результат: {result} (только Bool)")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    # 2. Проверка через CGWindowListCopyWindowInfo
    print("\n2. CGWindowListCopyWindowInfo (косвенная проверка):")
    try:
        from Quartz import (
            CGWindowListCopyWindowInfo, 
            kCGWindowListOptionAll,
            kCGWindowListOptionOnScreenOnly,
            kCGNullWindowID
        )
        
        windows = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
        print(f"   Количество окон: {len(windows) if windows else 0}")
        
        # Проверяем можем ли мы видеть имена окон других приложений
        if windows:
            other_app_windows = 0
            for w in windows:
                owner = w.get('kCGWindowOwnerName', '')
                if owner and owner not in ['Python', 'python3', 'Terminal']:
                    other_app_windows += 1
            
            print(f"   Окна других приложений: {other_app_windows}")
            if other_app_windows > 10:
                print("   → ✅ Вероятно GRANTED (видим много окон)")
            else:
                print("   → ⚠️ Неоднозначно")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    # 3. Попытка захвата экрана
    print("\n3. CGDisplayCreateImage (попытка захвата):")
    try:
        from Quartz import CGDisplayCreateImage, CGMainDisplayID
        
        display_id = CGMainDisplayID()
        image = CGDisplayCreateImage(display_id)
        
        if image:
            print(f"   ✅ Захват успешен → GRANTED")
            # Получаем размер для уверенности
            from CoreGraphics import CGImageGetWidth, CGImageGetHeight
            w = CGImageGetWidth(image)
            h = CGImageGetHeight(image)
            print(f"   Размер: {w}x{h}")
        else:
            print(f"   ❌ Захват не удался → возможно DENIED или NOT_DETERMINED")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    # 4. SCC API (macOS 12.3+)
    print("\n4. ScreenCaptureKit (macOS 12.3+):")
    try:
        import objc
        ScreenCaptureKit = objc.lookUpClass('SCShareableContent')
        print("   ScreenCaptureKit доступен")
        print("   ⚠️ Требует async API для проверки")
    except Exception as e:
        print(f"   ❌ ScreenCaptureKit недоступен: {e}")
    
    # 5. Проверка через NSWorkspace running applications
    print("\n5. Анализ поведения:")
    print("""
   Возможные подходы для Screen Capture:
   
   a) CGPreflightScreenCaptureAccess() = False:
      - Вызываем CGRequestScreenCaptureAccess() чтобы показать диалог
      - Если после вызова CGPreflightScreenCaptureAccess() = True → GRANTED
      - Если False → возможно DENIED (пользователь отклонил)
   
   b) Отслеживание состояния:
      - Сохраняем факт что мы вызвали Request
      - Если после Request всё ещё False → считаем DENIED
   
   c) Практический подход:
      - Screen Capture обычно нужен только для конкретных функций
      - Можно проверять непосредственно перед использованием
      - И показывать инструкцию если не работает
    """)
    
    print("\n" + "=" * 70)
    print("ВЫВОД ДЛЯ SCREEN CAPTURE")
    print("=" * 70)
    print("""
   Нет 100% надёжного способа отличить DENIED от NOT_DETERMINED.
   
   Рекомендуемый подход:
   1. CGPreflightScreenCaptureAccess() = True → GRANTED
   2. CGPreflightScreenCaptureAccess() = False:
      - Вызываем CGRequestScreenCaptureAccess() 
      - Ждём короткое время
      - Проверяем снова
      - Если False после Request → assume DENIED или показываем инструкцию
    """)

if __name__ == "__main__":
    test_screen_capture_alternatives()
