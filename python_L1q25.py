def main():
    x = int(input("Enter Number: "))
    
    # Extract the tens digit and hundreds digit
    tens = (x // 10) % 10
    hundreds = (x // 100) % 10
    
    # If same, (tens == hundreds) is True (1), so 1 * 5 = 5 is subtracted.
    # If different, (tens == hundreds) is False (0), so 0 * 5 = 0 is subtracted.
    y = x - (tens == hundreds) * 5
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
