def main():
    x = int(input("Enter Number: "))
    
    # Convert number to string to easily swap digits
    num_str = str(x)
    
    # Handle single digit numbers or empty inputs
    if len(num_str) <= 1:
        y = int(num_str)
    else:
        # Swap the first and last characters and reconstruct the string
        swapped_str = num_str[-1] + num_str[1:-1] + num_str[0]
        y = int(swapped_str)
        
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
