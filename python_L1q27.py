def main():
    x = int(input("Enter Number: "))
    
    # Extract digits and calculate their sum
    digit_sum = sum(int(digit) for digit in str(x))
    
    # Determine the result based on the sum
    if digit_sum == 10:
        y = "Success"
    else:
        y = "Failure"
        
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
