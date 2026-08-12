def main():
    # Initialize a variable to store the running sum
    total_sum = 0
    
    # Loop from 6 down to 1 (inclusive)
    for i in range(6, 0, -1):
        total_sum += i
        
    # Print the final result
    print(total_sum)

if __name__ == "__main__":
    main()
