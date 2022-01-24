from validateSudoku import validateSolution, validInput
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
        while True:
            try:
                newCoords = input("> ")
                coordsList = [char.upper() for char in newCoords if char != " "]
                if not validInput( coordsList  ):
                    raise ValueError
                break
            except ValueError:
                print('Invalid number, please enter a valid one.')
        
                
        targetColumn = columnCords.index(coordsList[0].upper())
        targetRow    = coordsList[1]
        targetNumber = coordsList[2]

        currBoard[int(targetRow)-1][int(targetColumn)] = targetNumber



        
        
