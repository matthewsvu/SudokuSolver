board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    is_empty = find_empty(bo)
    if not is_empty:
        return True
    else:
        row, col = is_empty

    for nums in range(1,10):
        if validate_board(bo, nums, (row, col)):
            bo[row][col] = nums

            if solve(bo):
                return True
                
            bo[row][col] = 0

    return False

def validate_board(bo, num, pos):
    #check the row
    for row in range(len(bo[0])):
        if bo[pos[0]][row] == num and pos[1] != num:
            return False
    #check the columns
    for col in range(len(bo)):
        if bo[col][pos[1]] == num and pos[0] != num:
            return False
    #check the box
    box_y = pos[0] // 3
    box_x = pos[1] // 3
    #check the box we're in
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
# function that will print the board 
def print_board(bo):
    for col in range(len(bo)):
        if col % 3 == 0 and col != 0:
            print("- - - - - - - - - - - - - ")
        for row in range(len(bo[0])):
            if row % 3 == 0 and row != 0: # print a | every 3 tiles
                print(" | ", end="")
            if row == 8: # hit the end of the row
                print(bo[col][row])
            else:
                print(str(bo[col][row]) + " ", end="")
# returns the location that contains a 0 - meaning that's is an empty tile
def find_empty(bo):
    for col in range(len(bo)):
        for row in range(len(bo[0])):
            if bo[col][row] == 0 : # is empty position return the location
                return (col, row)
    return None # means there isn't an empty tile in the board

print_board(board)
solve(board)
print("_______________________")
print_board(board)
print("_______________________")