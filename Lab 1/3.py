text = input()
reversed_text = text[::-1]
rev_text = ""
print(reversed_text)

for i in range(len(text) - 1, -1, -1):
    rev_text += text[i]
print(rev_text)
