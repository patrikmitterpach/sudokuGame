from validateSudoku import validateSolution, validInput
from drawSudoku import printBoard
from os import system


if __name__ == '__main__':
    

    originalBoard = [   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5], 
                        [3, 4, 5, 2, 8, 6, 1, 7, 0] ]

    currBoard = list(originalBoard) 
    columnCords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    gameActive = True
    while (gameActive) :

        system('clear')
        printBoard(currBoard)
        if validateSolution(currBoard):
            print("          YOU WON")
            print(" ")
            break
        print("Enter next move: [ > COLUMN ROW NUMBER]")
        while True:
            try:
                newCoords = input("> ")
                coordsList = [char.upper() for char in newCoords if char != " "]
                if not validInput( coordsList  ):
                    raise ValueError
                break
            except ValueError:
                print('Invalid move, please enter a valid one.')
        
                
        targetColumn = int(columnCords.index(coordsList[0].upper()))
        targetRow    = int(coordsList[1])-1
        targetNumber = int(coordsList[2])

        currBoard[targetRow][targetColumn] = targetNumber



        
        
