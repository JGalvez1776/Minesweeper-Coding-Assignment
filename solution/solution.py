###
### File:           minesweeper.py
### Author:         Justin Galvez and ...
### Description:    
###

#import sys
#sys.stdout = open('diagonalGame.out','wt')

def main():
    file_name = input("Enter File Name:\n")
    board = read_file(file_name)
    print(board)
    update_grid(board)
    print(board)
    input()
    return
    user_view = make_empty_clone(board)
    count = count_total_moves(board)
    game_status = True
    # NOTE: If code seems very difficult the main loop could be given as starter code
    #       Requiring that students come up with the functions used in main.
    while game_status:
        print("-" * (3 * len(board[0])))
        print_grid(user_view)

        # NOTE: We are going to assume that all commands are valid.
        command = input("\nWhat is your move?\n").lower()
        
        # Could also use sets to store old moves to prevent repeats
        # To make this more challenging you could add other commands (Flags, more validation of moves)

        # NOTE: Can add a little flag command to make it a little harder?
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

def count_total_moves(grid):
    '''
    Counts the number of moves that need to be made for the player to
    win the game. (Counts number of squares that are not mines)

    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    '''
    count = 0
    for row in grid:
        for elem in row:
            if elem != "X":
                count += 1
    return count

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


def dig(grid, coordinate, user_view):
    '''
    Translates an item at a coordinate on the grid to the correspoinding 
    location on the user_view. 

    Parameters:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    coordinate: A string where the first character is the x-position and the 
                characters that follow makes up the y-position for where to dig. 
                NOTE: The x-position is a letter and the y-position is a number.
    user_view:  2D list containing X's representing mines and numbers which are
                either the number of adjacent X's or 0. Unlike grid, some of the
                values are empty meaning the user has not seen the square.
    '''
    # NOTE: May want to make this easier or add in starter code function?
    x = "abcdefghijklmnopqrstuvwxyz".index(coordinate[0])
    y = len(grid) - int(coordinate[1:]) - 1
    # if y < 0:
    #    y *= -1

    user_view[y][x] = grid[y][x]




def update_grid(grid):
    '''
    NOTE: this function can be avoided by putting the numbers in the csv.
    Takes in a field of mines. Populates non-mine squares with the number
    of adjacent mines.
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    '''
    directions = ((0,1),(0,-1),(-1,0),(-1,1),(-1,-1),(1,0),(1,1),(1,-1))
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "X":
                count = 0
                for pos in directions:
                    count += find_mine(grid, x, y, pos)
                grid[y][x] = str(count)

def find_mine(grid, x, y, position):
    '''
    NOTE: this function can be avoided by putting the numbers in the csv.
    Determines if a square from a relative position contains a mine. 
    Returns 1 if there is, otherwise 0
    
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    x:          Integer which is the x postiion to be scanned for mines.
    y:          Integer which is the y postiion to be scanned for mines.
    position:        A tuple containing the relative coordinates to scan
    '''
    scan_position_x = x + position[0]
    scan_position_y = y + position[1]

    if scan_position_x < 0 or scan_position_x > len(grid[0]) - 1 or \
        scan_position_y < 0 or scan_position_y > len(grid) - 1:
        return 0
    if grid[scan_position_y][scan_position_x] == "X":
        return 1
    return 0
                

# NOTE: May want to give as starter code?
def print_grid(grid):
    '''
    Prints out a 2D grid with the y-axis labeled with numbers and the x-axis with letters.

    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                the number of adjacent X's.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    count = len(grid) - 1
    for y in range(len(grid)):
        print(format(count, "2d"), end= ' ')
        for x in range(len(grid[0])):
            print("[" + grid[y][x] + "]", end="")
        print()
        count -= 1
    print("  ", end='')
    for i in range(len(grid[0])):
        print("  " + letters[i], end='')
    print()

# NOTE: May want to give as starter code
def make_empty_clone(grid):
    '''
    Returns a 2D list which is the same dimensions as a passed in grid.
    '''
    outer = [""] * len(grid)
    for i in range(len(outer)):
        outer[i] = [' '] * len(grid[0])
    return outer
    
# NOTE: If above given as start code be sure to mention how the 2D list is to be formatted
def read_file(filename):
    '''
    Takes a given mine csv file and converts it to a 2D list.

    Parameters:
    filename:   The name of a csv file to be read.
    '''
    file = open(filename, 'r')
    x = int(file.readline())
    y = int(file.readline())
    grid = [''] * y
    for i in range(y):
        row = file.readline().strip("\n").split(",")

        for j in range(len(row)):
            # NOTE: May just need to change the csv files to prevent this
            if int(row[j]) == 1:
                row[j] = "X"
            else:
                row[j] = '0'
        grid[i] = row
    return grid

if __name__ == "__main__":
    main()
