# Function to compute GCD using Euclid's algorithm
def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to compute LCM
def compute_lcm(x, y):
    return abs(x * y) // compute_gcd(x, y)

if __name__ == "__main__":
    # Input two numbers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Compute GCD and LCM
    gcd = compute_gcd(num1, num2)
    lcm = compute_lcm(num1, num2)

    # Display the results
    print(f"GCD of {num1} and {num2} is: {gcd}")
    print(f"LCM of {num1} and {num2} is: {lcm}")
