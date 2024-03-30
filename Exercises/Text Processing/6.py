def replace_duplicate_letters(text):
    if not text:
        return ""

    result = text[0]
    for char in text[1:]:
        if char != result[-1]:
            result += char
    return result

text = input()

new_text = replace_duplicate_letters(text)

print(new_text)
