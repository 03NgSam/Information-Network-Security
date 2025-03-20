# 🔑 Diffie-Hellman Key Exchange Implementation

## 📌 Overview
This project implements the **Diffie-Hellman Key Exchange** algorithm in Python, allowing two parties to securely establish a shared secret key over an insecure communication channel.

---

## ⚙️ How It Works
Diffie-Hellman Key Exchange follows these steps:
1️⃣ **Select a Prime Number (`q`)** and a **Primitive Root (`a`)**.
2️⃣ **Each party selects a private key (`Xa` and `Xb`)**.
3️⃣ **Compute public keys:**
   - Party A computes: `Ya = (a^Xa) % q`
   - Party B computes: `Yb = (a^Xb) % q`
4️⃣ **Exchange public keys (`Ya` and `Yb`)** over the communication channel.
5️⃣ **Compute the shared secret key:**
   - Party A computes: `Ka = (Yb^Xa) % q`
   - Party B computes: `Kb = (Ya^Xb) % q`
6️⃣ Since `Ka` and `Kb` will be equal, both parties now have a **shared secret key**.

---

## 🚀 Installation & Requirements
✅ **Python 3** required. No additional libraries needed.

---

## ▶️ Usage
### 🏃 Running the script
```sh
python diffie_hellman.py
```

### ⌨️ Input Example
```
Enter a prime number: 23
Enter a primitive root: 5
Enter the private key of A: 6
Enter the private key of B: 15
```

### 📜 Output Example
```
Public key of A: 8
Public key of B: 19
Shared key for A: 2
Shared key for B: 2
```

---

## 🖥️ Code Implementation
```python
# 🔑 Diffie-Hellman Key Exchange in Python

def diffie_hellman():
    q = int(input("Enter a prime number: "))
    a = int(input("Enter a primitive root: "))
    Xa = int(input("Enter the private key of A: "))
    Xb = int(input("Enter the private key of B: "))
    
    # Compute public keys
    Ya = pow(a, Xa, q)  # (a^Xa) % q
    Yb = pow(a, Xb, q)  # (a^Xb) % q
    
    print("Public key of A:", Ya)
    print("Public key of B:", Yb)
    
    # Compute shared secret keys
    Ka = pow(Yb, Xa, q)  # (Yb^Xa) % q
    Kb = pow(Ya, Xb, q)  # (Ya^Xb) % q
    
    print("Shared key for A:", Ka)
    print("Shared key for B:", Kb)

if __name__ == "__main__":
    diffie_hellman()
```

---

## 🔐 Security Considerations
- 🔵 The prime number `q` should be **large** to prevent brute-force attacks.
- 🔵 The primitive root `a` should be carefully chosen for security.
- 🔵 Private keys (`Xa`, `Xb`) should be sufficiently large to prevent guessing.

---

## ⏳ Time Complexity
- ⏩ **Public Key Computation:** `O(log n)` (using modular exponentiation `pow()`)
- ⏩ **Shared Key Computation:** `O(log n)`
- ⏩ **Overall Complexity:** `O(log n)`

---



---

## 👤 Author
- Samruddi NG
---

## 🤝 Contributions
Feel free to contribute! Fork the repository and submit a pull request if you have improvements or optimizations. 🚀

