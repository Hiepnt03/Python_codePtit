import math
class ThiSinh:
    def __init__(self,ma,ten,diem,dt,kv):
        self.ma = format(ma,'02d')
        self.ma = "TS"+self.ma
        self.ten = ten
        self.diem = diem
        self.dt = dt
        self.kv = kv
    def ChuanHoa(self):
        tmp = self.ten.split()
        self.ten = " ".join(tmp).title()
    def getkv(self):
        return self.kv
    def getdt(self):
        return self.dt
    def infor(self):
        kv = self.getkv()
        if kv == 1:
            self.diem += 1.5
        elif kv == 2:
            self.diem +=1
        dt = self.getdt() 
        if dt == "Kinh":
            self.diem +=0
        else:
            self.diem += 1.5
    def out(self):
        print(self.ma + " " + self.ten+ " " + "%.1f"%self.diem,end=" ")
        if self.diem >=20.5:
            print("Do")
        else: print("Truot")
    def getMa(self):
        return self.ma
    def getDiem(self):
        return self.diem

n = int(input())
a = []
for i in range(n):
    t = ThiSinh(i+1,str(input()),float(input()),str(input()),int(input()))
    t.ChuanHoa()
    t.infor()
    a.append(t)
a.sort(key = lambda x : (-x.getDiem(),x.getMa()))
for x in a:
    x.out()