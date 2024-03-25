def characters_in_between(char1, char2):
    ascii_char1 = ord(char1)
    ascii_char2 = ord(char2)

    if ascii_char1 > ascii_char2:
        ascii_char1, ascii_char2 = ascii_char2, ascii_char1

    characters_between = ' '.join(chr(char) for char in range(ascii_char1 + 1, ascii_char2))

    return characters_between

char1 = input()
char2 = input()

print(characters_in_between(char1, char2))
