def main():
    x = int(input("Enter Number: "))
    
    # 1. Extract the last two digits (ten's and one's digit)
    num = x % 100
    
    # 2. Check if the two-digit number is prime
    is_prime = True
    
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
                
    # 3. Assign the string result to variable y
    y = "Prime" if is_prime else "Not Prime"
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
