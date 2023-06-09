from func import encryption, decryption, writing, reading, text_statistics

encryption_method = "Метод шифрования: Шифр Цезаря"
author = "Автор: Камбар"
date = "Дата разработки: 08.06.2023"

print(encryption_method)
print(author)
print(date)
print()
plaintext = reading()

# Получение шифротекста
key = int(input("Введите ключ шифрования: "))
ciphertext = encryption(key, plaintext)

# Вывод статистики для исходного текста
print("Статистика для исходного текста:")
plaintext_statistics = text_statistics(plaintext)
for char, count in plaintext_statistics.items():
    print(f"Символ '{char}': {count} раз")

# Вывод статистики для зашифрованного текста
print("Статистика для зашифрованного текста:")
ciphertext_statistics = text_statistics(ciphertext)
for char, count in ciphertext_statistics.items():
    print(f"Символ '{char}': {count} раз")

# Расшифровка текста
decrypted_text = decryption(key, ciphertext)
print("Расшифрованный текст:", decrypted_text)

# Запись расшифрованного текста в файл
writing(decrypted_text, 'р')
