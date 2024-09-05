def countdown(n):
    while n >= 0:
        print(n)
        n -= 1

if __name__ == "__main__":
    # Take input from the user
    number = int(input("Enter a number to start the countdown: "))
    
    # Call the countdown function
    countdown(number)