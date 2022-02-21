class Updater():
    def __init__(self):
        self.board = {1:'',
                      2: '',
                      3: '',
                      4: '',
                      5: '',
                      6: '',
                      7: '',
                      8: '',
                      9: '',}
        self.display = f"{self.board[7]}  | {self.board[8]}  | {self.board[9]}\n" \
                       f"---------\n" \
                       f"{self.board[4]}  | {self.board[5]}  | {self.board[6]}\n" \
                       f"---------\n" \
                       f"{self.board[1]}  | {self.board[2]}  | {self.board[3]}"
        self.win_position = []
        self.player = 0
    def display_board(self, positions):
        print(self.display)
