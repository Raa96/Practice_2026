# Program to Split Vowels and Consonants from a Paragraph

paragraph = input("Enter a paragraph: ")

vowels = ""
consonants = ""

for char in paragraph:
    if char.isalpha():  # Check if the character is an alphabet
        if char.lower() in "aeiou":
            vowels += char
        else:
            consonants += char

print("\nVowels:")
print(vowels)

print("\nConsonants:")
print(consonants)

print("\nTotal Vowels:", len(vowels))
print("Total Consonants:", len(consonants))