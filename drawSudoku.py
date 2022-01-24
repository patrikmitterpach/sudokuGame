def printBoard( board ):
    assert(len(board)    == 9)
    assert(len(board[0]) == 9)

    boardChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    print(" ", end=" ")
    for i in range(9):
        print(f'\033[1m{boardChars[i]}\033[0m', end=" ")
    print(" ")
    for i in range(9):
        print(f'\033[1m{i}\033[0m', end=" ")
        for ii in range(8):
            print(board[i][ii], end = " ")
        print(board[i][8])