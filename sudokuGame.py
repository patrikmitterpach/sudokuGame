from os import system
from copy import deepcopy
from random import randrange

import lib.console as console
from lib.input import loadFromFile
from lib.validation import validSolution, validInput


if __name__ == '__main__':
    # Load difficulty
    gameDifficulty = console.chooseDifficulty()

    originalBoard, boardDescription = loadFromFile("sudoku.txt", gameDifficulty)
    currBoard = deepcopy(originalBoard) # keep original and current separate for
                                        #  drawing the board, deepcopy is
    gameActive = True                   #  useful as normal copy methods don't
                                        #  really work.
    
    while gameActive :                
        console.printBoard(currBoard, originalBoard, boardDescription)

        if validSolution(currBoard):
            print("\t\t   YOU WON\n\n")
            break
        
        print("Enter next move: \n[ > COLUMN ROW NUMBER ]\n")
        while True:
            try:
                newCoords = input(" > ")
                coordsList = [char.upper() for char in newCoords if char != " "] 
                    # Add raw user input to a list and
                    #   check it with a function
                if len(coordsList) != 3 or not validInput(coordsList):
                    raise IndexError
        
                columnCords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
                targetColumn = int(columnCords.index(coordsList[0].upper()))
                targetRow    = int(coordsList[1])-1
                targetNumber = int(coordsList[2])

                if targetRow < 0 or targetRow > 9:
                    raise IndexError
                if targetColumn not in range(10):
                    raise IndexError
                if originalBoard[targetRow][targetColumn] != 0:
                    raise ValueError
                break

            except IndexError:
                console.printBoard(currBoard, originalBoard, boardDescription)
                print('Invalid move, please enter a valid one.\n\n')
            except ValueError:
                console.printBoard(currBoard, originalBoard, boardDescription)
                print('Original positions cannot be overwritten,')
                print('     please enter a valid move.\n')
            except:
                print("\n\n")
                quit()
                

        currBoard[targetRow][targetColumn] = targetNumber



        
        
