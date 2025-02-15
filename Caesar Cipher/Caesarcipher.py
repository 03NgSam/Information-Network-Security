Plaintext = input("Enter text:\n")
k = 3

encoded_text = ""
for i in Plaintext:
    if i.islower():
        encoded_char = chr(((ord(i) + k - 97) % 26) + 97)
    elif i.isupper():
        encoded_char = chr(((ord(i) + k - 65) % 26) + 65)
    else:
        encoded_char = i
    encoded_text += encoded_char

decoded_text = ""
for i in encoded_text:
    if i.islower():
        decoded_char = chr(((ord(i) - k - 97) % 26) + 97)
    elif i.isupper():
        decoded_char = chr(((ord(i) - k - 65) % 26) + 65)
    else:
        decoded_char = i
    decoded_text += decoded_char

print("Encoded code:", encoded_text)
print("Decoded code:", decoded_text)
