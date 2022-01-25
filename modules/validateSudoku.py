# Validation.py
# Repurposed copy of sudokuValidation.py from /algorithmicProblems

# Sudoku is valid if:
#   each row  contains digits 1-9
#   each line contains digits 1-9
#   each 3x3  contains digits 1-9

def validateSolution(board):
    digitList = [1,2,3,4,5,6,7,8,9]

    # Row validation
    for i in range(9):
        digitListCopy = list(digitList)

        for ii in range(9):
            if board[i][ii] in digitListCopy:
                digitListCopy.remove(board[i][ii]) 

        if digitListCopy:
            return False
        
    # Column validation
    for i in range(9):
        digitListCopy = list(digitList)
        
        for ii in range(9):
            if board[ii][i] in digitListCopy:
                digitListCopy.remove(board[ii][i]) 

        if digitListCopy:
            return False

    # Box validation
    for currBoxRow in range(0, 9, 3):       # values of 0,3,6
        for currBoxColumn in range(0,9,3):  
            digitListCopy = list(digitList) 
            
            for i in range(currBoxRow, currBoxRow + 3): # each loop starts at 0/3/6 and continues
                for ii in range(currBoxColumn, currBoxColumn + 3): # to 3/6/9 respectively.
                        if board[i][ii] in digitListCopy:
                            digitListCopy.remove(board[i][ii])
            if digitListCopy:
                return False
    return True

def validInput(inputList):
    validColumns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    
    # Number of elements has to be 
    #   exactly three (column, row, number)
    if len(inputList) != 3:
        return False

    try:
        currColumn = inputList[0]           # I've built myself into a terrible
        currRow    = int(inputList[1])      #  situation with the input handling,
        currValue  = int(inputList[2])      #  but this should handle most cases..
    except:
        return False
    
    # Column has to belong to the list of columnCords
    if currColumn not in validColumns:
        return False
    if currRow > 9 or currRow < 0:
        return False
    if currValue > 9 or currValue < 0:
        return False

    return True

if __name__ == '__main__':
    # Testing cases
    assert ( validateSolution([ [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                [2, 8, 7, 4, 1, 9, 6, 3, 5], # Valid testcase
                                [3, 4, 5, 2, 8, 6, 1, 7, 9]] ) == True )

    assert ( validateSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [6, 7, 2, 1, 9, 0, 3, 4, 9],
                            [1, 0, 0, 3, 4, 2, 5, 6, 0],
                            [8, 5, 9, 7, 6, 1, 0, 2, 0],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 0, 1, 5, 3, 7, 2, 1, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5], # Invalid digits
                            [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False )

    assert ( validateSolution([[1, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [1, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [1, 5, 9, 7, 6, 1, 4, 2, 3],
                            [1, 2, 6, 8, 5, 3, 7, 9, 1],
                            [1, 1, 3, 9, 2, 4, 8, 5, 6],
                            [1, 6, 1, 5, 3, 7, 2, 8, 4],
                            [1, 8, 7, 4, 1, 9, 6, 3, 5], # Invalid column
                            [1, 4, 5, 2, 8, 6, 1, 7, 9]] ) == False) 

    assert ( validateSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5], # Invalid row
                            [1, 1, 1, 1, 1, 1, 1, 1, 1]] ) == False )

    assert ( validateSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 5, 3, 4, 2, 8, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 5, 8, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 5, 8, 6],
                            [9, 6, 1, 8, 3, 7, 2, 5, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5], # Invalid box
                            [3, 4, 8, 2, 5, 6, 1, 7, 9]] ) == False )