# Dont forget to debug the thing about the string in the guess_row and guess_col
# Go back to 19/19 on codecademy to finish the extra credit

from random import randint

board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(0, 5):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 4:
            print ("Game Over")
        print_board(board)
        print ("Turn", turn + 1)
