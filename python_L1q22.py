def main():
    x = int(input("Enter Number: "))
    
    # Isolate ten's digit, check if odd (1) or even (0), subtract accordingly
    tens_digit = (x // 10) % 10
    is_odd = tens_digit % 2
    y = x - (5 * is_odd)
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
