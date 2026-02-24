import requests
import json

# URL сервера (localhost, т.к. мы тестируем с локальной машины)
URL = "http://localhost:8080/api/subscription/checkout"
HARDWARE_ID = "test_hw_id_manual" # Ваш ID тестирования

print(f"🚀 Запрос ссылки на оплату для HWID: {HARDWARE_ID}...")

try:
    response = requests.post(URL, json={"hardware_id": HARDWARE_ID})
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Ссылка создана успешно!")
        print(f"🔗 URL: {data.get('url')}")
        print("\nПросто перейдите по этой ссылке, чтобы оплатить.")
    else:
        print(f"\n❌ Ошибка: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"\n❌ Ошибка соединения: {e}")
