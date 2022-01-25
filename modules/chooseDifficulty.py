from os import system
from random import randrange

def printDifficultyScreen():
    system('clear')
    print("             \n\n\n\
        Choose difficulty:  \n\
            0: Auto         \n\
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
    
    
    return difficultyDictionary[userChoice]

if __name__ == '__main__':
    print( chooseDifficulty() )