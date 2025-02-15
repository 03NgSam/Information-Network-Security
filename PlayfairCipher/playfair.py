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

    # Create a 5x5 matrix (list of lists)
    return [list(matrix[i:i + 5]) for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def preprocess_text(plaintext):
    # Replace 'J' with 'I' and convert to uppercase
    plaintext = plaintext.upper().replace('J', 'I')
    pairs = []

    i = 0
    while i < len(plaintext):
        # If there are two similar letters, insert 'X' in between
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

        if r1 == r2:  # Same row: shift columns
            c1 = (c1 + 1) % 5 if mode == 'encrypt' else (c1 - 1) % 5
            c2 = (c2 + 1) % 5 if mode == 'encrypt' else (c2 - 1) % 5
        elif c1 == c2:  # Same column: shift rows
            r1 = (r1 + 1) % 5 if mode == 'encrypt' else (r1 - 1) % 5
            r2 = (r2 + 1) % 5 if mode == 'encrypt' else (r2 - 1) % 5
        else:  # Rectangle: swap corners
            c1, c2 = c2, c1

        result.append(matrix[r1][c1] + matrix[r2][c2])

    return ''.join(result)


plaintext = input("Enter the message to encrypt: ")
keyword = input("Enter the keyword: ")

encrypted_message = playfair(plaintext, keyword, mode='encrypt')
print(f"Encrypted Message: {encrypted_message}")


decrypted_message = playfair(encrypted_message, keyword, mode='decrypt')
print(f"Decrypted Message: {decrypted_message}")
