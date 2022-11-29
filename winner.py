from player import player

"""
    class có chức năng kiểm tra thử người chơi thắng hay chưa ứng theo từng chế dộ chơi: 
        kiển tra theo dòng
        kiển tra theo cột
        kiển tra theo đường chéo
"""


class winner(player):

    def __init__(self):
        super(winner, self).__init__()
        self.game_over = False  # biến đánh dâu xem có ai thắng chưa
        # self.nguoichoi = 0
        self.winner = ""  # biến lưu người chơi X hay O thắng
        self.th = 0  # biến xem thửu người chơi thắng bao nhiêu đường
        # ---------------------------------#
        self.W1 = "---SINGLE VICTORY---"
        self.W2 = "---DOUBLE VICTORY---"
        self.W3 = "---TRIPLE VICTORY---"
        self.W4 = "---SPIDER VICTORY---"
        # ---------------------------------#
        # thông báo khi người chơi thắng nhiều đường

    """ hàm dùng để thông báongười chơi thắng được bao nhiêu đường """

    def Victory(self):
        if self.th == 1:
            print(self.W1)
        elif self.th == 2:
            print(self.W2)
        elif self.th == 3:
            print(self.W3)
        elif self.th == 4:
            print(self.W4)

    """ 
        hàm dùng để kiểm tra thử
            nếu đúng điều kiện thì người chơi thắng
            hàm này tùy thuộc vào biến mình đã đánh dấu là biến K
            (K là biến để đánh dấu người chơi chơi ở chế độ caro hay tic toc toe đã nói ở class trước ) 
    """

    def kieuchoi(self, check, k):
        if k == 3:  # chế độ tic toc toe
            self.winner = check[0]
            return check.count(check[0]) == len(check) and check[0] != self.space
        elif k == 5:  # chế độ caro
            # print(check, end='\n \n \n')
            for i in range(len(check) - 4):  # kiểm tra vị trí hiện tại và 5 vị trí kể từ sau nó
                # print("oke",end="\n")
                if check[i:i + 5] == ["X", "X", "X", "X", "X"]:  # người chơi X thắng
                    self.winner = "X"
                    return True
                elif check[i:i + 5] == ["O", "O", "O", "O", "O"]:  # người chơi O thắng
                    self.winner = "O"
                    return True
            return False

    """ kiểm tra trên dòng thử ai thắng chưa """

    def checkdong(self):
        check = list()  # tạo một list tạm để lưu 1 dòng trong bảng vào và chuyển cho hàm kieuchoi để kiểm tra
        for t in range(self.kichthuoc):
            for m in range(self.kichthuoc):
                check.append(self.bang[t][m])
            # Khối lệnh dùng để lưu dòng t vào bảng tạm
            if self.kieuchoi(check, self.k):  # nếu người chơi thăng
                self.th += 1  # đếm số đường thắng tăng lên 1 và thông báo ra màng hình
                print(f"{self.winner} ACHIEVES A ROW VICTORY (-)({self.kichthuoc if (self.k == 3) else 5})")
                self.Victory()
                self.game_over = True
                return
            else:  # nếu chưa thắng thì tiếp tục kiểm tra dòng tiếp theo bằng cách làm sạch mảng
                check.clear()

    """ kiểm tra trên cot thử ai thắng chưa """

    def checkcot(self):
        check = list()
        for q in range(self.kichthuoc):
            for m in range(self.kichthuoc):
                check.append(self.bang[m][q])
            if self.kieuchoi(check, self.k):
                self.th += 1
                print(f"{self.winner} ACHIEVES A COLUMN VICTORY (|)({self.kichthuoc if (self.k == 3) else 5})")
                self.Victory()
                self.game_over = True
                return
            else:
                check.clear()

    """ kiểm tra trên đường chéo phụ thử ai thắng chưa """

    def checkcheophu(self):
        check = list()
        for n in range(self.kichthuoc):
            check.append(self.bang[n][-(n + 1)])
        if self.kieuchoi(check, self.k):
            self.th += 1
            print(f"{self.winner} ACHIEVES A BACKSLASH VICTORY (/)({self.kichthuoc if (self.k == 3) else 5})")
            self.Victory()
            self.game_over = True
        else:
            check.clear()

    """ kiểm tra trên dòng thử ai thắng chưa """

    def checkcheochinh(self):
        check = list()
        for n in range(self.kichthuoc):
            check.append(self.bang[n][n])
        if self.kieuchoi(check, self.k):
            self.th += 1
            print(f"{self.winner} ACHIEVES A SLASH VICTORY (\\)({self.kichthuoc if (self.k == 3) else 5})")
            self.Victory()
            self.game_over = True
        else:
            check.clear()

    def checkcheophu5(self):
        check = list()
        for m in range(4, self.kichthuoc):
            for n in range(m + 1):
                check.append(self.bang[n][m - n])
            if self.kieuchoi(check, self.k):
                self.th += 1
                print(f"{self.winner} ACHIEVES A BACKSLASH VICTORY (/)({self.kichthuoc if (self.k == 3) else 5})")
                self.Victory()
                self.game_over = True
                return
            else:
                check.clear()

        for m in range(1, self.kichthuoc - 4):
            for n in range(self.kichthuoc - m, 0, -1):
                check.append(self.bang[self.kichthuoc - n][n + m - 1])
            if self.kieuchoi(check, self.k):
                self.th += 1
                print(f"{self.winner} ACHIEVES A BACKSLASH VICTORY (/)({self.kichthuoc if (self.k == 3) else 5})")
                self.Victory()
                self.game_over = True
                return
            else:
                check.clear()

    def checkcheochinh5(self):
        check = list()
        for m in range(0, self.kichthuoc -4):
            for n in range(self.kichthuoc, m, -1):
                check.append(self.bang[n-1][n-m-1])
            if self.kieuchoi(check, self.k):
                self.th += 1
                print(f"{self.winner} ACHIEVES A SLASH VICTORY (\\)({self.kichthuoc if (self.k == 3) else 5})")
                self.Victory()
                self.game_over = True
                return
            else:
                check.clear()

        for m in range(1, self.kichthuoc - 4):
            for n in range(0, self.kichthuoc-m):
                check.append(self.bang[n][n+m])
            if self.kieuchoi(check, self.k):
                self.th += 1
                print(f"{self.winner} ACHIEVES A SLASH VICTORY (\\)({self.kichthuoc if (self.k == 3) else 5})")
                self.Victory()
                self.game_over = True
                return
            else:
                check.clear()

