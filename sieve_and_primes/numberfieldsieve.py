import math
import time

def sieve_of_eratosthenes(n):
    """Generate all primes less than or equal to n."""
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, int(math.sqrt(n)) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    for i in range(int(math.sqrt(n)) + 1, n + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def find_factor(n):
    """Find a non-trivial factor of n."""
    primes = sieve_of_eratosthenes(int(math.sqrt(n)) + 1)
    for p in primes:
        if n % p == 0:
            return p
    return None

def number_field_sieve(n):
    """Factorize n using the Number Field Sieve."""
    factors = []
    while True:
        factor = find_factor(n)
        if factor:
            factors.append(factor)
            n //= factor
        else:
            factors.append(n)
            break
    return factors

# Example usage:
number = 28068285780721
start_time = time.time()
factors = number_field_sieve(number)
end_time = time.time()
print("Factors of", number, "are:", factors)
print("Execution time:", end_time - start_time, "seconds")
