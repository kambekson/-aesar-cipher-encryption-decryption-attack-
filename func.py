import os

def encryption(Key, PlainText):
    CipherText = ''
    for p in PlainText:
        code = ord(p)+Key
        CipherText += chr(code)
    return CipherText

def decryption(Key, CipherText):
    PlainText = ''
    for c in CipherText:
        code = ord(c) - Key
        PlainText += chr(code)
    return PlainText

def reading():
    source = input("Источник данных: \n 'c' - консоль \t 'f' - файл \n")
    if source == 'c':
        data = input("Введите текст: ").strip()
        return data
    elif source == 'f':
        filename = input("Название файла с данными в формате '*.txt': \n")
        full_path = os.path.abspath(filename)
        print("Полный путь к файлу:", full_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data
    else:
        print("[-] Выбрана неверная операция")

def operationtype(operation):
    sh = "шифрования"
    rsh = "расшифрования"
    if operation == "ш":
        return sh
    elif operation == "р":
        return rsh

def writing(data, operation):
    op = operationtype(operation)
    exit = input("Вид вывода данных: \n 'c' - консоль \t 'f' - файл: \n")
    if exit == 'c':
        print("Результат: ", data)
    elif exit == 'f':
        filename = input(f"Файл для вывода результата {op} в формате 'имя.txt': \n")
        print(os.getcwd())
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print("\n[+] Результат %s записан в файл %s" % (operationtype(operation), filename))
    else:
        print("[-] Выбрана неверная операция")


def text_statistics(text):
    statistics = {}
    for char in text:
        if char in statistics:
            statistics[char] += 1
        else:
            statistics[char] = 1
    return statistics
