#!/usr/bin/python3

"""
A function that generates Pascal's Triangle.
"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows. And Returns list of lists of integers representing the Pascal's triangle of n.
    """
    pasc_triangle = []

    for i in range(n):
        if i <= 0:
            return pasc_triangle
        if i == 0:
            pasc_triangle.append([1])
        else:
            previous_row = pasc_triangle[-1]
            new_row = [1]

            for j in range(1, len(previous_row)):
                new_number = previous_row[j - 1] + previous_row[j]
                new_row.append(new_number)

            new_row.append(1)
            pasc_triangle.append(new_row)

    return pasc_triangle
