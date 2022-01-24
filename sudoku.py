from validateSudoku import validateSolution
from drawSudoku import printBoard
from os import system


if __name__ == '__main__':
    
    currBoard = [[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0] ]
    columnCords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    gameActive = True
    while (gameActive) :
        system('clear')
        printBoard(currBoard)
        print("Enter next move: [ > COLUMN ROW NUMBER]")
        newCoords = input("> ")
        coordsList = [char for char in newCoords]
        
        targetColumn = columnCords.index(coordsList[0].upper())
        targetRow =    coordsList[1]
        targetNumber = coordsList[2]

        currBoard[int(targetRow)-1][int(targetColumn)] = targetNumber



        
        
