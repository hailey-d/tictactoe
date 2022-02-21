
class Game():
    def __init__(self):
        super().__init__()
        self.board = {1:'',
                      2: '',
                      3: '',
                      4: '',
                      5: '',
                      6: '',
                      7: '',
                      8: '',
                      9: '',}
        self.win_position = []
        self.player = 0
        self.display = ''
    def update_board(self, position):
        if self.board[position] == '':
            if self.player % 2 == 0:
                self.board[position] = 'X'
            else:
                self.board[position] = 'O'
            self.player +=1
        else:
            print("Pick another square")
        self.display = f"{self.board[7]} | {self.board[8]} | {self.board[9]}\n" \
                       f"---------\n" \
                       f"{self.board[4]} | {self.board[5]} | {self.board[6]}\n" \
                       f"---------\n" \
                       f"{self.board[1]} | {self.board[2]} | {self.board[3]}"
        print(self.display)
        return self.board

    def check_win(self):
        is_over = False
        def all_same(items):
            return all(x == items[0] for x in items)

        col_1 = [self.board[1], self.board[4], self.board[7]]
        col_2 = [self.board[2], self.board[5], self.board[8]]
        col_3 = [self.board[3], self.board[6], self.board[9]]
        row_1 = [self.board[1], self.board[2], self.board[3]]
        row_2 = [self.board[4], self.board[5], self.board[6]]
        row_3 = [self.board[7], self.board[8], self.board[9]]
        diag_1 = [self.board[7], self.board[5], self.board[3]]
        diag_2 = [self.board[1], self.board[5], self.board[9]]
        sol_list = [col_1, col_2, col_3,
                    row_1, row_2, row_3,
                    diag_1, diag_2]
        for item in sol_list:
            if all_same(item):
                if 'X' in item:
                    is_over = True
                    self.win_position = item
                    break
                elif 'O' in item:
                    is_over = True
                    self.win_position = item
                    break
                else:
                    is_over = False
        return is_over

    def who_won(self):
        if 'X' in self.win_position:
            print("Player 1 (X) Wins!")
        else:
            print("Player 2 (O) Wins")


