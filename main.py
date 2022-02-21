from game import Game
from update import Updater

board = Game()
board.check_win() == False
print(Updater().display)
while board.check_win() == False:
    user_input = int(input('What position?\n')) #takes a position based on keypad
    board.update_board(user_input)
    board.check_win()
    if board.check_win() == True:
        board.who_won()
