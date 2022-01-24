
# Module for loading a sudoku board from a file named "sudoku.txt"
import copy

def loadFromFile(filename):
    sudokuList = []
    sudokuFile = open(filename)

    for i in range(9):
        sudokuList.append([int(num) for num in sudokuFile.readline() 
                                if num != " " and num != "\n"])

    sudokuFile.close()
    return sudokuList

if __name__ == '__main__':
    currBoard = loadFromFile("sudoku.txt")

    newBoard = copy.deepcopy(currBoard)
    newBoard[1][1] = 600
    for i in range(9):
        print(currBoard[i])
    for i in range(9):
        print(newBoard[i])
