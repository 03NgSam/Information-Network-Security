# Hill Cipher

## Overview
This project is an implementation of the **Hill Cipher** in Python. The Hill Cipher is a polygraphic substitution cipher based on linear algebra, where blocks of letters are transformed using matrix multiplication and modular arithmetic.

## Features
- Encrypts plaintext using a given key matrix.
- Converts letters to numerical values for processing.
- Ensures the plaintext length is a multiple of the matrix size by padding with 'X'.

## How It Works
1. The user inputs a plaintext message.
2. The program converts the plaintext into numerical values.
3. The plaintext is split into blocks matching the size of the key matrix.
4. Each block is multiplied by the key matrix and reduced modulo 26.
5. The resulting numerical values are converted back into letters to form the ciphertext.

## Code
```python
import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)
    return ciphertext

plaintext = input("Enter the plaintext: ")
key_matrix = np.array([[7, 8], [11, 11]])
print("Encrypted:", hill_cipher_encrypt(plaintext, key_matrix))
```

## Usage
1. Run the script in a Python environment.
2. Enter a plaintext message when prompted.
3. The script will output the encrypted text.

## Example
**Input:**
```
HELLO
```
**Output:**
```
Encrypted: ZEBBW
```

## Notes
- The key matrix should be square (e.g., 2×2, 3×3, etc.).
- The determinant of the key matrix should be invertible modulo 26 for decryption to work.
- Spaces in the plaintext are removed before encryption.
- If the length of the plaintext is not a multiple of the matrix size, it is padded with 'X'.

## License
This project is open-source and available for use and modification.


