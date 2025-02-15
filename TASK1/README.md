# Hybrid Cipher: Combining AES and Columnar Transposition
A secure encryption tool that combines AES and columnar transposition for enhanced data protection.

## Description
This project implements a **hybrid cipher** that combines **AES encryption** (substitution) and **columnar transposition** (transposition) to provide enhanced security for encrypting and decrypting messages. The hybrid approach ensures stronger protection against cryptanalysis and brute-force attacks.

## Features
- **AES Encryption**: Uses AES-128 for strong substitution-based encryption.
- **Columnar Transposition**: Adds an additional layer of security by rearranging the ciphertext.
- **User Input**: Takes plaintext, AES key, and transposition key as input.
- **Output**: Displays ciphertext (in hexadecimal format) and decrypted plaintext.

## Requirements
- Python 3.x
- `pycryptodome` library (for AES encryption)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/03NgSam/Information-Network-Security.git
   cd Information-Network-Security
   
2. Install dependencies:
   ```bash
   pip install pycryptodome
   
   
   
---

## Usage
1. Run the script:
   ```bash
   python hybrid_cipher.py

---

## How It Works
1. **AES Encryption**: The plaintext is encrypted using AES in ECB mode with a 128-bit key.
2. **Columnar Transposition**: The AES ciphertext is rearranged using a columnar transposition cipher.
3. **Hybrid Encryption**: The final ciphertext is the result of applying AES encryption followed by columnar transposition.
4. **Decryption**: The ciphertext is first reversed using the transposition key, then decrypted using the AES key.


## Why This Hybrid Cipher Is Secure
- **Defense in Depth**: Combines substitution (AES) and transposition (columnar transposition) for layered security.
- **Resistance to Cryptanalysis**: AES ensures strong encryption, while transposition disrupts patterns in the ciphertext.
- **Increased Key Space**: Uses both an AES key and a transposition key, making brute-force attacks harder.
- **Adaptability**: Can be extended to use stronger encryption algorithms or more complex transposition techniques.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

## Contact
For questions or feedback, please contact:
- **Author**: Samruddi N.G
- **Email**: samruddi3504@gmail.com
- **GitHub**: [03NgSam](https://github.com/03NgSam)

## Acknowledgments
- Inspired by cryptographic techniques and hybrid cipher designs.
- Uses the `pycryptodome` library for AES encryption.
