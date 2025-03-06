# Monoalphabetic Cipher

## Overview
This project is an implementation of the **Monoalphabetic Cipher** in Python. A Monoalphabetic Cipher is a substitution cipher where each letter in the plaintext is replaced by a fixed different letter of the alphabet based on a shifting or mapping rule.

## Features
- Encrypts a given plaintext using a shift-based substitution method.
- Decrypts the encoded text back to its original form.
- Supports both uppercase and lowercase letters while preserving non-alphabetic characters.

## How It Works
1. The user inputs a plaintext message.
2. The program applies a shift to each letter to create an encrypted message.
3. The encrypted message can be decrypted by reversing the shift.
4. The program prints both the encrypted and decrypted messages.

## Code (Python Version)
```python
def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            encrypted_text += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            decrypted_text += chr((ord(char) - ord(base) - shift + 26) % 26 + ord(base))
        else:
            decrypted_text += char
    return decrypted_text

plaintext = input("Enter plaintext: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
```

## Usage
1. Run the script in a Python environment.
2. Enter a plaintext message and a shift value when prompted.
3. The script will output the encrypted and decrypted text.

## Example
**Input:**
```
Hello, World!
Shift: 3
```
**Output:**
```
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
```

## Notes
- The shift value determines how much each letter is displaced in the alphabet.
- Spaces and special characters remain unchanged.
- The decryption function reverses the shift to recover the original message.

## License
This project is open-source and available for use and modification.


