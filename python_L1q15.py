def main():
    x = int(input("Enter Number: "))
    
    # Extract the first two digits (e.g., 9561 -> 95)
    first_two = x // 100
    
    # Extract the last two digits (e.g., 9561 -> 61)
    last_two = x % 100
    
    # Reverse the last two digits mathematically
    reversed_last_two = (last_two % 10) * 10 + (last_two // 10)
    
    # Combine them back together
    y = (first_two * 100) + reversed_last_two
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
