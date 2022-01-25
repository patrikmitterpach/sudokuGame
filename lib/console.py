from os import system
from random import randrange

# Drawing the board is pretty complicated as different parts have to be
#   printed simultaneously, leaving a pretty messy codebase. 

def printDifficultyScreen():
    system('clear')
    print("             \n\n\n\
        Choose difficulty:  \n\
            0: Random       \n\
             1: Easy        \n\
              2: Medium     \n\
               3: Hard      \n")

def chooseDifficulty():
    difficultyDictionary = { -1 : 0, # testing board, or an easter egg B) 
                              0 : randrange(1,7),
                              1 : randrange(1,3),
                              2 : randrange(3,5),
                              3 : randrange(5,7)  }                        
    printDifficultyScreen()

    while True:
        try:
            userChoice = int(input("      > "))
            if userChoice not in range(-1, 4):
                raise ValueError
            break
        except ValueError:
            system('clear')
            printDifficultyScreen()
            print("\t Invalid choice")
            print("\t  [ > NUMBER ]\n")
        except:
            print("\n")
            quit()
    
    
    return difficultyDictionary[userChoice]

def printBoard( board, originalBoard, tag):
    assert(len(board)    == 9)
    assert(len(board[0]) == 9)

    boardChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    boardSymbol = "\N{cherry blossom}" #  emoji to display 
    system('clear')                    #    in the top left corner

    print(f'\n {boardSymbol} |  ', end="") # end="" to ignore newline
    for i in range(9):
        print(f'\033[1m{boardChars[i]}  \033[0m', end="") # unix code for printing
        if i % 3 == 2:                                    #     in bold.
                print("   ", end="") # column separation
    
    for i in range(9): 
        # Grid border
        if i % 3 == 0 and i == 0:
            print("\n ---+----------------------------------")
        elif i % 3 == 0:
            print("    | ") # row separation for boxes
        
        # Row numbers in bold, i+1 to compensate
        #  for all ranges starting at zero
        print(f'\033[1m  {i+1}\033[0m ', end="| ")

        # Board numbers
        #  - given positions in square brackets
        #  - 0s in the list represented as _        
        #  - all numbers printed with a space on both sides
        #       for alignment
        for ii in range(9):
            if originalBoard[i][ii] != 0:
                print(f'[{board[i][ii]}]', end = "")
            elif board[i][ii] == 0:
                print(" _ ", end= "")
            else:
                print(f' {board[i][ii]} ', end = "")
            
            
            # Column separation for box clarity
            if ii % 3 == 2:
                print("   ", end="")
        if i == 0:   print( "  Difficulty:")
        elif i == 1: print(f'  {tag}')
        elif i == 3: print( "  To delete a number,")
        elif i == 4: print( "  enter the coordinates")
        elif i == 5: print( "  with 0 as NUMBER.")

        else:
            print(" ")
    print("\n")