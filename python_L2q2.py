def main():
    x = int(input("Enter Number: "))
    
    # # Your Code Here
    while x >= 1:
        print(x)
        x -= 1
        
    # Setting y to an empty string to avoid syntax errors with the template's final print
    y = "Done!" 
    print(f"Result = {y}")

if __name__ == "__main__":
    main()
