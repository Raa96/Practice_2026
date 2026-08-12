def main():
    x = int(input("Enter Number: "))
    
    # 1. Extract the middle two digits (hundreds and tens digits)
    # Floor divide by 10 to remove the units digit, then modulo 100 to get the next two digits
    middle_two = (x // 10) % 100
    
    # 2. Check if the middle two digits form a prime number
    if middle_two < 2:
        y = "Not Prime"
    else:
        is_prime = True
        for i in range(2, int(middle_two**0.5) + 1):
            if middle_two % i == 0:
                is_prime = False
                break
        
        y = "Prime" if is_prime else "Not Prime"
        
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
