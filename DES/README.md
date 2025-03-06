# Data Encryption Standard (DES) 

## 📌 Overview
This project implements the **Data Encryption Standard (DES)** in Python. DES is a symmetric-key block cipher that encrypts data using a 64-bit key and operates on 64-bit blocks.

## ✨ Features
- 🔒 Encrypts a given plaintext using a simple DES-like approach.
- 🔐 Generates keys for encryption using bit manipulation and shifting.
- ⚖️ Demonstrates basic block cipher concepts using binary transformations.
- 🔁 Provides a random key permutation for additional security.

## 🔍 How It Works
1. The user inputs a plaintext message.
2. The text is converted into an 8-bit binary representation.
3. The bits are split into two halves (left and right).
4. A series of bitwise transformations and shifts are applied.
5. Random key permutations are generated for added complexity.
6. The encrypted message is displayed.

---

## 📝 Code
```python
import random
s = input("Enter a string : ")
result = ''.join(format(ord(i),'08b') for i in s)
answer = ""

for i in range(len(result)):
    if(i%8!=0):
        answer+=result[i]

l = int(len(answer)/2)
left = answer[:l]
right = answer[l:]

lt = [2,3,6,7,1,6,5,9]
keys = []

for i in range(0,8):
    newKey = ""
    newAnswer = ""
    nl=int(left,2)
    nl=bin(nl <lt[i])
    num=2+lt[i]
    nr = int(right,2)
    nr = bin(nr <lt[i])
    num=2+lt[i]
    newKey = nr[num:]+nl[num:]
    rm =[]

while(len(rm)!=8):
    r = random.randint(0, len(newKey) -1)
    if(r not in rm):
        rm.append(r)

for i in range(len(newKey)):
    if(i not in rm):
        newAnswer+=newKey[i]

keys.append(newAnswer)

for i in range(0,len(keys)):
    print("Key ",i+1," = ",keys[i])
```

---

## 🚀 Usage
1. Run the script in a Python environment.
2. Enter a plaintext message when prompted.
3. The script will generate a key and encrypt the text.
4. The encrypted message is displayed as a binary output.

---

## 📈 Example
**Input:**
```
Message: HELLO
```
**Output:**
```
Key 1 = 1011010101...
```

---

## 🔎 Notes
- This is a simplified implementation of DES focusing on bitwise operations.
- The actual DES algorithm includes multiple permutations and XOR operations.
- Random key permutation adds a layer of complexity.

---

## 📚 License
This project is open-source and available for use and modification.

---

## 📩 Contact
For questions or feedback, please contact:

- **Author:** Samruddi N.G
- **Email:** [samruddi3504@gmail.com](mailto:samruddi3504@gmail.com)
- **GitHub:** [03NgSam](https://github.com/03NgSam)

