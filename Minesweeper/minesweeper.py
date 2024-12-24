# Author: Domagoj Matosevic
# Just a simple mindsweeper game played in the terminal, without graphics
import random
def draw_board(board, height, width):
    for i in range(height):
        line = ""
        for j in range(width):
            if board[j*width + i -1] == 0:
                line = line + 'O'
            else:
                line = line + '*'
        print(line)

def create_board(height, width, numBombs):
    coordinates = list(set(random.sample(range(0, width*height-1), numBombs)))
    board = [0]*(width*height)
    for i in coordinates:
        board[i] = 1
    return board

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

def play(board):
    pick = input("Pick a tile.")
    return 'ongoing'



if __name__ == '__main__':
    print("WELCOME TO MINESWEEPER")
    print("The rules are as follows.")
    print("Define the size of the board(maxium is 5x5, and please give me whole number values :) )")
    print("The number of bombs has to lower than the number of tiles on the board.")
    print("First, define the values.")

    height = input_value('Height', 1, 5)
    width = input_value('Width', 1, 5)
    numBombs = input_value('Number of bombs', 1, height*width)
    
    print(f"In this game we have values:\nHeight: {height}\nWidth: {width}\nNumber of Bombs: {numBombs}")
    print("LET THE GAME START!")

    realBoard = create_board(height, width, numBombs)
    
    game = 'ongoing'
    while(game == 'ongoing'):
        draw_board(realBoard, height, width)
        game = play(realBoard,)

