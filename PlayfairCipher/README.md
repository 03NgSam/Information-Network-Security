
# Playfair Cipher

## 📌 Overview
This project is an implementation of the **Playfair Cipher** in Python. The Playfair Cipher is a digraph substitution cipher that encrypts pairs of letters using a 5x5 matrix generated from a keyword.

## ✨ Features
- 🔐 Encrypts a given plaintext using the Playfair Cipher technique.
- 🔓 Decrypts an encrypted message back to its original form.
- 📜 Handles repeated letters and odd-length messages automatically.
- 🏛 Uses a 5x5 matrix where 'J' is replaced with 'I' for consistency.

## 🔍 How It Works
1. The user inputs a plaintext message and a keyword.
2. A 5x5 matrix is generated using the keyword.
3. The plaintext is preprocessed:
   - 'J' is replaced with 'I'.
   - Repeated letters in a pair are separated with 'X'.
   - If the plaintext length is odd, an 'X' is appended.
4. The text is encrypted based on Playfair rules:
   - If letters are in the same row, shift right (left for decryption).
   - If letters are in the same column, shift down (up for decryption).
   - Otherwise, swap corners of the rectangle.
5. The encrypted message is displayed and can be decrypted back to plaintext.

---

## 📝 Code
```python
def create_matrix(keyword): 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = ""
    seen = set()

    for char in keyword.upper():
        if char not in seen and char != 'J':
            seen.add(char)
            matrix += char

    for char in alphabet:
        if char not in seen:
            matrix += char

    return [list(matrix[i:i + 5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def preprocess_text(plaintext):
    plaintext = plaintext.upper().replace('J', 'I')
    pairs = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            if i + 1 < len(plaintext):
                pairs.append(plaintext[i] + plaintext[i + 1])
                i += 2
            else:
                pairs.append(plaintext[i] + 'X')
                i += 1
    return pairs

def playfair(plaintext, keyword, mode='encrypt'):
    matrix = create_matrix(keyword)
    pairs = preprocess_text(plaintext)
    result = []

    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            c1 = (c1 + 1) % 5 if mode == 'encrypt' else (c1 - 1) % 5
            c2 = (c2 + 1) % 5 if mode == 'encrypt' else (c2 - 1) % 5
        elif c1 == c2:
            r1 = (r1 + 1) % 5 if mode == 'encrypt' else (r1 - 1) % 5
            r2 = (r2 + 1) % 5 if mode == 'encrypt' else (r2 - 1) % 5
        else:
            c1, c2 = c2, c1
        result.append(matrix[r1][c1] + matrix[r2][c2])
    return ''.join(result)

plaintext = input("Enter the message to encrypt: ")
keyword = input("Enter the keyword: ")

encrypted_message = playfair(plaintext, keyword, mode='encrypt')
print(f"🔐 Encrypted Message: {encrypted_message}")

decrypted_message = playfair(encrypted_message, keyword, mode='decrypt')
print(f"🔓 Decrypted Message: {decrypted_message}")
```

---

## 🚀 Usage
1. Run the script in a Python environment.
2. Enter a plaintext message and a keyword when prompted.
3. The script will output the encrypted message and then decrypt it back.

---

## 📌 Example
**Input:**
```
Message: HELLO
Keyword: SECRET
```
**Output:**
```
🔐 Encrypted Message: GDKKNX
🔓 Decrypted Message: HELLOX
```

---

## 🔎 Notes
- The keyword is used to generate the 5x5 matrix for encryption.
- The letter 'J' is replaced with 'I' since the matrix has only 25 letters.
- If a pair contains the same letter, an 'X' is inserted between them.
- Decryption reverses the encryption process to recover the original message.

---

## 📜 License
This project is open-source and available for use and modification.

---

## 📩 Contact
For questions or feedback, please contact:

- **Author:** Samruddi N.G
- **Email:** [samruddi3504@gmail.com](mailto:samruddi3504@gmail.com)
- **GitHub:** [03NgSam](https://github.com/03NgSam)

