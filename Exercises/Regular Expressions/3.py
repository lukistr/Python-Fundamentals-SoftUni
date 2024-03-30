def count_word_occurrences(string, word):
    string_lower = string.lower()
    word_lower = word.lower()

    occurrences = string_lower.count(word_lower)
    return occurrences

string = input()
word = input()

occurrences = count_word_occurrences(string, word)

print(occurrences)
