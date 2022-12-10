# Tic Tac Toe #
# By Alexis.D AKA Aldbg74 #
# 2022 #
# based on https://geekflare.com/fr/tic-tac-toe-python-code/ #

import random
print ("Welcome to Tic Tac Toe")
print ("You need to use coordonates to play")
print ("The coordonates are like that")
print ("1 2 3")
print ("1 - - ")
print ("2 - - ")
print ("3 - - ")
print ("So for putting a synbol in the middle of the board you need to type 2 2")
print ("Good luck")
print ("")


class TicTacToe:
    def __init__(self):
        self.board = []

def creqte_board():
    for i in range(3):
        row = []
        for j in range(3):
            row.append("-")
        self.board.append(row)

def get_random_first_player(self):
    return randon.randint(0, 1)

def fix_spot(self, row, col, player):
    self.board[row][col] = player

def is_player_win(self, player):
    win = None

    n = len(self.board)

    #checking the rows
    for i in range(n):
        win = True
        for j in range(n):
            if self.board[i][j] != player:
                win = False
                break
        if win:
            return win

    #checking the columns
    for i in range(n):
        win = True
        for j in range(n):
            if self.board[j][i] != player:
                win = False
                break
        if win:
            return win

    #checking the diagonals
    for i in range(n):
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break

    if win:
        return win
    
    win = True
    for i in range(n):
        if self.board[i][n-i-1] != player:
            win = False
            break
    
    if win :
        return win
    return False

    for row in self.board :
        for item in row:
            if item == "-":
                return False
    return True

def is_board_filled(self):
    for row in self.board:
        for item in row:
            if item == "-":
                return False
    return True

def swap_player_turn(self, player):
    return 'x' if player == 'o' else 'o'

def show_board(self):
    for row in self.board:
        for item in row:
            print(item, end=" ")
        print()

def start(self):
    self.create_board()

    player = 'x' if self.get_random_first_player() == 1 else 'o'
    while True:
        print(f"player {player} turn")

        self.show_board()

        # Taking the user input
        row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
        print()

        # fixing the spot
        self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
        if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
        if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
        player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game 
# DU COUP SA MERDE ICI
tic_tac_toe = TicTacToe()
tic_tac_toe.start()