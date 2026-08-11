def main():
    x = int(input("Enter Number: "))
    # Your Code Here
    y = x - (x % 2) * 5
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
