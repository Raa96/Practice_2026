# python assessment july 8 Q1
# Take the sentence from the user as input and reverse each word in the sentence individually.
user_input = input("Enter a sentence: ")

# Split the sentence into a list of individual words
words = user_input.split()

# Reverse each word individually using slicing [::-1]
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a single sentence with spaces
output_sentence = " ".join(reversed_words)

# Print the final output
print(output_sentence)

