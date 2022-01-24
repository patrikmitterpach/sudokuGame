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