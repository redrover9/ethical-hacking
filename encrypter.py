def encrypt(plaintext):
    ciphertext = ""
    for i in plaintext:
        i = ord(i)
        i -= 96
        i = str(i)
        ciphertext += i
        ciphertext += " "
    return ciphertext
print(encrypt("grace"))