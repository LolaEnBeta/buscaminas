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
        buscaminas[random.randint(0,board_size-1)][random.randint(0,board_size-1)] = "*"
        num_minas-=1

def calculate_neighbours(current_row, current_column, buscaminas, ri, rf, ci, cf):
    neighbours = 0
    for row_index in range(current_row - ri, current_row + rf):
        for column_index in range(current_column - ci, current_column + cf):
            if row_index == current_row and column_index == current_column:
                continue
            if buscaminas[row_index][column_index] == "*":
                neighbours += 1
    buscaminas[current_row][current_column] = neighbours

def calculate_neigbours_in_current_box(current_row, current_column, buscaminas):
    # para la primera fila
    if current_row == 0:
        if current_column == 0:
            calculate_neighbours(current_row, current_column, buscaminas, 0, 2, 0, 2)
        elif current_column == board_size - 1:
            calculate_neighbours(current_row, current_column, buscaminas, 0, 2, 1, 1)
        else:
            calculate_neighbours(current_row, current_column, buscaminas, 0, 2, 1, 2)

    # para la ultima fila
    elif current_row == board_size - 1:
        if current_column == 0:
            calculate_neighbours(current_row, current_column, buscaminas, 1, 1, 0, 1)
        elif current_column == board_size - 1:
            calculate_neighbours(current_row, current_column, buscaminas, 1, 1, 1, 1)
        else:
            calculate_neighbours(current_row, current_column, buscaminas, 1, 1, 1, 2)

    # para filas y columnas centricas
    else:
        if current_column == 0:
            calculate_neighbours(current_row, current_column, buscaminas, 1, 2, 0, 2)
        elif current_column == board_size - 1:
            calculate_neighbours(current_row, current_column, buscaminas, 1, 2, 1, 1)
        else:
            calculate_neighbours(current_row, current_column, buscaminas, 1, 2, 1, 2)

def select_box_one_by_one_to_calculate_neighbours(buscaminas):
    for row_index in range(1, board_size):
        for column_index in range(1, board_size):
            if buscaminas[row_index][column_index] == "*":
                continue
            calculate_neigbours(row_index, column_index, buscaminas)

buscaminas = create_board(board_size)

generate_minas(10, buscaminas)

while True:
    row = int(input("Choose a row: "))
    column = int(input("Choose a column: "))
    if buscaminas[row][column] == "*":
        print("BOOOM")
        exit()
    else:
        calculate_neigbours_in_current_box(row, column, buscaminas)
        print_board(buscaminas)
