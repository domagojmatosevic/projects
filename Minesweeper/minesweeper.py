# Author: Domagoj Matosevic
# Just a simple mindsweeper game played in the terminal, without graphics
import random
import itertools
# drawing the board
def draw_board(board):
    index = "   "
    for i in range(len(board)):
        index += " " + str(i+1)
    print(index)
    print("   " + len(board)*" %")
    for i in range(len(board)):
        line = str(i+1) + " % "
        for j in range(len(board[0])):
            line += str(board[i][j]) + " "
        print(line)

# creating the initial board with all the bombs and number tiles
def create_board(height, width, numBombs):
    coordinates = list(set(random.sample(range(0, width*height-1), numBombs)))
    board = [[0]*width for _ in  range(height)]
    for i in coordinates:
        board[int(i/width)][int(i%width)] = '*'
    # Here we add the number values to the tiles that don't have bombs
    for i in range(height):
        for j in range(width):
            if board[i][j] != '*':
                sum = 0
                for element in itertools.product([i-1,i,i+1],[j-1,j,j+1]):
                    if (element[0] == i) & (element[1] == j):
                        continue
                    if (element[0] < 0) | (element[0] >= height):
                        continue
                    if (element[1] < 0) | (element[1] >= width):
                        continue
                    if (board[element[0]][element[1]] == "*"):
                        sum += 1
                board[i][j] = sum
    return board

# A function to check the if the given value is within the given parameters
def input_value(name, lowerbound, uppperbound):
    while(1):
        value = input(f"{name}: ")
        try:
            value = int(value)
            if (value >= lowerbound) & (value <= uppperbound):
                break
            else:
                print("This value is not allowed. Try again.")
        except ValueError:
            print("This value is not allowed. Try again.")
    return value

def play(realBoard, shownBoard, tilesLeft):
    while(1):
        pick = input("Pick a tile: ")
        tiles_coordinates = pick.split(",")
        if len(tiles_coordinates) != 2:
            print("Bad input. Give me coordinates of the tile.")
            continue
        try:
            x = int(tiles_coordinates[0])
            y = int(tiles_coordinates[1])
            if (x > width) | (x < 0):
                print("Bad input. Give me coordinates of the tile.")
                continue
            if (y > height) | (y < 0):
                print("Bad input. Give me coordinates of the tile.")
                continue
            if realBoard[y-1][x-1] == '*':
                print("It's a bomb, you lose")
                draw_board(realBoard)
                return 0
            else:
                shownBoard[y-1][x-1] = realBoard[y-1][x-1]
                tilesLeft -= 1
                if (tilesLeft == 0):
                    print("Congratulations, you've won!")
                    draw_board(realBoard)
                break
        except ValueError:
            print("Bad input. Give me coordinates of the tile.")
            continue
    return tilesLeft



if __name__ == '__main__':

    try:
        file = open('Minesweeper/rules.txt', 'r')
        print(file.read())
    except FileNotFoundError:
        print("Couldn't find the rules.txt file.")

    height = input_value('Height', 2, 5)
    width = input_value('Width', 2, 5)
    numBombs = input_value('Number of bombs', 1, height*width)
    
    print(f"In this game, the given parameters are:\nHeight: {height}\nWidth: {width}\nNumber of Bombs: {numBombs}")
    print("LET THE GAME BEGIN!")

    realBoard = create_board(height, width, numBombs)
    shownBoard = [['H']*width for _ in  range(height)]
    
    game = 'ongoing'
    tilesLeft = width*height - numBombs
    while(tilesLeft != 0):
        draw_board(shownBoard)
        tilesLeft = play(realBoard, shownBoard, tilesLeft)