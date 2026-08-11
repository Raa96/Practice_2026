def main():
    x = int(input("Enter Number: "))
    
    # Extract digits using integer division and modulo
    hundreds = x // 100
    ones = x % 10
    
    # Check equality: True (1) if same, False (0) if different
    is_same = (ones == hundreds)
    
    # Subtract 5 * 1 or 5 * 0
    y = x - (5 * int(is_same))
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
