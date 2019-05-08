import random
board_size = 8

def create_board(board_size):
    board = []
    for row in range(board_size):
        row = []
        for column in range(board_size):
            row.append("-")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for column in row:
            print(column, " ", end="")
        print("")

def generate_minas(num_minas, buscaminas):
    while num_minas > 0:
        buscaminas[random.randint(1,6)][random.randint(1,6)] = "*"
        num_minas-=1

def calculate_neigbours(current_row, current_column, buscaminas):
    neighbours = 0
    for row_index in range(current_row - 1, current_row + 2):
        for column_index in range(current_column - 1, current_column + 2):
            if row_index == current_row and column_index == current_column:
                continue
            if buscaminas[row_index][column_index] == "*":
                neighbours += 1
    buscaminas[current_row][current_column] = neighbours   

buscaminas = create_board(board_size)

generate_minas(10, buscaminas)

calculate_neigbours(1, 1, buscaminas)

print_board(buscaminas)
