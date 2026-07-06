def replace_numbers(n):
    replacements = {
        "3": "jux",
        "6": "mux",
        "9": "pux"
    }

    return "".join(replacements.get(ch, ch) for ch in str(n))

# Test the function
numbers = [876539216,963,369,693,]
for num in numbers:
    print(f"{num} -> {replace_numbers(num)}")