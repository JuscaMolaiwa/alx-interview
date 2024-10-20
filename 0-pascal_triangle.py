#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of depth n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]  # Get the previous row
        new_row = [1]  # First element of the new row is always 1

        # Calculate the middle elements by summing adjacent elements in the previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element of the new row is always 1
        triangle.append(new_row)

    return triangle

