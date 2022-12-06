from Bangs import Bangs

'''
class thao tác của người chơi gồm:
    đánh X hoặc O vào bảng
    kiểm tra xem vị trí người chơi đánh đã được đánh hay chưa
        nếu chưa thì đánh vào
        nếu đánh rồi thì yêu cầu người dùng nhập lại
'''


class player(Bangs):

    def __init__(self):
        super(player, self).__init__()
        self.vong = 1

    """
     kiểm tra xem vị trí mà người chơi đánh X hoặc O vào đã được đánh chưa
     nếu đã có thì báo lỗi và bắt người chơi nhập lại
     nếu chưa thì đánh vào đo
    """
    def checkplayer(self, vitri=str(), kytu=str()):
        # lấy vị trí mà người chơi muốn nhập
        # -------------------------#
        dong = int(vitri[0:2])
        cot = int(vitri[2:4])
        # -------------------------#

        # nếu tại vị trí mà người chơi muốn đánh vào đã có X hoặc O thì báo lỗi và bắt người chơi nhập lại
        if self.bang[dong - 1][cot - 1] in ["X", "O"]:
            print("vị trí đã được chọn.")
            self.luotchoi(kytu)
        # nếu chưa thì nhập vào nhảy sang lượt tiếp theo
        else:
            self.bang[dong - 1][cot - 1] = kytu
            self.vong += 1

    # người chơi đánh X hoặc O và chuyển cho hàm checkplayer để kiểm tra
    def luotchoi(self, kytu=str()):
        print("Nhập 4 số, hai số đầu là dòng, hai số sau là cột")
        in1 = input("ví dụ: 0101 là dòng 1 cột 1: ")
        # nếu người chơi chưa nhập vào thì báo lỗi và bắt người chơi nhập lại
        if len(in1) == 0:
            print(self.L1)
            self.luotchoi(kytu)
        # nếu người chơi nhập đúng 4 ký tự thì kiểm tra tiếp
        elif len(in1) == 4:
            # nếu nó là số thì kiểm tra tiếp
            if in1.isnumeric():
                # nếu nó giá trị ngoài vùng thì báo lỗi và nhập lại
                if int(in1[0:2]) > self.kichthuoc or int(in1[2:4]) > self.kichthuoc:
                    print(self.L3)
                else:  # nếu đúng thì chuyển qua checkplayer để thực hiện
                    self.checkplayer(in1, kytu)
            else: # nếu người chơi nhập không phải là số thì báo lỗi và bắt người chơi nhập lại
                print("Yêu cầu nhập số có 4 chữ số")
                self.luotchoi(kytu)
        # nếu người chơi nhập quá nhiều số thì báo lỗi và bắt người chơi nhập lại
        elif len(in1) != 0 and len(in1) != 4:
            print(self.L3)
            self.luotchoi(kytu)
        else:  # báo lỗi khác và bắt người chơi nhập lại
            print(self.L2)
            self.luotchoi(kytu)
