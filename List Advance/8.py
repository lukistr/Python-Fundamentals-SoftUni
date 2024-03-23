def decipher_message(messages):
    words = messages.split()
    deciphered_words = []

    for word in words:
        last_char = ''
        first_chars = ''
        i = 0
        while word[i].isdigit():
            first_chars += word[i]
            i += 1

        first_char_code = int(first_chars)
        second_char = word[i]
        if i < len(word) - 1:
            last_char = word[-1]
        rest_chars = word[i + 1:-1]

        deciphered_word = chr(first_char_code) + last_char + rest_chars + second_char
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)

message = input()
print(decipher_message(message))
