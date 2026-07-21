## python assessment july 8 Q2
#version 1
text = "Developer"
result = ""

for i, char in enumerate(text):
    if i % 2 != 0:
        result += "*"  # Replace alternate characters
    else:
        result += char  # Keep the original character

print(result)  # Output: D*v*l*p*r

#version 2
def replace_alternate_letters(text):
    result = []
    for index, char in enumerate(text):
        if index % 2 == 1:
            result.append("*")
        else:
            result.append(char)
    return "".join(result)
    
user_input = input("Enter a string: ")
modified_text = replace_alternate_letters(user_input)
print("Modified string:", modified_text)
