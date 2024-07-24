#!/usr/bin/python3
"""
a function that returns a list of lists of integers
representing the Pascal’s triangle of n:

LOGIC:
For this particular question, The whole triangle
is a list of lists
    - if n <= 0, return []
an empty list is returned, since Pascal's triangle cannot
be generated for non-positive numbers

    - if n == 1, return [[1]]
a list containing a single list with a single element is
returned, since Pascal's triangle for 1 is constant

    - if n == 2, return [[1], [1, 1]]
a list containing two lists is returned, [1] and [1, 1], since
Pascal's triangle for n=2 is always [1], followed by [1, 1].

    - for idx in range(2, n):
begin a loop that iterates over the remaining rows of Pascal's
triangle, starting from the third row (i.e., index 2) up to the nth row.

    - row = [1]
initialize a variable row with a list containing a single
element, 1. This is the first element of every row in Pascal's triangle.

    - for j in range(1, idx):
begin a loop that iterates over the remaining elements of the
row, starting from the second element (i.e., index 1) up to the
last element (i.e., index idx - 1).

    - row.append(triangle[idx - 1][j - 1] + triangle[idx - 1][j])
append the sum of the two elements above the current element to
the row variable.

    - row.append(1)
append a 1 to the end of the row variable, since the last element
of every row in Pascal's triangle is always 1.

    - triangle.append(row)
append the row variable (new list) to the triangle list so that
it becomes the next row in the triangle.

    - return triangle
return the final triangle list, which contains all the rows(of
lists) of Pascal's triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    """This initializes the triangle variable with the first two
    rows of Pascal's triangle, which are [1] and [1, 1]."""
    triangle = [[1], [1, 1]]

    for idx in range(2, n):
        row = [1]
        for j in range(1, idx):
            row.append(triangle[idx - 1][j - 1] + triangle[idx - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
