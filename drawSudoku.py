from os import system

def printBoard( board, originalBoard ):
    assert(len(board)    == 9)
    assert(len(board[0]) == 9)

    boardChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    system('clear')

    print(" \N{cherry blossom} |  ", end="")
    for i in range(9):
        print(f'\033[1m{boardChars[i]} \033[0m', end=" ")
        if i % 3 == 2:
                print(" ", end="")
    for i in range(9):
        if i % 3 == 0:
            if i == 0:
                print("\n ---+-------------------------------")
            else:
                print("    | ")
        print(f'\033[1m  {i+1}\033[0m', end=" | ")
        for ii in range(9):

            if originalBoard[i][ii] != 0:
                print(f'[{board[i][ii]}]', end = "")
            elif board[i][ii] == 0:
                print(" _ ", end= "")
            else:
                print(f' {board[i][ii]}', end = " ")
            
            
            
            if ii % 3 == 2:
                print(" ", end="")
        print(" ")
    print("\n")