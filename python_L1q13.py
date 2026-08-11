def main():
    x = int(input("Enter Number: "))
    
    # Your Code Here
    ones = x % 10
    tens = x // 10
    y = (ones * 10) + tens
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
