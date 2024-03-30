def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + 3)
        encrypted_text += encrypted_char
    return encrypted_text

text = input()

encrypted_text = encrypt_text(text)

print(encrypted_text)
