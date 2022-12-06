"""
class tạo bảng với kích thước nXn và chiếu ra màng hình console
n do người dùng dùng nhập
ví dụ bảng 3X3 có dạng:

+ — + — + — +
|   |   |   |
+ — + — + — +
|   |   |   |
+ — + — + — +
|   |   |   |
+ — + — + — +
"""


class Bangs:

    def __init__(self):
        self.kichthuoc = None  # đây là kích thước n của bảng( do người dùng nhập)

        # --------------------------------------------------------------------#
        self.L1 = "Bạn chưa nhập dữ liệu"
        self.L2 = "Lệnh chưa được ghi nhận"
        self.L3 = "Giá trị bạn vừa nhập nằm ngoài vùng hoạt động"
        # --------------------------------------------------------------------#
        # đây là một số thông báo khi người dùng nhập sai

        self.space = " "  # Ký tự mặc định của bảng khi chưa nhập X hoặc O
        self.bang = []  # dùng 1 list để lưu bảng
        self.k = 0  # biến này dùng để đánh dấu là kiểu chơi caro là tic toc toe hay là caro

    """ dùng để người chơi nhập kiểu muốn chơi là caro hay tic toc toe """
    def cachchoi(self):
        print("1. tic-toc-toe")
        print("2. caro")
        # hứng lỗi nếu người dùng nhập ký tự không phải là số
        try:
            in0 = int(input("Nhập kiểu chơi: "))
            if in0 == 1:
                print(f'cách chơi bạn vừa nhập là toc-toc-toe')
                self.k = 3  # đánh dấu nếu người chơi chơi tic toc toe thì biến đánh dấu là số 3
            elif in0 == 2:
                print(f'cách chơi bạn vừa nhập là caro')
                self.k = 5  # đánh dấu nếu người chơi chơi cờ caro thì biến đánh dấu là số 5
            else:  # nếu đó không phải là số 1 hoặc 2 thì báo lỗi là bắt người dùng nhập lại
                print(self.L3)
                self.cachchoi()
        except:  # nếu người dùng nhập ký tự thì báo lỗi và bắt người dùng nhập lại
            print(self.L3)
            self.cachchoi()

    """ hàm dùng để nhập kích thước n của bảng """
    def nhap(self):
        in1 = input(f'Nhập kích thước bảng từ {self.k}-20:')
        # nếu người dùng chơi tic toc toe thì kích thước bảng từ 3-20
        # nêu người dùng chơi caro thì kích thước bảng từ 5-20
        # vì bảng để chơi caro phải lớn hơn 5 thì mới đủ 5 nước để thắng

        # nếu người dùng chưa nhập thì báo lỗi
        if len(in1) == 0:
            print(self.L1)
            self.nhap()
        elif in1.isnumeric():
            # người dùng nhập kích thước bảng phải trong khoảng từ k đến 20 với k là biên đánh dấu đã nói ở trên
            if self.k <= int(in1) <= 20:
                self.kichthuoc = int(in1)
            # nếu nằm ngoài thì phạm vi trên thì báo lỗi và bắt người dùng nhập lại
            else:
                print(self.L3)
                self.nhap()
        else:  # báo lỗi khác và bắt người dùng nhập lại
            print(self.L2)
            self.nhap()
        return f"kích thước bảng bạn vừa nhập: {self.kichthuoc}x{self.kichthuoc}"

    # hàm tạo bảng dựa trên kích thước n đã nhập ở hàm Nhap()
    def taobang(self):
        self.bang = [self.space] * self.kichthuoc  # lúc này bảng có dạng [' ', ' ', ' '] với n = 3
        for n in range(self.kichthuoc):
            self.bang[n] = [self.space] * self.kichthuoc
            # bảng có dạng [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] (3X3)

    ''' hàm để biểu diễn [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] thành :    + — + — + — +
                                                                                        |   |   |   |
                                                                                        + — + — + — +
                                                                                        |   |   |   |
                                                                                        + — + — + — +
                                                                                        |   |   |   |
                                                                                        + — + — + — + '''
    def display(self):
        # khối lệnh dùng để ghi + — + — + — +  vào một biến
        # -----------------------------------------------#
        display_line = "+"
        print("    ",end="")
        for n in range(self.kichthuoc):
            print("{:>3}".format(n+1),end=" ")
        print()
        for n in range(self.kichthuoc):
            display_line = display_line + " — +"
        # -----------------------------------------------#

        print("   " + display_line)

        # khối lệnh dùng để biến đổi [ ,  ,  ,  ] thành |   |   |   |
        # và sau đó in ra |   |   |   |
        #                 + — + — + — +
        # ------------------------------------------------------------#
        for n in range(self.kichthuoc):
            print("{:>3}".format(n+1),end="")
            display_content = self.bang[n]
            display_content = str(display_content)
            display_content = display_content.replace("[", "| ")  # [' ', ' ', ' '] - > |' ', ' ', ' ']
            display_content = display_content.replace(", ", " | ")  # |' ', ' ', ' '] -> | ' ' | ' ' | ' ']
            display_content = display_content.replace("]", " |")  # | ' ' | ' ' | ' '] -> | ' ' | ' ' | ' '|
            display_content = display_content.replace("'", "")  # | ' ' | ' ' | ' '| -> |   |   |  |
        # ------------------------------------------------------------#
            print(display_content)
            print("   " + display_line)
