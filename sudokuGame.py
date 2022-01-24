from multiprocessing.sharedctypes import Value
from validateSudoku import validateSolution, validInput
from drawSudoku import printBoard
from loadSudoku import loadFromFile
from os import system
from copy import deepcopy



if __name__ == '__main__':
    

    originalBoard = loadFromFile("sudoku.txt")
    currBoard = deepcopy(originalBoard) 
    columnCords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    gameActive = True
    while (gameActive) :

        printBoard(currBoard, originalBoard)
        if validateSolution(currBoard):
            print("          YOU WON")
            print(" ")
            break
        print("Enter next move: [ > COLUMN ROW NUMBER ]")
        while True:
            try:
                newCoords = input("> ")
                coordsList = [char.upper() for char in newCoords if char != " "]
        
                if not validInput( coordsList  ):
                    raise IndexError
        
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



        
        
