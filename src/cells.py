# This file contains functions to work with cells in a matrix

#These are general functions to work with cells in a matrix.
def count(matrix, condition):
    "Purpose: counts the number of cells given in a matrix with a certain condition"
    "Parameters: matrix - a 2D list representing cells, condition - the value to count in the matrix"
    "Return: the number of cells in the matrix that match the condition"
    count_value = 0

    for cell in matrix:
        # Case 1: simple list of strings
        if isinstance(cell, str):
            if cell.lower() == condition.lower():
                count_value += 1

        # Case 2: dictionary row (real dataset)
        elif isinstance(cell, dict):
            if cell.get("state", "").lower() == condition.lower():
                count_value += 1

    return count_value

def disease_percentage(matrix):
    "Purpose: calculates the percentage of diseased cells in a matrix"
    "Parameters: matrix - a 2D list representing cells where each row is a cell."
    "Return: the percentage of diseased cells in the matrix"
    diseased = count(matrix, "diseased")
    healthy = count(matrix, "healthy")
    total = diseased + healthy
    if total == 0:
        return 0
    return (diseased / total) * 100

