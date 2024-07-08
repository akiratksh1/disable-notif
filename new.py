import winreg

def disable_windows_notifications():
    try:
        # Abrir ou criar a chave de registro das configurações das notificações
        reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications'
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

        # Desativar as notificações
        winreg.SetValueEx(key, "ToastEnabled", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)

        # Configurações adicionais para desativar outras notificações (central de ações, etc.)
        reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings'
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

        apps = ["Windows.SystemToast", "Windows.Alarm", "Windows.Calendar"]

        for app in apps:
            app_key = winreg.CreateKey(key, app)
            winreg.SetValueEx(app_key, "Enabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(app_key)

        winreg.CloseKey(key)

        print("Notificações desativadas com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao desativar as notificações: {e}")

disable_windows_notifications()
