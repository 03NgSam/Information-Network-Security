# Caesar Cipher

## Overview
This project is a simple implementation of the **Caesar Cipher** in Python. The Caesar Cipher is a basic encryption technique that shifts each letter in the plaintext by a fixed number of positions in the alphabet.

## Features
- Encrypts a given text using a shift of `3`.
- Decrypts the encoded text back to its original form.
- Supports both uppercase and lowercase letters while keeping non-alphabetic characters unchanged.

## How It Works
1. The user inputs a plaintext message.
2. Each letter is shifted forward by `3` positions to create an encoded message.
3. The encoded message is then shifted back by `3` positions to retrieve the original plaintext.
4. The program prints both the encoded and decoded messages.

## Code
```python
Plaintext = input("Enter text:\n")
k = 3

encoded_text = ""
for i in Plaintext:
    if i.islower():
        encoded_char = chr(((ord(i) + k - 97) % 26) + 97)
    elif i.isupper():
        encoded_char = chr(((ord(i) + k - 65) % 26) + 65)
    else:
        encoded_char = i
    encoded_text += encoded_char

decoded_text = ""
for i in encoded_text:
    if i.islower():
        decoded_char = chr(((ord(i) - k - 97) % 26) + 97)
    elif i.isupper():
        decoded_char = chr(((ord(i) - k - 65) % 26) + 65)
    else:
        decoded_char = i
    decoded_text += decoded_char

print("Encoded code:", encoded_text)
print("Decoded code:", decoded_text)
```

## Usage
1. Run the script in a Python environment.
2. Enter a plaintext message when prompted.
3. View the encoded message and its decrypted version.

## Example
**Input:**
```
Hello, World!
```
**Output:**
```
Encoded code: Khoor, Zruog!
Decoded code: Hello, World!
```

## Notes
- The shift value (`k=3`) can be modified to use a different key.
- The program only shifts alphabetic characters, leaving spaces and symbols unchanged.

## License
This project is open-source and available for use and modification.


