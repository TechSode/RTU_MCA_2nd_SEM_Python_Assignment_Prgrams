def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total = 0
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total

if __name__ == "__main__":
    limit = 2000000
    result = sum_of_primes(limit)
    print(f"The sum of all primes below {limit} is: {result}")