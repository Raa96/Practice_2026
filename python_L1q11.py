def main():
    x = int(input("Enter Number: "))
    
    # Extract the tens digit using integer division
    tens = x // 10
    
    # Extract the ones digit using the modulo operator
    ones = x % 10
    
    # Sum the two digits
    y = tens + ones
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
