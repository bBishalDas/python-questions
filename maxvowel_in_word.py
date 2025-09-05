vowels = ["a","e","i","o","u","A","E","I","O","U"]

file = input("Enter file name: ")

with open(file) as f:
    text = f.read().strip()

words = text.split()

max_vowel_word = ""
max_vowel_count = 0

for word in words:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    # check if this word beats the current max
    if count > max_vowel_count:
        max_vowel_count = count
        max_vowel_word = word

print(f"The word with the most vowels is '{max_vowel_word}' with {max_vowel_count} vowels.")
