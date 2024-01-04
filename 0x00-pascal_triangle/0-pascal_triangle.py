def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - list: A list of lists representing Pascal's triangle.

    Note:
    Returns an empty list if n <= 0. Assumes n will always be an integer.
    """

    # Check if n is less than or equal to 
    # If true, return an empty list
    if n <= 0:
        return []

    # Initialize an empty list to store the rows of Pascal's triangle
    triangle = []

    # Iterate through each row from 0 to n-1
    for i in range(n):
        # Initialize a new row with all elements set to 1
        row = [1] * (i + 1)

        # Check if the row index is greater than 1 
        if i > 1:
            # Update elements in the row based on the values from the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the current row to the triangle list
        triangle.append(row)

    return triangle
