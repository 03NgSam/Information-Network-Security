# Key Management System (KMS)

## 📌 Overview
This Key Management System (KMS) provides secure key generation, storage, exchange, and revocation for symmetric and asymmetric encryption methods. It supports:

- **Symmetric Key Management (AES-256)**
- **Asymmetric Key Management (RSA/ECC)**
- **Diffie-Hellman Key Exchange**
- **Key Revocation System**
- **Secure API using Flask with TLS**

## 🚀 Features
- **Generate and store symmetric AES keys securely**
- **Generate and manage RSA key pairs**
- **Perform secure key exchange using Diffie-Hellman**
- **Revoke compromised keys**
- **Protect communications with TLS security**

## 📁 Project Structure
```
/Key-Management-System
│── app.py                 # Main Flask application
│── requirements.txt       # Dependencies
│── server.crt             # SSL certificate (provide your own)
│── server.key             # SSL private key (provide your own)
│── README.md              # Project documentation
```

## 🛠️ Installation & Setup
### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Generate SSL Certificates (Required for TLS Security)
```sh
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
```

### 3️⃣ Run the Application
```sh
python app.py
```

## 🔑 API Endpoints
### 📌 Generate a Symmetric Key (AES)
```http
POST /generate_symmetric_key
```
**Request Body:**
```json
{
    "client_id": "user1"
}
```
**Response:**
```json
{
    "client_id": "user1",
    "symmetric_key": "Jqk9K1JZ6E..."
}
```

### 📌 Generate RSA Key Pair
```http
POST /generate_rsa_key
```
**Request Body:**
```json
{
    "client_id": "user1"
}
```
**Response:**
```json
{
    "client_id": "user1",
    "public_key": "-----BEGIN PUBLIC KEY-----..."
}
```

### 📌 Generate Diffie-Hellman Key Pair
```http
POST /generate_dh_key
```

### 📌 Revoke a Key
```http
POST /revoke_key
```
**Request Body:**
```json
{
    "key_id": "user1_rsa"
}
```
**Response:**
```json
{
    "message": "Key user1_rsa revoked."
}
```

## 🔒 Security Measures
- **Prevention of MITM Attacks:** Uses PKI and TLS encryption.
- **Forward Secrecy:** Uses ephemeral Diffie-Hellman keys.
- **Access Control:** Key expiration, authentication, and revocation checks.

## 🛡️ Mitigation of Attacks
### 🔹 Man-in-the-Middle (MITM) Attack Prevention
- **TLS Encryption:** Ensures secure communication between clients and the server.
- **Public Key Infrastructure (PKI):** Ensures authenticity and integrity of public keys.
- **Certificate-Based Authentication:** Clients must verify server certificates to avoid MITM attacks.

### 🔹 Key Compromise Mitigation
- **Key Rotation:** Periodic regeneration and replacement of cryptographic keys.
- **Key Revocation System:** Maintains a revocation list to disable compromised keys.
- **Secure Key Storage:** Uses encrypted vaults for storing private keys.

### 🔹 Brute Force & Cryptanalysis Resistance
- **Strong Key Sizes:** Uses AES-256, RSA-2048, and DH-2048 for enhanced security.
- **Rate Limiting:** Prevents repeated key access attempts.
- **Multi-Factor Authentication (MFA):** Ensures authorized key access.

## 📜 License
This project is open-source and available under the **MIT License**.

---
Made with ❤️ for Secure Communication 🚀


