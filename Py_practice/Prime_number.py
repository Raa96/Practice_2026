#!/usr/bin/env python3
"""Find prime numbers based on user input and print n primes after that.

Usage: run the script and follow prompts.
"""
import math


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    r = int(math.isqrt(num))
    for i in range(3, r + 1, 2):
        if num % i == 0:
            return False
    return True


def next_n_primes(start: int, count: int):
    found = 0
    candidate = start + 1
    while found < count:
        if is_prime(candidate):
            yield candidate
            found += 1
        candidate += 1


def main():
    try:
        start = int(input("Enter starting integer: ").strip())
        n = int(input("Enter how many primes to print after that: ").strip())
    except Exception:
        print("Invalid input")
        return
    if n <= 0:
        print("Nothing to print")
        return
    for p in next_n_primes(start, n):
        print(p)


if __name__ == "__main__":
    main()
