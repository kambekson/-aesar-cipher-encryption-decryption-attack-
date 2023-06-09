from datetime import datetime

# Функция для проверки ключа и срока действия лицензии
def check_license(key):
    valid_key = "crypt31"  # Замените на ваш действительный ключ лицензии
    valid_until = datetime(2023, 12, 31)  # Замените на действительную дату окончания лицензии

    if key != valid_key:
        print("[-] Ошибка: Недействительный ключ лицензии.")
        return False

    if datetime.now() > valid_until:
        print("[-] Ошибка: Истек срок действия лицензии.")
        return False

    return True



