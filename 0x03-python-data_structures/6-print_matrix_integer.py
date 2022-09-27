#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    for x in range(len(matrix)):
        if len(matrix[x]) == 0:
            print("")
        for y in range(len(matrix[x])):
            if y != len(matrix[x]) - 1:
                print("{}".format(matrix[x][y]), end=" ")
            else:
                print("{}".format(matrix[x][y]))
        
