# 🔐 Настройка Federated Identity Credentials для GitHub Actions OIDC

## 🚨 **ПРОБЛЕМА: Отсутствуют Federated Identity Credentials**

**Ошибка в workflow:**
```
AADSTS70025: The client '***'(Nexy) has no configured federated identity credentials
```

**Причина:** Azure App Registration "Nexy" не настроен для OIDC аутентификации с GitHub Actions

## 📋 **Что нужно настроить в Azure**

### **1. Federated Identity Credentials**
- ✅ **Источник:** GitHub Actions
- ✅ **Репозиторий:** `Seregawpn/Nexy_server`
- ✅ **Ветка:** `main`
- ✅ **Тип аутентификации:** OIDC (OpenID Connect)

## 🔍 **Пошаговая настройка в Azure Portal**

### **Шаг 1: Откройте Azure Portal**
1. Перейдите в [Azure Portal](https://portal.azure.com)
2. Войдите в аккаунт с проектом Nexy

### **Шаг 2: Найдите App Registration "Nexy"**
1. В поиске найдите **"App registrations"**
2. Выберите приложение **"Nexy"**
3. Убедитесь, что это приложение с ID: `cc9cdd36-113c-441d-9413-f5ca224c3d0b`

### **Шаг 3: Перейдите в Federated Credentials**
1. В левом меню найдите **"Certificates & secrets"**
2. Нажмите на вкладку **"Federated credentials"**
3. Нажмите **"Add credential"**

### **Шаг 4: Настройте GitHub Actions Credential**
1. **Federated credential scenario:** Выберите **"GitHub Actions deploying Azure resources"**
2. **Organization:** Введите `Seregawpn`
3. **Repository:** Введите `Nexy_server`
4. **Entity type:** Выберите **"Branch"**
5. **GitHub reference name:** Введите `main`
6. **Name:** Введите `github-actions-nexy` (или любое понятное имя)
7. Нажмите **"Add"**

## 🎯 **Проверка настройки**

### **После добавления credential должно быть:**
```
Federated credentials:
✅ github-actions-nexy
   Source: GitHub Actions
   Repository: Seregawpn/Nexy_server
   Branch: main
   Added: [дата]
```

## 🔧 **Проверка workflow файла**

### **Убедитесь, что workflow использует правильные secrets:**
```yaml
- name: Azure Login with OIDC
  uses: azure/login@v2
  with:
    client-id: ${{ secrets.NEXY_AZURE_CLIENT_ID }}
    tenant-id: ${{ secrets.NEXY_AZURE_TENANT_ID }}
    subscription-id: ${{ secrets.NEXY_AZURE_SUBSCRIPTION_ID }}
```

### **Проверьте названия secrets в GitHub:**
- ✅ `NEXY_AZURE_CLIENT_ID` = `cc9cdd36-113c-441d-9413-f5ca224c3d0b`
- ✅ `NEXY_AZURE_TENANT_ID` = `eff9d76e-8a35-4d35-9db0-0ee271664040`
- ✅ `NEXY_AZURE_SUBSCRIPTION_ID` = `6d225f4c-756c-41ff-b361-62f248a60a2d`

## 🚀 **После настройки Federated Credentials**

### **1. Сделайте новый commit** в репозиторий
### **2. GitHub Actions запустится автоматически**
### **3. Azure Login пройдет успешно:**
```
✅ Azure Login with OIDC - пройдет
✅ Test Azure CLI - пройдет
✅ Check Container Registry nexy1 - пройдет
✅ Build and push to ACR - пройдет
✅ Deploy Container App - пройдет
```

## 📚 **Полезные ссылки**

### **Официальная документация:**
- [Configure federated credentials in Azure AD](https://github.com/Azure/login#configure-federated-credentials-in-azure-ad)
- [GitHub Actions OIDC with Azure](https://docs.microsoft.com/en-us/azure/developer/github/connect-from-azure)

### **GitHub Actions Azure Login:**
- [azure/login action](https://github.com/azure/login)

## ✅ **Результат**

После настройки Federated Identity Credentials:
1. **GitHub Actions сможет аутентифицироваться в Azure**
2. **Workflow пройдет все шаги успешно**
3. **Docker образ соберется и загрузится**
4. **Container App обновится на Azure**

**Настройте Federated Credentials и OIDC аутентификация заработает!** 🎉
