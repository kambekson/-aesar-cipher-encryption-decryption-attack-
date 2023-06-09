from func import encryption, decryption, writing, reading
from licence import check_license
# Запрос ключа лицензии
license_key = input("Введите ключ лицензии: ")

# Проверка ключа и срока действия лицензии
if not check_license(license_key):
    exit()

Key = int(input("Введите ключ шифрования: "))
operation = str(input("Введите 'e' для шифрования, 'd' для расшифрования: "))

if operation == 'e':
    PlainText = reading()
    CipherText = encryption(Key, PlainText)
    print("\n[+] Шифрование завершено\n")
    writing(CipherText, operation)
elif operation == 'd':  # если необходимо расшифровать текст
    CipherText = reading()
    PlainText = decryption(Key, CipherText)
    print("\n[+] Расшифрование завершено\n")
    writing(PlainText, operation)
else:
    print("[-] Выбрана неверная операция")  # если введена неверная операция
