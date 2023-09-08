import sys

"""
Program: Project 1
Author: Braden Bell
Date Created: 08/30/23
Last Modified: 09/07/23
Description: 
    This program is a command-line utility for calculating the Greatest Common Divisor (GCD)
    of two integers. It provides three different algorithms for calculating the GCD:
    1. Extended Euclidean Algorithm
    2. Consecutive Integer Checking Algorithm
    3. Middle School Method (Bonus)
    
    The program takes two integers, m and n, as command-line arguments and outputs the GCD
    in the format: gcd(m, n) = v, where m and n are the input values, and v is the calculated GCD.
    
    The program is implemented in Python and adheres to the requirements specified in the Project1
    assignment.

Usage:
    python3 babell45_project1.py <number_1> <number_2>
"""

# Check for correct number of command line arguments
if len(sys.argv) != 3:
    print("Usage: python3 babell45_project1.py <number 1> <number 2>")
    sys.exit(1)

try:
    A = int(sys.argv[1])
    B = int(sys.argv[2])
except ValueError:
    print("Input Error: Please provide integers greater than 0 as input.")
    sys.exit(1)


def extended_euclid(a, b):
    """
    Extended Euclidean Algorithm to find gcd(a, b) and coefficients x, y such that gcd(a, b) = ax + by.

    Args:
    a, b: Integers for which gcd is to be computed.

    Returns:
    Tuple containing gcd, x, and y.
    """
    if a <= 0 or b <= 0:
        return "undefined", 0, 0

    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0


def consecutive_integer(a, b):
    """
    Find gcd of a and b using consecutive integer checking.

    Args:
    a, b: Integers for which gcd is to be computed.

    Returns:
    gcd of a and b.
    """
    if a <= 0 or b <= 0:
        return "undefined"

    min_value = min(a, b)

    for i in range(min_value, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def prime_factors(a):
    """
    Factorizes integer a into its prime factors.
    Helper function for middle_school() function.

    Args:
    a: Integer to be factorized.

    Returns:
    List of prime factors.
    """
    i = 2
    factors = []
    while i * i <= a:
        if a % i:
            i += 1
        else:
            a //= i
            factors.append(i)
    if a > 1:
        factors.append(a)
    return factors


def count_factors(factors):
    """
    Counts the occurrences of each prime factor.
    Helper function for middle_school() function.

    Args:
    factors: List of prime factors.

    Returns:
    Dictionary with prime factors as keys and their counts as values.
    """
    factor_count = {}
    for factor in factors:
        if factor in factor_count:
            factor_count[factor] += 1
        else:
            factor_count[factor] = 1
    return factor_count


def middle_school(a, b):
    """
    Find gcd of a and b using the middle-school method.

    Args:
    a, b: Integers for which gcd is to be computed.

    Requires:
    count_factors()
    prime_factors()

    Returns:
    gcd of a and b.
    """
    if a == 0 or b == 0:
        return "undefined"

    factors_a = count_factors(prime_factors(a))
    factors_b = count_factors(prime_factors(b))

    gcd = 1
    for factor, count_a in factors_a.items():
        if factor in factors_b:
            count_b = factors_b[factor]
            min_count = min(count_a, count_b)
            gcd *= factor**min_count

    return gcd


# Display results
print("\nExtended Euclid's Algorithm:")
gcd, x, y = extended_euclid(A, B)
print(f"gcd({A}, {B}) = {gcd}")
print(f"x, y: {x}, {y}")

print("\nConsecutive Integer Checking Algorithm:")
gcd = consecutive_integer(A, B)
print(f"gcd({A}, {B}) = {gcd}")

print("\nMiddle School Method:")
gcd = middle_school(A, B)
print(f"gcd({A}, {B}) = {gcd}\n")
