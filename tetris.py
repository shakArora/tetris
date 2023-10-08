rows = 15
columns = 10
print("Welcome to Tetris\nCreated By shakArora\n\nRules: \na/d: Left and right\ns: Down two\nw: Rotate\nenter: Down one\nHave fun playing!")
import random
import time
def visual():
    global board
    board1 = []
    for i in range(rows):
        row1 = []
        for n in range(columns):
            row1.append('-')
        board1.append(row1)
    return board1
board = visual()
def printVisual():
    for i in range(rows):
        row_str = "|"
        for j in range(columns):
            row_str += f" {board[i][j]}"
        row_str += " |"
        print(row_str)
    print("‾‾‾‾‾‾‾‾‾‾‾\n\n")
def clear_block(startRow, startCol, block_type):
    for i in range(len(block_type)):
        for j in range(len(block_type[0])):
            if block_type[i][j] == 'X':
                board[startRow + i][startCol + j] = '-'
def create_block(startRow, startCol, block_type):
    for i in range(len(block_type)):
        for j in range(len(block_type[0])):
            if block_type[i][j] == 'X':
                board[startRow + i][startCol + j] = 'X'
def rotate_block(block_type):
    return list(zip(*reversed(block_type)))
blocks = [
    [
        ['X', 'X'],
        ['X', 'X']
    ],
    [
        ['X', 'X', 'X', 'X']
    ],
    [
        ['X', 'X', 'X'],
        ['-', 'X', '-']
    ],
    [
        ['X', 'X', 'X'],
        ['X', '-', '-']
    ],
    [
        ['X', 'X', 'X'],
        ['-', '-', 'X']
    ],
    [
        ['-', 'X', 'X'],
        ['X', 'X', '-']
    ],
    [
        ['X', 'X', '-'],
        ['-', 'X', 'X']
    ]
]
def check_collision(startRow, startCol, block_type):
    for i in range(len(block_type)):
        for j in range(len(block_type[0])):
            if block_type[i][j] == 'X':
                if startRow + i >= rows or startCol + j < 0 or startCol + j >= columns or board[startRow + i][startCol + j] == 'X':
                    return True
    return False
def reset_block():
    global x, y, current_block
    x = 0
    y = (columns - len(current_block[0])) // 2
    current_block = random.choice(blocks)
def check_and_clear_rows():
    global x, y, current_block
    for i in range(rows):
        if all(cell == 'X' for cell in board[i]):
            for j in range(i, 0, -1):
                board[j] = board[j - 1].copy()
            board[0] = ['-'] * columns
            x += 1
    reset_block()
x = 0
y = 0
current_block = random.choice(blocks)
last_time = time.time()
move_down_time = last_time
while True:
    current_time = time.time()
    if current_time - move_down_time >= 0.5:
        move_down_time = current_time
        if x + len(current_block) < rows:
            clear_block(x, y, current_block)
            if not check_collision(x + 1, y, current_block):
                x = x + 1
                create_block(x, y, current_block)
            else:
                for i in range(len(current_block)):
                    for j in range(len(current_block[0])):
                        if current_block[i][j] == 'X':
                            board[x + i][y + j] = 'X'
                check_and_clear_rows()
        else:
            for i in range(len(current_block)):
                for j in range(len(current_block[0])):
                    if current_block[i][j] == 'X':
                        board[x + i][y + j] = 'X'
            check_and_clear_rows()
    printVisual()
    ask = input("move: ")
    if ask == 'd':
        if y + len(current_block[0]) < columns:
            clear_block(x, y, current_block)
            y = y + 1
            if not check_collision(x, y + 1, current_block):
                create_block(x, y, current_block)
    elif ask == 'a':
        if y > 0:
            clear_block(x, y, current_block)
            y = y - 1
            if not check_collision(x, y - 1, current_block):
                create_block(x, y, current_block)
    elif ask == 'w':
        rotated_block = rotate_block(current_block)
        if x + len(rotated_block) <= rows and y + len(rotated_block[0]) <= columns:
            clear_block(x, y, current_block)
            if not check_collision(x, y, rotated_block):
                current_block = rotated_block
                create_block(x, y, current_block)
    elif ask == 's':
        if x + 2 < rows:
            clear_block(x, y, current_block)
            if not check_collision(x + 2, y, current_block):
                x = x + 2
                create_block(x, y, current_block)
    elif ask == 'q':
        break
