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
        random_row = random.randint(0,board_size-1)
        random_column = random.randint(0,board_size-1)

        buscaminas[random_row][random_column] = "*"
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

    return neighbours

def calculate_neigbours_in_current_box(current_row, current_column, buscaminas):

    if current_row == 0: # first row
        ri = 0
        rf = 2
    elif current_row == board_size - 1: # last row
        ri = 1
        rf = 1
    else: # middle rows
        ri = 1
        rf = 2

    if current_column == 0: # first column
        ci = 0
        cf = 2
    elif current_column == board_size - 1: # last column
        ci = 1
        cf = 1
    else: # middle column
        ci = 1
        cf = 2

    return calculate_neighbours(current_row, current_column, buscaminas, ri, rf, ci, cf)

def select_box_one_by_one_to_calculate_neighbours(buscaminas):
    for row_index in range(1, board_size):
        for column_index in range(1, board_size):
            if buscaminas[row_index][column_index] == "*":
                continue
            calculate_neigbours(row_index, column_index, buscaminas)

def get_user_input():
    row = int(input("Choose a row: "))
    column = int(input("Choose a column: "))

    while row < 0 or row >= board_size or column < 0 or column >= board_size:
        row = int(input("Choose a row: "))
        column = int(input("Choose a column: "))

    return row, column

buscaminas = create_board(board_size)

generate_minas(10, buscaminas)

secret_buscaminas = create_board(board_size)

while True:
    print_board(secret_buscaminas)
    row, column = get_user_input()

    if buscaminas[row][column] == "*":
        print_board(buscaminas)
        print("¡¡¡BOOOM!!!")
        exit()
    else:
        neighbours_in_current_box = calculate_neigbours_in_current_box(row, column, buscaminas)
        secret_buscaminas[row][column] = neighbours_in_current_box
