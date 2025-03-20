# RSA Encryption and Decryption in Python

## 📌 Overview
This project presents a simple yet effective implementation of the RSA encryption and decryption algorithm in Python. The script generates public and private keys, encrypts a message, and then decrypts it back to its original form.

## 🔍 How It Works
1. **User Input:** The user provides two prime numbers (`p` and `q`) and a message to encrypt.
2. **Key Generation:**
   - Compute `n = p * q` and Euler's totient function `phi = (p-1) * (q-1)`.
   - Select a small integer `e` such that it is coprime to `phi`.
   - Compute `d`, the modular multiplicative inverse of `e`.
3. **Encryption:** The message is encrypted using: 
   ```math
   c = (msg ^ e) % n
   ```
4. **Decryption:** The ciphertext is decrypted using: 
   ```math
   d = (c ^ d) % n
   ```

## ✅ Prerequisites
- Python 3.x installed on your system.

## 🚀 Running the Program
No additional dependencies are required. Simply execute the script in a Python environment.

### 📌 Steps to Run:
1. Open a terminal or command prompt.
2. Run the script using:
   ```sh
   python rsa.py
   ```
3. Enter the required values for `p`, `q`, and `msg` when prompted.

### 💡 Example Execution
#### 🔹 Input:
```
Enter the value of p: 61
Enter the value of q: 53
Enter the message: 42
```
#### 🔹 Output:
```
Encrypted message: 279
Decrypted message: 42
```

---

## 🖥️ Code Implementation
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def rsa(p, q, msg):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break
    
    j = 0
    while True:
        if (j * e % phi) == 1:
            d = j
            break
        j += 1
    
    c = (msg ** e) % n
    print("🔒 Encrypted message:", c)
    
    d = (c ** d) % n
    print("🔓 Decrypted message:", d)

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
msg = int(input("Enter the message: "))
rsa(p, q, msg)
```

---

## 📌 Important Notes
- Ensure that `p` and `q` are **prime numbers** for the correct execution of the RSA algorithm.
- This is a **basic RSA implementation** and is **not suitable for real-world cryptographic security**.



## ✨ Author
Samruddi NG

---




