def main():
    x = int(input("Enter Number: "))
    
    # Extract each digit using floor division (//) and modulo (%) operators
    hundreds = x // 100
    tens = (x // 10) % 10
    ones = x % 10
    
    # Calculate the sum
    y = hundreds + tens + ones
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
