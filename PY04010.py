class ThiSinh:
    def __init__(self,name,birthday,d1,d2,d3) :
        self.name = name
        self.birthday = birthday
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def out(self):
        tong = self.d1 + self.d2 + self.d3
        print(self.name+" "+self.birthday+" "+"%.1f"%tong)

p = ThiSinh(str(input()),str(input()),float(input()),float(input()),float(input()))
p.out()