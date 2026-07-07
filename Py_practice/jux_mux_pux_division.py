def check_divisibility(n):
    labels = []
    
    if n % 3 == 0:
        labels.append("jux")
    if n % 6 == 0:
        labels.append("mux")
    if n % 9 == 0:
        labels.append("pux")
        
    return "-".join(labels) if labels else "None"

# Test the function
numbers = [3, 9, 12, 18, 859, 745, 669]
for num in numbers:
    result = check_divisibility(num)
    print(f"Number {num}: {result}")
