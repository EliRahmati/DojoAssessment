import copy


def is_valid_move(line):
    count = 1
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            count = count + 1
        else:
            count = 1
        if count >= 3:
            return True

    return False


def get_block(board, i0, j0):
    return [board[i0 + i][j0:j0 + 3] for i in range(3)]


def is_equal(line):
    return all(element == line[0] for element in line)


def check_bomb(block):
    for i in range(3):
        for j in range(3):
            if is_equal(block[i]) and is_equal([r[j] for r in block]):
                return True


def is_valid(board, i0, j0, i1, j1):
    n = len(board)
    if not (0 <= i0 <= n - 1 and 0 <= j0 <= n - 1 and 0 <= i1 <= n - 1 and 0 <= j1 <= n - 1):
        print("not valid")
        return

    if not ((abs(i1 - i0) == 1 and abs(j1 - j0) == 0) or (abs(j1 - j0) == 1 and abs(i1 - i0) == 0)):
        print("not valid")
        return

    new_board = copy.deepcopy(board)
    move_element = new_board[i0][j0]
    new_board[i0][j0] = new_board[i1][j1]
    new_board[i1][j1] = move_element

    # bombs
    for i0 in range(2):
        for j0 in range(2):
            block = get_block(new_board, i0, j0)
            if check_bomb(block):
                print("you got one bomb")
                return

    # rows
    if is_valid_move(new_board[i0]) or is_valid_move(new_board[i1]):
        print("You got 1 point")
        return

    # columns
    if is_valid_move([r[j0] for r in new_board]) or is_valid_move([r[j1] for r in new_board]):
        print("You got 1 point")
        return

    print("not valid")
    return

# main_board = [
#     [2, 1, 2, 3],
#     [5, 4, 4, 5],
#     [2, 5, 3, 4],
#     [6, 7, 6, 1]
# ]

# (3, 2) to (2, 2) gives a bomb
main_board = [
    [6, 7, 4, 6],
    [2, 1, 4, 3],
    [5, 4, 1, 4],
    [2, 5, 4, 5]
]
while True:
    print("give the initial location (i0, j0)")
    i0 = int(input())
    j0 = int(input())
    print("give the final location (i1, j1)")
    i1 = int(input())
    j1 = int(input())

    is_valid(main_board, i0, j0, i1, j1)

