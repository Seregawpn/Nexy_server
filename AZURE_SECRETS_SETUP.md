# 🔐 Настройка Azure Secrets для GitHub Actions

## 🚨 **ПРОБЛЕМА: Отсутствуют Azure Secrets**

**Ошибка в workflow:**
```
❌ CRITICAL ERROR: GITHUB_SHA is empty!
❌ CRITICAL ERROR: GITHUB_SHA must be exactly 40 characters
```

**Причина:** Отсутствуют Azure credentials для аутентификации

## 📋 **Что нужно добавить в GitHub Secrets**

### **1. Перейдите в настройки репозитория:**
```
GitHub → Seregawpn/Nexy_server → Settings → Secrets and variables → Actions
```

### **2. Добавьте следующие secrets:**

| Secret Name | Описание | Где взять |
|-------------|----------|-----------|
| `NEXY_AZURE_CLIENT_ID` | Client ID из Azure App Registration | Azure Portal |
| `NEXY_AZURE_TENANT_ID` | Tenant ID из Azure App Registration | Azure Portal |
| `NEXY_AZURE_SUBSCRIPTION_ID` | Subscription ID из Azure | Azure Portal |

## 🔍 **Как получить Azure credentials**

### **Шаг 1: Azure Portal**
1. Откройте [Azure Portal](https://portal.azure.com)
2. Войдите в аккаунт, связанный с проектом Nexy

### **Шаг 2: App Registration**
1. Найдите **App registrations** в поиске
2. Найдите приложение для Nexy или создайте новое
3. Скопируйте **Application (client) ID** → это `NEXY_AZURE_CLIENT_ID`
4. Скопируйте **Directory (tenant) ID** → это `NEXY_AZURE_TENANT_ID`

### **Шаг 3: Subscription ID**
1. В поиске найдите **Subscriptions**
2. Выберите подписку, где развернут проект Nexy
3. Скопируйте **Subscription ID** → это `NEXY_AZURE_SUBSCRIPTION_ID`

## 🎯 **Пошаговая настройка GitHub Secrets**

### **1. Откройте репозиторий:**
```
https://github.com/Seregawpn/Nexy_server
```

### **2. Перейдите в Settings:**
```
Settings → Secrets and variables → Actions
```

### **3. Добавьте каждый secret:**
- Нажмите **New repository secret**
- Введите **Name** (например, `NEXY_AZURE_CLIENT_ID`)
- Введите **Value** (скопированное значение из Azure)
- Нажмите **Add secret**

### **4. Повторите для всех трех secrets:**
- ✅ `NEXY_AZURE_CLIENT_ID`
- ✅ `NEXY_AZURE_TENANT_ID`
- ✅ `NEXY_AZURE_SUBSCRIPTION_ID`

## 🔧 **Проверка настройки**

### **После добавления secrets:**
1. **Сделайте новый commit** в репозиторий
2. **GitHub Actions запустится автоматически**
3. **Проверьте логи** - должны исчезнуть ошибки с Azure credentials

### **Ожидаемый результат:**
```
✅ All Azure credentials are present
✅ Azure CLI working
✅ ACR nexy1 found
✅ Admin access enabled
✅ ACR credentials obtained
```

## 🚀 **Что произойдет после настройки**

### **1. Аутентификация в Azure:**
- ✅ GitHub Actions сможет войти в Azure
- ✅ Получит доступ к Container Registry
- ✅ Сможет деплоить Container Apps

### **2. Сборка и загрузка образа:**
- ✅ Docker образ соберется
- ✅ Загрузится в ACR nexy1
- ✅ Получит правильный тег

### **3. Деплой:**
- ✅ Container App обновится
- ✅ Использует новый образ
- ✅ Health check пройдет успешно

## 📚 **Полезные ссылки**

### **Azure документация:**
- [Create Azure AD app registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Find tenant ID](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant)
- [Find subscription ID](https://docs.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id)

### **GitHub Actions:**
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Azure login action](https://github.com/azure/login)

## ✅ **Результат**

После добавления Azure secrets:
1. **Workflow запустится без ошибок**
2. **Docker образ соберется и загрузится**
3. **Container App обновится успешно**
4. **Деплой завершится успешно**

**Добавьте Azure secrets и деплой заработает!** 🎉
