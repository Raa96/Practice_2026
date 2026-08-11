def main():
    x = int(input("Enter Number: "))
    # Your Code Here
    digit1 = x % 10  # Gets the last digit (e.g., 1 from 561)
    digit2 = (x // 10) % 10  # Gets the middle digit (e.g., 6 from 561)
    digit3 = x // 100  # Gets the first digit (e.g., 5 from 561)

    y = (digit1 * 100) + (digit2 * 10) + digit3
    print(f"Result = {y}")


if __name__ == "__main__":
    main()
