def pascal_triangle(n):
    if n <= 0:
        # If n  <= 0 return an empty list
        return []

    # Initialize an empty list to store the rows of Pascal's triangle
    triangle = []

    # Iterate through each row from 0 to n-1
    for i in range(n):
        # Initialize a new row with all elements set to 1
        row = [1] * (i + 1)

        # Check if the row index is greater than 1 (to avoid IndexError)
        if i > 1:
            # Update elements in the row based on the values from the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the current row to the triangle list
        triangle.append(row)

    # Return the resulting Pascal's triangle
    return triangle