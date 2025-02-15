# Vigenère Cipher Implementation

This project implements the **Vigenère Cipher**, a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. The Vigenère Cipher uses a keyword to shift letters in the plaintext, making it more secure than a simple Caesar Cipher.

## Features
- **Vigenère Cipher**: Encrypts plaintext using a keyword.
- **Case Insensitivity**: Converts all input to uppercase for consistency.
- **Alphabetic Only**: Ignores non-alphabetic characters (e.g., spaces, numbers, punctuation).

## Requirements
- Python 3.x

## Usage
1. Run the script:
   ```bash
   python vigenere_cipher.py

2. Provide input:

The script uses a predefined plaintext ```("HELLO")``` and key ```("KEY")```

3.View output:

The script will display the plaintext, key, and encrypted ciphertext.
## Example
## Input:
```bash
plaintext = "HELLO"
key = "KEY"
```
## Output:
```bash
Plaintext: HELLO
Key: KEY
Encrypted: RIJVS
```
## How It Works
1. ## Input Processing:

- The plaintext and key are converted to uppercase.

- Non-alphabetic characters (e.g., spaces, numbers, punctuation) are ignored.

2. ## Encryption:

- Each letter in the plaintext is shifted by a corresponding letter in the key.

- The shift value is determined by the position of the key letter in the alphabet (A=0, B=1, ..., Z=25).

- The formula for encryption is:
  ```bash
  ciphertext_char = (plaintext_char + key_char) % 26
  ```
  3. ## Output:
     - The encrypted ciphertext is displayed.

  ## Why Use the Vigenère Cipher?
  - **Polyalphabetic Substitution:**  The Vigenère Cipher uses multiple Caesar Ciphers based on the keyword, making it more secure than a simple substitution cipher.

- **Simplicity:** The algorithm is easy to understand and implement.

- **Historical Significance:** The Vigenère Cipher was considered unbreakable for centuries and is a classic example of early cryptography.

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

## Acknowledgments
- Inspired by classical cryptographic techniques and the Vigenère Cipher.

- Special thanks to the Python community for providing excellent resources.

   
