from modules.validateSudoku import validateSolution, validInput
from modules.drawSudoku import printBoard
from modules.loadSudoku import loadFromFile
from os import system
from copy import deepcopy


if __name__ == '__main__':
    originalBoard = loadFromFile("sudoku.txt")
    currBoard = deepcopy(originalBoard) # keep original and current separate for
                                        #  drawing the board, deepcopy is
    gameActive = True                   #  useful as normal copy methods don't
                                        #  really work.
    while gameActive :                
        printBoard(currBoard, originalBoard)

        if validateSolution(currBoard):
            print("\t\tYOU WON\n\n")
            break
        
        print("Enter next move: [ > COLUMN ROW NUMBER ]")
        while True:
            try:
                newCoords = input("> ")
                coordsList = [char.upper() for char in newCoords if char != " "] 
                    # Add raw user input to a list and
                    #   check it with a function
        
                if not validInput(coordsList):
                    raise IndexError
        
                columnCords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
                targetColumn = int(columnCords.index(coordsList[0].upper()))
                targetRow    = int(coordsList[1])-1
                targetNumber = int(coordsList[2])

                if originalBoard[targetRow][targetColumn] != 0:
                    raise ValueError
                break

            except IndexError:
                printBoard(currBoard, originalBoard)
                print('Invalid move, please enter a valid one.')

            except ValueError:
                printBoard(currBoard, originalBoard)
                print('Original positions cannot be overwritten,')
                print(' please enter a valid move.')
                

        currBoard[targetRow][targetColumn] = targetNumber



        
        
