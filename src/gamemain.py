from winner import winner

"""
    class để tổng hợp lại và thêm một số chức năng để thành 1 trò choi
"""


class game(winner):

    def __init__(self):
        super(game, self).__init__()

    # reset lại toàn bộ chương trình
    def reset(self):
        self.game_over = False
        self.vong = 1
        self.th = 0
        board = self.nhap()
        print(board)
        self.taobang()

    # khi có người thắng chương trình hỏi thử có tiếp tục chơi hay không
    def replay(self):
        self.display()
        replay_confirmation = input("Bạn muốn chơi lại? (Y/N)").upper()

        # nếu người chơi nhập khác 1 ký tự thì báo lỗi và nhập lại
        if len(replay_confirmation) != 1:
            print(self.L3)
            self.replay()

        # nếu yes thì tiếp tục chơi lại
        elif replay_confirmation[0] == "Y":
            self.cachchoi()
            self.reset()

        # nếu No thì kết thúc chương trình
        elif replay_confirmation[0] == "N":
            exit()

        else:  # lỗi khác
            print(self.L3)
            self.replay()

    # hàm tổng hợp để hai người chơi chơi với nhau
    def two_player_mode(self):

        while self.game_over.__eq__(False) and self.vong <= (self.kichthuoc ** 2):

            if self.vong % 2 == 1:
                print(f"Player X")
                print(f"Turn: {self.vong}")
                self.display()
                self.luotchoi("X")
                self.checkdong()
                self.checkcot()
                if self.k == 3:
                    self.checkcheochinh()
                    self.checkcheophu()
                elif self.k == 5:
                    self.checkcheochinh5()
                    self.checkcheophu5()

            elif self.vong % 2 == 0:
                print(f"Player O")
                print(f"Turn: {self.vong}")
                self.display()
                self.luotchoi("O")
                self.checkdong()
                self.checkcot()
                if self.k == 3:

                    self.checkcheochinh()
                    self.checkcheophu()
                elif self.k == 5:
                    self.checkcheochinh5()
                    self.checkcheophu5()

        if self.game_over.__eq__(False):
            self.game_over = True
            print("X draws with O")

        self.replay()
        self.two_player_mode()

    def start(self):
        self.cachchoi()
        print(self.nhap())
        self.taobang()
        self.two_player_mode()


a = game()
a.start()
