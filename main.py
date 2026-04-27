2-m
class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi

    def ovoz(self):
        print("Ovoz chiqaryapti")


class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()
        print(f"Miyov Miyov")

u1 = Hayvon("Mushuk")
u1.ovoz()
