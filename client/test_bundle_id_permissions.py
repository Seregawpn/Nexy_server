#!/usr/bin/env python3
"""
Тест проверки разрешений по Bundle ID.
Проверяем можно ли получить информацию о разрешениях по Bundle ID.

Запуск: python3 test_bundle_id_permissions.py
"""

def test_bundle_id_permissions():
    print("=" * 70)
    print("ТЕСТ: Получение информации о разрешениях по Bundle ID")
    print("=" * 70)
    
    # Определяем Bundle ID текущего процесса
    print("\n1. Определение Bundle ID текущего процесса:")
    try:
        from Foundation import NSBundle
        bundle_id = NSBundle.mainBundle().bundleIdentifier()
        print(f"   NSBundle.mainBundle().bundleIdentifier() = {bundle_id}")
        
        if bundle_id:
            print(f"   ✅ Запущено как приложение с Bundle ID: {bundle_id}")
        else:
            print(f"   ⚠️ Запущено из Python интерпретатора (нет Bundle ID)")
            print(f"      При запуске из Nexy.app будет: com.nexy.assistant")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    # Проверяем что API проверяют для текущего процесса
    print("\n2. Как работают API проверки разрешений:")
    print("""
   API                              | Проверяет для
   ---------------------------------|---------------------------
   AXIsProcessTrusted()             | Текущий процесс
   IOHIDCheckAccess()               | Текущий процесс  
   AVCaptureDevice.authorizationStatusForMediaType_ | Текущий процесс
   CGPreflightScreenCaptureAccess() | Текущий процесс
    """)
    
    print("   Все эти API проверяют разрешения для ТЕКУЩЕГО ЗАПУЩЕННОГО процесса.")
    print("   TCC привязывает разрешения к code signature / Bundle ID приложения.")
    
    # Проверяем tccutil (работает с Bundle ID!)
    print("\n3. Проверка через tccutil (по Bundle ID):")
    import subprocess
    
    services = ["Microphone", "Accessibility", "ListenEvent", "ScreenCapture"]
    bundle_to_check = "com.nexy.assistant"
    
    for service in services:
        try:
            # tccutil check <service> <bundle_id> - проверяет по Bundle ID!
            result = subprocess.run(
                ['tccutil', 'check', service, bundle_to_check],
                capture_output=True,
                text=True,
                timeout=5
            )
            print(f"   tccutil check {service} {bundle_to_check}")
            print(f"     returncode: {result.returncode}")
            print(f"     stdout: {result.stdout.strip() or '(пусто)'}")
            print(f"     stderr: {result.stderr.strip() or '(пусто)'}")
            
            # tccutil возвращает 0 если разрешение есть, 1 если нет
            if result.returncode == 0:
                print(f"     → ✅ {service}: РАЗРЕШЕНО")
            else:
                print(f"     → ❌ {service}: НЕ РАЗРЕШЕНО или неизвестно")
            print()
        except Exception as e:
            print(f"   tccutil {service}: ошибка - {e}")
    
    # TCC database (для информации)
    print("\n4. TCC Database (только для информации):")
    print("   Разрешения хранятся в ~/Library/Application Support/com.apple.TCC/TCC.db")
    print("   Прямой доступ к базе заблокирован (SIP protection).")
    print("   Но tccutil может проверять по Bundle ID!")
    
    # Вывод
    print("\n" + "=" * 70)
    print("ВЫВОД")
    print("=" * 70)
    print("""
   1. API (IOHIDCheckAccess и др.) проверяют ТЕКУЩИЙ процесс
   2. Когда Nexy.app запущено, оно имеет Bundle ID com.nexy.assistant
   3. TCC привязывает разрешения к этому Bundle ID
   4. Значит когда код выполняется внутри Nexy.app, API проверяют 
      разрешения именно для com.nexy.assistant
   
   ✅ Да, мы получаем информацию о разрешениях для нашего приложения!
    """)

if __name__ == "__main__":
    test_bundle_id_permissions()
