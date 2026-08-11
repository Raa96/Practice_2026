def main():
    x = int(input("Enter Number: "))
    
    # Extract the two digits
    tens = x // 10
    ones = x % 10
    
    # Calculate the sum of the digits
    digit_sum = tens + ones
    
    # If odd, (digit_sum % 2) is 1 -> subtracts 5 * 1 = 5
    # If even, (digit_sum % 2) is 0 -> subtracts 5 * 0 = 0
    y = x - (5 * (digit_sum % 2))
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
