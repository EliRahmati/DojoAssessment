import copy


def check_equal(line):
    return all(element == line[0] for element in line)


def is_valid(board, i0, j0, i1, j1):
    if not (0 <= i0 <= 2 and 0 <= j0 <= 2 and 0 <= i1 <= 2 and 0 <= j1 <= 2):
        return False

    if not ((abs(i1 - i0) == 1 and abs(j1 - j0) == 0) or (abs(j1 - j0) == 1 and abs(i1 - i0) == 0)):
        return False

    new_board = copy.deepcopy(board)
    move_element = new_board[i0][j0]
    new_board[i0][j0] = new_board[i1][j1]
    new_board[i1][j1] = move_element

    # rows
    if check_equal(new_board[i0]) or check_equal(new_board[i1]):
        return True

    # columns
    if check_equal([r[j0] for r in new_board]) or check_equal([r[j1] for r in new_board]):
        return True

    return False

main_board = [[1, 2, 3], [4, 4, 5], [5, 3, 4]]

while True:
    print("give the initial location (i0, j0)")
    i0 = int(input())
    j0 = int(input())
    print("give the final location (i1, j1)")
    i1 = int(input())
    j1 = int(input())

    valid = is_valid(main_board, i0, j0, i1, j1)

    if valid:
        print("It is valid")
    else:
        print("not valid")


