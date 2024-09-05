def sum_even_fibonacci(limit):
    a, b = 1, 2  # Start with the first two Fibonacci numbers
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b  # Move to the next Fibonacci number
    return total

if __name__ == "__main__":
    limit = 4000000
    result = sum_even_fibonacci(limit)
    print(f"The sum of even Fibonacci numbers below {limit} is: {result}")
