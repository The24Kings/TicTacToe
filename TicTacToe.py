from random import *
import math
import time


class TicTacToe:
    _p1 = ""
    _p2 = ""

    def __init__(self, board):
        self._board = board

    def new_board(self):
        self._board = [" ", " ", " ",
                       " ", " ", " ",
                       " ", " ", " "]

    def get_space(self, spot):
        return self._board[spot]

    @property
    def board(self):
        return self._board

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, choice):
        self._p1 = choice

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, choice):
        self._p2 = choice

    def place(self, spot, choice):
        if self._board[spot] == " ":
            self._board[spot] = choice
        else:
            return False

    def display(self):
        print("")
        for spot in range(len(self._board)):
            if spot % 3 == 0:
                print("", end=" ")

            print(self._board[spot], end=" ")

            if spot % 3 <= 1:
                print("|", end=" ")

            if spot % 3 == 2 and not (spot == 0 or spot == 8):
                print("\n---|---|---")

    def check(self):
        horizontal, vertical, diagonal = 0, 0, 0

        for spot in range(3):
            # Horizontal
            for i in range(3):
                if self._board[spot*i] == "X":
                    horizontal += 1
            pass

            # Vertical

            # Diagonal

        if horizontal == 3 or vertical == 3 or diagonal == 3:
            return True
        else:
            return False

    def player2(self, turn):
        if turn == 1:
            self._board[math.floor(uniform(1, 9))] = self._p2
        else:
            pass


def main():
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    game = TicTacToe(board)

    turn = 1
    spot = 0
    choosing = True
    win = False

    welcome = open("Welcome.txt", "r")
    print(welcome.read())

    while choosing:
        game.p1 = input("Pick X or O: ")
        if game.p1 == "X":
            game.p2 = "O"
            choosing = False

        elif game.p1 == "O":
            game.p2 = "X"
            choosing = False
        else:
            print("\nPlease choose X or O!\n")

    while not win:
        game.display()

        try:
            spot = int(input(f"\nWhich space would you like to place an {game.p1}?\n> "))
        except ValueError:
            print("\nPlease Choose a number between 1-9!\n")

        game.place(spot - 1, game.p1)
        game.display()

        if not game.check():  # Checks is player 1 won before letting p2 go
            print("\nWaiting for Player 2 to choose...\n")
            time.sleep(2)

            game.player2(turn)
            game.check()


if __name__ == "__main__":
    main()
