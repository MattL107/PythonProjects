# sudokuSolver.py

# setting the blank character (b = blank)

import copy

b = 0

puzzle = [[b,7,b,b,2,b,b,4,6],[b,6,b,b,b,b,8,9,b],[2,b,b,8,b,b,7,1,5],
          [b,8,4,b,9,7,b,b,b],[7,1,b,b,b,b,b,5,9],[b,b,b,1,3,b,4,8,b],
          [6,9,7,b,b,2,b,b,8],[b,5,8,b,b,b,b,6,b],[4,3,b,b,8,b,b,7,b]]

# loop through every square in the list
# check if the square is empty
# if it *is* empty (i.e. contains the blank value) check which
# values it can take, by removing the values in the same
# row and column from a copy of a list 1-9
# then also make some code to check the box
# once you have worked out which values it can take, run through
# the whole grid and assign any fully-determined blanks
# then repeat either until the puzzle is complete or there are
# no more fully determined blanks. if the puzzle is incomplete,
# we have to start making guesses, and potentially backtracking
# if they turn out to be incorrect


digits = [1,2,3,4,5,6,7,8,9]
puzzleLists = []

rows = list(range(9))
columns = list(range(9))

'''
for row in rows:
    for column in columns:
        if puzzle[row][column] == b:
            elementValues = copy.deepcopy(digits).remove(# all values in same row, column or square
          '''
# 
                # we will need yet another nested loop to do the
                # .remove() for the row and columns (and boxes)

# boxValues function - takes row and column indexes as input and returns a list of size-2 lists of
# the indexes of the elements in the same box. So these can be cycled through to refer to the
# elements in the same box in the puzzle, similar to how columns and lists can be cycled through
# easily

def boxValues(row,column):
    for box in range(9):
        try:
            boxIndex = puzzleIndexes[box].index([row,column])
            boxValue = puzzleIndexes[box]
            break
        except ValueError:
            continue
    return boxValue
                
puzzleIndexes = []
for bigRow in range(3):
    for bigColumn in range(3):
        localBox = []
        for row in range(3):
            for column in range(3):
                localBox.append([row+bigRow*3,column+bigColumn*3])
        puzzleIndexes.append(localBox)

def elementPotentialValues(puzzle):
    puzzleElementValues = []
    for row in rows:
        lineElementValues = []
        for column in columns:
            if puzzle[row][column] == b:
                numbersInColumn = []
                for rowNumber in rows:
                    numbersInColumn.append(puzzle[rowNumber][column])
                numbersInRow = []
                for columnNumber in columns:
                    numbersInRow.append(puzzle[row][columnNumber])
                numbersInBox = []
                for Row, Column in boxValues(row,column):
                    numbersInBox.append(puzzle[Row][Column])
                invalidValues = numbersInColumn + numbersInRow + numbersInBox
                elementValues = copy.deepcopy(digits)
                for number in invalidValues:
                    if number in elementValues:
                        elementValues.remove(number)
                lineElementValues.append(elementValues)
            else:
                lineElementValues.append([0])
        puzzleElementValues.append(lineElementValues)
    return puzzleElementValues
            
print(elementPotentialValues(puzzle))

# def elementAssigner(puzzle, puzzleElementValues):
    
                

# once we have found a blank square in a particular row and column:
# cycle through all rows for the column and append all non-blanks to a list
# cycle through all colums for the row and append all non-blanks to a list
# remove all numbers from these lists from a copy of the digits list
# save this list to a 9x9 array of lists, where each value in the array is a list of possible numbers
# for the element at that position (so essentially we have a 3D array)



# with this code, we should be left with elementValues which is the full list of possible numbers
# maybe also add some code like:

#if len(elementValues) == 1:
#    puzzle[row][column] = elementValues[0]

# now we have fully developed the code for generating an array of lists of potential element values
# what are the next steps?
# - cycle through all elements in the puzzle
# - if length of elementvalues list is 1, and the number != 0, then we update the puzzle value at that
# - index to the value in the elementvalues array
# (this is essentially its own process, which we should be able to put into a function)
# - then put the elementalues list maker into its own function
# - then the whole process is a matter of:
# elementValues()
# elementAssigner()
# and then looping these one after another until the state of the puzzle is the same for two successive runs
# at this point, check if the puzzle is complete. if it is, congrats! if not, then we need to start coding
# in the guessing part of the algorithm

