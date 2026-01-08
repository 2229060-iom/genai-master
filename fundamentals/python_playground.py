word = input("Enter a word: ")

letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter, count in letter_count.items():
    print(letter, ":", count)
