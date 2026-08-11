def main():
    x = int(input("Enter Number: "))
    
    # Extract the first two digits
    prefix = x // 100
    
    # Extract the last two digits
    last_two = x % 100
    
    # Reverse the last two digits
    reversed_last_two = (last_two % 10) * 10 + (last_two // 10)
    
    # Combine them back together
    y = (prefix * 100) + reversed_last_two
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
