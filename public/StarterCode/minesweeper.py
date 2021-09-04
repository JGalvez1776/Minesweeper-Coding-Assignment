###
### File: minesweeper.py
### Author: Justin Galvez
### Description: Provides a main function and some helper functions 
###              to help students implement a text-based minesweeper
###              game.
### DO NOT MODIFY ANY OF THIS FILE 

# This imports all functions from utils.
from utils import *

def main():
    # NOTE: You should not change anything in main past this point. 
    #       An exception is if you are implementing a graphics portion.

    file_name = input("Enter File Name:\n")
    board = read_file(file_name)
    update_grid(board)
    user_view = make_empty_clone(board)
    count = count_total_moves(board)
    game_status = True
    while game_status:
        print("-" * (3 * len(board[0])))
        print_grid(user_view)
        # NOTE: We are going to assume that all commands are valid.
        command = input("\nWhat is your move?\n").lower()
    
        if command == "exit":
            print("Thank you for playing")
            return
        else:
            dig(board, command, user_view)
        count -= 1
        game_status = determine_game_status(user_view, count)
    print_grid(user_view)
    print("Game Over")
    if count == 0:
        print("You Win!")
    print_grid(board)



def determine_game_status(grid, count):
    '''
    Returns a boolean which is True if the game should continue or 
    False if the game is over. False is returned if a mine has been
    revealed or count is 0 meaning there are no squares without mines
    that are not revealed.
    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    count:      Integer which is the number of mineless squares left to be revealed.
    '''
    for row in grid:
        for elem in row:
            if elem == "X":
                return False

    return count != 0

def find_mine(grid, x, y, position):
    '''
    Determines if a square from a relative position contains a mine. 
    Returns 1 if there is, otherwise returns 0.
    
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    x:          Integer which is the x postiion to be scanned for mines.
    y:          Integer which is the y postiion to be scanned for mines.
    position:        A tuple containing the relative coordinates to scan

    Examples:
    grid = [["X", 0],
            [0, "0"]]
    
    find_mine(grid, 0, 0, (0, 0)))    Returns: 1
    find_mine(grid, 0, 0, (1, 0)))    Returns: 0
    find_mine(grid, 0, 0, (0, 1)))    Returns: 1
    find_mine(grid, 0, 0, (1, 1)))    Returns: 0
    find_mine(grid, 0, 0, (20, 20)))  Returns: 0  
    '''
    # NOTE: You should not need to change this function.
    scan_position_x = x + position[0]
    
    # Notice how position[1] is added to y. 
    # Your grid should have the top row at index 0 so a positive y position goes down the grid
    scan_position_y = y + position[1]

    if scan_position_x < 0 or scan_position_x > len(grid[0]) - 1 or \
        scan_position_y < 0 or scan_position_y > len(grid) - 1:
        return 0
    if grid[scan_position_y][scan_position_x] == "X":
        return 1
    return 0

#main()

grid = [["X", 0],
            [0, "0"]]
    
print(find_mine(grid, 0, 0, (0, 0)))   #Returns: 1
print(find_mine(grid, 0, 0, (1, 0)))   #Returns: 0
print(find_mine(grid, 1, 1, (-1, -1)))    #Returns: 1
print(find_mine(grid, 0, 0, (1, 1)))    #Returns: 0
print(find_mine(grid, 0, 0, (20, 20)))  #Returns: 0  