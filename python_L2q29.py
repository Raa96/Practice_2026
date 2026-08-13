import math

def main():
    # Get three numbers from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    
    # Calculate the LCM of the three numbers
    result = math.lcm(num1, num2, num3)
    
    # Print the result
    print("The LCM of the three numbers is:", result)

if __name__ == "__main__":
    main()
