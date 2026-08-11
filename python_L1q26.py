def main():
    x = int(input("Enter Number: "))
    
    # Extract the tens digit and units digit
    tens = x // 10
    units = x % 10
    
    # Calculate sum and determine success or failure
    if (tens + units) == 10:
        y = "Success"
    else:
        y = "Failure"
        
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
