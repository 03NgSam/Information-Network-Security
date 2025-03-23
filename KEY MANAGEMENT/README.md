# Key Management System

## Objective
The purpose of this project is to design and implement a key management system that supports both symmetric and asymmetric encryption. The system will include centralized key distribution for symmetric encryption and a Public Key Infrastructure (PKI) for asymmetric encryption. Key generation, secure storage, and exchange mechanisms will be demonstrated, along with key revocation in case of compromise.

## System Architecture
The system is divided into the following main components:

1. **Centralized Key Distribution System**: Handles symmetric key distribution securely.
2. **Public Key Infrastructure (PKI)**: Manages asymmetric encryption keys, including issuance, verification, and revocation.
3. **Secure Key Exchange**: Implements Diffie-Hellman for exchanging symmetric keys securely.
4. **Key Revocation System**: Provides mechanisms to revoke compromised keys.

### Design Diagram
```
+--------------------------+
| Centralized Key Server   |
| - Key Generation        |
| - Secure Storage        |
| - Key Distribution      |
+--------------------------+
         |  (Symmetric Keys)
         v
+-------------------------+
| Client A               |
| - Requests Key         |
| - Encrypts Data        |
+-------------------------+

+--------------------------+
| Public Key Infrastructure |
| - Certificate Authority   |
| - Key Revocation List     |
+--------------------------+
         |  (Asymmetric Keys)
         v
+-------------------------+
| Client B               |
| - Requests Certificate |
| - Verifies Keys        |
+-------------------------+
```

## Implementation

### Secure Key Generation and Storage
#### Symmetric Key Generation
```python
from cryptography.fernet import Fernet

def generate_symmetric_key():
    key = Fernet.generate_key()
    with open("symmetric.key", "wb") as key_file:
        key_file.write(key)
    return key
```

#### Asymmetric Key Generation
```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_asymmetric_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
```

### Secure Key Exchange using Diffie-Hellman
```python
from cryptography.hazmat.primitives.asymmetric import dh

def diffie_hellman_key_exchange():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    private_key_A = parameters.generate_private_key()
    private_key_B = parameters.generate_private_key()

    public_key_A = private_key_A.public_key()
    public_key_B = private_key_B.public_key()

    shared_key_A = private_key_A.exchange(public_key_B)
    shared_key_B = private_key_B.exchange(public_key_A)

    assert shared_key_A == shared_key_B
    return shared_key_A
```

### Key Revocation
```python
import json

def revoke_key(key_id):
    with open("revoked_keys.json", "r+") as file:
        revoked_keys = json.load(file)
        revoked_keys.append(key_id)
        file.seek(0)
        json.dump(revoked_keys, file)
```

## Security Measures
### Mitigation of Attacks
1. **Man-in-the-Middle Attacks**:
   - Use certificates issued by a trusted Certificate Authority (CA) for key verification.
   - Implement mutual authentication to verify both parties.

2. **Key Compromise**:
   - Implement key revocation mechanisms with a revocation list.
   - Use forward secrecy to prevent past communications from being decrypted if a key is compromised.

3. **Replay Attacks**:
   - Implement nonce-based authentication to prevent reuse of exchanged keys.
   
## Conclusion
This key management system ensures secure generation, storage, exchange, and revocation of both symmetric and asymmetric keys. It mitigates security risks such as man-in-the-middle attacks and key compromise through a robust PKI and revocation mechanisms. The implemented solution is a foundational system for secure communications and encryption management.

