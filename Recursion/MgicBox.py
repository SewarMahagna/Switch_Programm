import numpy as np

def magic_box_3x3(matrix):
    rows, cols = matrix.shape
    if not (rows ==3 or cols ==3 ) : 
        TypeError("Matrix should be with size 3x3")

    flattened = [element for row in matrix for element in row]
    is_distinct = len(flattened) == len(set(flattened))
    return is_distinct 

def magic_box_nxn(matrix):
    rows, cols = matrix.shape
    row_start, row_end = 0, 3
    col_start, col_end = 0, 3
    sum_of_magic_boxes=0
    for row in rows:
        while col_end < cols : 
            submatrix = matrix[row_start:row_end, col_start:col_end]
            col_end+=1
            col_start+=1
            sum_of_magic_boxes += magic_box_3x3(submatrix)




            
    

