def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext
    
def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = []
    key_index = 0
    key_length = len(key)

    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            plaintext.append(chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A')))
            key_index = (key_index + 1) % key_length
        else:
            plaintext.append(char)  # Keep non-alphabet characters unchanged

    return ''.join(plaintext)
    
plaintext = "HELLO"
key = "KEY"
print("Plaintext", plaintext)
print("key", key)
print("Encrypted:", vigenere_encrypt(plaintext, key))
print("Decrypted:", vigenere_decrypt(vigenere_encrypt(plaintext, key), key))
