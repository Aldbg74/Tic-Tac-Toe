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

class TicTacToe:
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