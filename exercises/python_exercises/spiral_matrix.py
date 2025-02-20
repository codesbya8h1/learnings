def spiral_matrix(matrix):
    res = []

    while matrix:
        # add the first row of the matrix and delete it
        res+=matrix.pop(0)


        # add the last elements from all the remaninig lists and delete the added ones
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())


        # add the elements from last list in revers order and delete them
        if matrix:
            res+=(matrix.pop()[::-1])


        # add all the first element from  all the list and delete them from matrix
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))

    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_matrix(matrix))