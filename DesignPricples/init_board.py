import random

def initialize_board(size, elements): 
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    if len(elements) < size * size:
        raise ValueError("Not enough elements to fill the board.")
    random.shuffle(elements)
    board = [elements[i * size:(i + 1) * size] for i in range(size)]
    return board


size = 4  
elements = list(range(1, (size * size) + 1))
board = initialize_board(size, elements)

for row in board:
    print(row)
