def main():
    x = int(input("Enter Number: "))
    
    # 1. Check if the number is prime
    is_prime = True
    if x < 2:
        is_prime = False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break
                
    # 2. Calculate the sum of digits
    # Using generator expression for efficient digit summation
    digit_sum = sum(int(digit) for digit in str(abs(x)))
    
    # 3. Format the final output string dynamically
    if is_prime and digit_sum == 14:
        y = "Prime & Sum of Digits is 14"
    elif not is_prime and digit_sum == 14:
        y = "Not Prime but sum of digits is 14"
    elif is_prime and digit_sum != 14:
        y = "Prime, but sum of Digits is not 14"
    else:
        y = "Not Prime and sum of digits is not 14"

    print(f"Result = {y}")

if __name__ == "__main__":
    main()
