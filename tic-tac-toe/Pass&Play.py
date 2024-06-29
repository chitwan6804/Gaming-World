import os

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else ' ')
    one = 'X' if xState[1] else ('O' if zState[1] else ' ')
    two = 'X' if xState[2] else ('O' if zState[2] else ' ')
    three = 'X' if xState[3] else ('O' if zState[3] else ' ')
    four = 'X' if xState[4] else ('O' if zState[4] else ' ')
    five = 'X' if xState[5] else ('O' if zState[5] else ' ')
    six = 'X' if xState[6] else ('O' if zState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if zState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if zState[8] else ' ')
    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, zState):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            printBoard(xState,zState)
            print("X won the match!")
            return 1
        if zState[win[0]] + zState[win[1]] + zState[win[2]] == 3:
            printBoard(xState,zState)
            print("O won the match!")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    moves = 0
    print("Welcome to Tic Tac Toe")

    while True:
        os.system('CLS')
        printBoard(xState, zState)
        if turn == 1:
            print("X's Turn")
        else:
            print("O's Turn")

        while True:
            try:
                value = int(input("Please enter a value (0-8): "))
                if value < 0 or value > 8:
                    print("Invalid input. Please enter a number between 0 and 8.")
                elif xState[value] == 1 or zState[value] == 1:
                    print("Cell already taken. Choose another cell.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1

        moves += 1
        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            break

        if moves == 9:
            print("It's a draw!")
            break

        turn = 1 - turn