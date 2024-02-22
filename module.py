def vigenere_cipher(text, key, encrypt=True):
    # Русский алфавит
    russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    # Английский алфавит
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Определяем алфавит на основе первого символа ключа
    if key[0].lower() in russian_alphabet:
        alphabet = russian_alphabet
    else:
        alphabet = english_alphabet

    key_length = len(key)
    key_as_int = [alphabet.index(i.lower()) for i in key]
    ciphertext = ''
    key_index = 0

    for char in text:
        if char.lower() in alphabet:
            offset = alphabet.index(alphabet[0])
            if encrypt:
                value = (alphabet.index(char.lower()) + key_as_int[key_index]) % len(alphabet)
            else:
                value = (alphabet.index(char.lower()) - key_as_int[key_index]) % len(alphabet)
            ciphertext += alphabet[value].upper() if char.isupper() else alphabet[value]
            key_index = (key_index + 1) % key_length
        else:
            ciphertext += char
    return ciphertext


def vigenere_decipher(ciphertext, key):
    return vigenere_cipher(ciphertext, key, encrypt=False)


# Пример использования
# key = 'ключ'  # Русский ключ
# plaintext = 'Пример текста для шифрования'
# ciphertext = vigenere_cipher(plaintext, key)
# print('Зашифрованный текст:', ciphertext)
# decrypted_text = vigenere_decipher(ciphertext, key)
# print('Расшифрованный текст:', decrypted_text)
#
# key = 'LEMON'
# plaintext = 'Attack at dawn!'
# ciphertext = vigenere_cipher(plaintext, key)
# print('Зашифрованный текст:', ciphertext)
# decrypted_text = vigenere_decipher(ciphertext, key)
# print('Расшифрованный текст:', decrypted_text)
