"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?


Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""
from math import sqrt

number = 600851475143

factors = []
prime_factors = []

# find all factors for our number. in range to sqr. all of them are appended to list
for i in range(1, round(sqrt(number))):
    if number % i == 0:
        factors.append(i)


def is_simple(num):
    """
    def checks if num is prime
    """
    for j in range(2, round(sqrt(num))):
        if num % j == 0:
            return False
    return True


# generate list of prime factors
for item in factors:
    if is_simple(item):
        prime_factors.append(item)

# Print max value of prime factors list
print(max(prime_factors))
