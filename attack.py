from func import encryption, decryption, writing, reading

def finding(word, ciphertext):
    for i in range(len(ciphertext)-len(word)):
        g = [ord(ciphertext[i+j])-ord(word[j]) for j in range(len(word))]
        s = 0
        for k in range(len(g)):
            if g[k] == g[0]:
                s +=1
        if s == len(g):
            return g[0]
    return None

ciphertext = reading()
voc = [' и ', ' в ', ' не ', ' на ', ' что ', ' по ', ' к ', ' но ', ' у ', ' как ']

for word in voc:
    key = finding(word, ciphertext)
    if key is not None:
        plaintext = decryption(key, ciphertext)
        print("Найден ключ:", key)
        print("Расшифрованный текст:", plaintext)
        writing(plaintext, 'р')
        break
else:
    print("Ключ не найден.")
