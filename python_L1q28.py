def main():
    x = int(input("Enter Number: "))
    
    # Extract the individual digits
    ones_digit = x % 10
    hundreds_digit = x // 100
    
    # Check the condition and assign the result to 'y'
    if (ones_digit + hundreds_digit) < 10:
        y = "Success"
    else:
        y = "Failure"
        
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
