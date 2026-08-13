def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Euclidean algorithm via loop
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    
    print(f"The HCF of {num1} and {num2} is {a}")

if __name__ == "__main__":
    main()
