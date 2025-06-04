# 1. Write a function that takes a list of numbers and returns the sum of only the prime numbers.
#    Input: [2, 4, 5, 6, 7]
#    Output: 14

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(numbers):
    return sum(n for n in numbers if is_prime(n))

print(sum_primes([2, 4, 5, 6, 7])) 


