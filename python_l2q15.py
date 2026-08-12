def main():
    x = int(input("Enter Number: "))
    
    # Convert to string to easily access and manipulate the first digit (MSB)
    s = str(x)
    msb = int(s[0])
    
    if msb % 2 == 0:
        # If even, the number remains unchanged
        y = s
    else:
        # If odd, subtract 1 from the MSB and reconstruct the string
        new_msb = str(msb - 1)
        y = new_msb + s[1:]
        
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
