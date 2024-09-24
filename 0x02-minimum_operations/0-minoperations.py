#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n: int) -> int:
    """Method that calculates the fewest number of operations needed to
    resultin exactly n H characters in the file.
    """
    # If n is impossible to achieve, return 0. File already has 1 H
    if n <= 1:
        return 0

    # Find the smallest factor of n starting from 2
    for fact in range(2, n + 1):
        if n % fact == 0:
            # Return fact + the number of operations needed to get the
            # remaining  `n / fact`` Hs
            return fact + minOperations(int(n / fact))


# an alternate solution
"""
def minOperations(n: int) -> int:
    # This checks if n is less than or equal to 1. If so, it
    returns 0, because it's impossible to get n H characters with
    only one H

    if n <= 1:
        return 0

    # This initializes a variable i to 2 and a variable min_ops to0.
    i = 2
    min_ops = 0

    # This is a loop that will continue until i is greater than n.
    while i <= n:

    # This checks if n is divisible by i. . If so, it adds i to
    min_ops and updates n to be n/i. This is because if n is
    divisible by i, we can divide it by i to get closer to our goal
    of n H characters.
    if n % i == 0:
        min_ops += i
        n /= i

    # If n is not divisible by i, we increment i and try again.
    else:
         i += 1

    return min_ops
"""
