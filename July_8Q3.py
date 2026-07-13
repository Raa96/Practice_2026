# Read the input sentence from the user
sentence = input()

# Replacement dictionary creation
replacements = {
    "cat": "dog",
    "apple": "orange",
    "red": "blue"
}

# Replace words in the sentence
words = sentence.split()
result = [replacements.get(word, word) for word in words]

# Print the modified sentence
print(" ".join(result))
