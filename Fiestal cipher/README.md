# Feistel Cipher Implementation

This project implements a **Feistel Cipher**, a symmetric encryption structure used in many block ciphers (e.g., DES). The Feistel Cipher divides the input data into two halves, processes them through multiple rounds of encryption, and combines them to produce the ciphertext. This implementation uses a simple key-based function for encryption and decryption.

## Features
- **Feistel Cipher Structure**: Implements the Feistel network for encryption and decryption.
- **Binary Operations**: Uses binary XOR and addition for the round function.
- **Custom Key**: Allows the user to input a custom key for encryption.
- **Text Encryption**: Encrypts and decrypts plaintext strings.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/03NgSam/Feistel-Cipher.git
   cd Feistel-Cipher

## Usage
1. Run the script:
   ```bash
   python feistel_cipher.py
2. Provide input:
   Enter the plaintext string to encrypt.
   Enter the key (a string used for encryption).
3. Output:
   The script will display the ciphertext (in binary format) and the decrypted plaintext.

## Example
## Input:
```bash
Enter a string: Hello
Enter a key: key
```
## Output:
```bash
Result: 0100100001100101011011000110110001101111
Ciphertext: 0100100001100101011011000110110001101111
Plaintext: Hello
```
## How It Works
## 1. Input Processing:

The plaintext is converted into a binary string.
The binary string is divided into two halves: left and right.

## 2. Feistel Rounds:

The right half is combined with the key using binary addition.
The result is XORed with the left half to produce the new right half.
The halves are swapped, and the process is repeated for the next round.

## 3. Ciphertext Generation:

After the rounds, the final halves are combined to produce the ciphertext.

## 4. Decryption:

The same process is repeated in reverse to decrypt the ciphertext.

## Why Use a Feistel Cipher?

- **Simplicity:** The Feistel structure is easy to implement and understand.

- **Reversibility:** The same algorithm can be used for both encryption and decryption.

- **Security:** By using multiple rounds, the Feistel Cipher can achieve strong encryption.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

## Contact
For questions or feedback, please contact:

- **Author:** Samruddi N.G
- **Email:** samruddi3504@gmail.com
- **GitHub:** [03NgSam](https://github.com/03NgSam)
