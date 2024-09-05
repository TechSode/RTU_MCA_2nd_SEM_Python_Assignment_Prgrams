def check_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

if __name__ == "__main__":
    # Input: List of numbers to check
    n = int(input("How many numbers do you want to check? "))
    numbers = []

    for i in range(n):
        number = int(input(f"Enter number {i+1}: "))
        numbers.append(number)
    
    # Check if each number is even or odd
    check_even(numbers)
