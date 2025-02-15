from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES Encryption (Substitution)
def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# AES Decryption (Substitution)
def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_text, AES.block_size).decode()
    return plaintext

# Columnar Transposition Encryption
def transposition_encrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    padded_ciphertext = ciphertext.ljust(num_rows * num_columns, b'\0')
    matrix = [padded_ciphertext[i * num_columns:(i + 1) * num_columns] for i in range(num_rows)]
    transposed_ciphertext = b''.join([bytes([matrix[row][col] for row in range(num_rows)]) for col in key_order])
    return transposed_ciphertext

# Columnar Transposition Decryption
def transposition_decrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = (len(ciphertext) // num_columns)
    matrix = [[b'\0' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for col in key_order:
        for row in range(num_rows):
            matrix[row][col] = ciphertext[index:index + 1]  # Ensure we're working with bytes
            index += 1
    decrypted_ciphertext = b''.join([b''.join(row) for row in matrix])
    return decrypted_ciphertext.rstrip(b'\0')

# Hybrid Encryption
def hybrid_encrypt(plaintext, aes_key, transposition_key):
    aes_ciphertext = aes_encrypt(plaintext, aes_key)
    hybrid_ciphertext = transposition_encrypt(aes_ciphertext, transposition_key)
    return hybrid_ciphertext

# Hybrid Decryption
def hybrid_decrypt(ciphertext, aes_key, transposition_key):
    transposed_ciphertext = transposition_decrypt(ciphertext, transposition_key)
    plaintext = aes_decrypt(transposed_ciphertext, aes_key)
    return plaintext

# Main Function
if __name__ == "__main__":
    # Take user input for plaintext
    plaintext = input("Enter the plaintext to encrypt: ")

    # Take user input for AES key (must be 16, 24, or 32 bytes)
    aes_key = input("Enter the AES key (16, 24, or 32 characters): ").encode()
    if len(aes_key) not in [16, 24, 32]:
        print("Error: AES key must be 16, 24, or 32 bytes long.")
        exit()

    # Take user input for transposition key
    transposition_key = input("Enter the transposition key (e.g., 'SECRET'): ")

    # Encrypt the plaintext
    ciphertext = hybrid_encrypt(plaintext, aes_key, transposition_key)
    print("\nCiphertext (Hex):", ciphertext.hex())

    # Decrypt the ciphertext
    decrypted_text = hybrid_decrypt(ciphertext, aes_key, transposition_key)
    print("Decrypted Text:", decrypted_text)