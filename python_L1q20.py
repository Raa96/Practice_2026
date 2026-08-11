def main():
    x = int(input("Enter Number: "))
    
    # Calculate the result by keeping the hundreds and ones digits, setting tens to 0
    y = (x // 100) * 100 + (x % 10)
    
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
