
# Module for loading a sudoku board from a file named "sudoku.txt"
import copy

def loadFromFile(filename, difficulty):
    sudokuList = []
    sudokuFile = open(filename)

    sudokuIndex = difficulty
    newLine = sudokuFile.readline()
    while newLine[0:2] != f'{sudokuIndex}.':
        newLine = sudokuFile.readline()
    boardDescription = newLine[3:-1]
    
    for i in range(9):
        sudokuList.append([int(num) for num in sudokuFile.readline() 
                                if num != " " and num != "\n"])

    sudokuFile.close()
    return sudokuList, boardDescription

if __name__ == '__main__':
    currBoard = loadFromFile("sudoku.txt")

    newBoard = copy.deepcopy(currBoard)
    newBoard[1][1] = 600
    for i in range(9):
        print(currBoard[i])
    for i in range(9):
        print(newBoard[i])
