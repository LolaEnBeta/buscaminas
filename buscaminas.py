import random
board_size = 8

def create_board(board_size):
    board = []
    for row in range(board_size):
        row = []
        for column in range(board_size):
            row.append("*")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for column in row:
            print(column, " ", end="")
        print("")

def generate_minas(num_minas, buscaminas):
    while num_minas > 0:
        buscaminas[random.randint(0,7)][random.randint(0,7)] = "O"
        num_minas-=1

buscaminas = create_board(board_size)

generate_minas(10, buscaminas)

print_board(buscaminas)
