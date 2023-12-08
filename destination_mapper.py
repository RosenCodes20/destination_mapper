import re

some_string = input()
found_words_regex = r"=[A-Z][A-za-z]{2,}=|/[A-Z][A-Za-z]{2,}/"

find_words = re.findall(found_words_regex, some_string)
leters = []
wordes = []
for word in find_words:
    found_word = r"\w+"
    find_word = re.findall(found_word, word)
    for words in find_word:
        wordes.append(words)
        for letter in words:
            leters.append(letter)
print(f"Destinations: {', '.join(wordes)}")
print(f"Travel Points: {len(leters)}")
