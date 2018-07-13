#  Write a program that reads a string and returns a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each letter occurs. 


my_string = input("Write a sentence: ")

print("The sentence has:")

letter_counts = {}
for letter in my_string:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

for key, value in letter_counts.items():
    print(key, value)
