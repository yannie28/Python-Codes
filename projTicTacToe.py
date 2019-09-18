from random import randrange

boards = {'1': (0,0), '2': (0,1), '3': (0,2),
          '4': (1,0), '5': (1,1), '6': (1,2),
          '7': (2,0), '8': (2,1), '9': (2,2)}

board = [['1','2','3'], ['4','5','6'], ['7','8','9']]

def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    for i in range(3):
        print(("+" + "-"*7)*3 + "+\n" + ("|" + " "*7)*3 + "|")
        print(("|   " + board[i][0] + "   ") + ("|   " + board[i][1] + "   ") + ("|   " + board[i][2] + "   ") + "|")
        print(("|" + " "*7)*3 + "|")
    print(("+" + "-"*7)*3 + "+")

def MakeListOfFreeFields(board): #board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#   
    global avail
    avail = []
    for i in range(3):
        for j in range(3):
            if board[i][j] in boards:
                avail.append(boards[board[i][j]])

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    while True:
        move = int(input("Enter your move: "))
        if move < 10 and move > 0: #move = 1
            if boards[str(move)] in avail: #boards[move] = (0,0)
                #change move to 'O'; update board
                board[boards[str(move)][0]][boards[str(move)][1]] = 'O'
                break
            else:
                print("Position already taken. Please pick another number")
        else:
            print("Invalid move")

    
def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#   
    victory = False
    diagonal = 0
    for i in range(3):
        horizontal = vertical = 0
        for j in range(3):
            if board[i][j] == sign:
                horizontal += 1
            if board[j][i] == sign:
                vertical += 1
            if i == j and board[i][j] == sign:
                diagonal += 1

        if horizontal == 3 or vertical == 3 or diagonal == 3:
            victory = True
            break

    return victory

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#   
    while True:
        move = str(randrange(1,10))
        if boards[move] in avail: #boards[move] = (0,0)
            #change move to 'X'; update board
            board[boards[move][0]][boards[move][1]] = 'X'
            break
    print("Computer moves box " + move)

sign = 'O'
victory = False
avail = ['sample']
MakeListOfFreeFields(board)
DisplayBoard(board)
while not victory and avail:
    if sign == 'O':
        EnterMove(board)
        victory = VictoryFor(board, sign)
        sign = 'X'
    elif sign == 'X':
        DrawMove(board)
        victory = VictoryFor(board, sign)
        sign = 'O'
    MakeListOfFreeFields(board)
    DisplayBoard(board)

if victory and sign == 'O': #opposite since in the while cascade the sign was changed before terminating the loop
    print("The computer wins!")
elif victory and sign == 'X':
    print("You win!")
else:
    print("It's a draw")


