a = [0,10,10,10,12,12,12,12,12,14,14,14,14,14,14,14,20]
b = [0,10,10,10,11,11,11,11,11,13,13,13,13,13,13,13,16]
c = [0,9,9,9,10,10,10,10,10,12,12,12,12,12,12,12,14]
d = [0,8,8,8,9,9,9,9,9,11,11,11,11,11,11,11,13]
class NhanVien:
    def __init__(self,ma,ten,luongcb,ngayc,heso) :
        self.ma = ma
        self.ten = ten
        self.luongcb = luongcb
        self.ngayc = ngayc
        self.heso = heso
def getloai(ma):
    return ma[0]
def getnam(ma):
    return int(ma[1]) * 10 + int(ma[2])
def getpb(ma):
    return ma[3:]
m=[]
phongban={}
for t in range(int(input())):
    pb = str(input())
    phongban[pb[:2]] = pb[3:]
for t in range(int(input())):
    ma = input()
    ten = input()
    luongcb = int(input())
    ngayc = int(input())
    if getloai(ma) == "A":
        if getnam(ma) > 15:
            heso = a[16]
        else: heso = a[getnam(ma)]
    elif getloai(ma) == "B":
        if getnam(ma) > 15:
            heso = b[16]
        else: heso = b[getnam(ma)]
    elif getloai(ma) == "C":
        if getnam(ma) > 15:
            heso = c[16]
        else: heso = c[getnam(ma)]
    else :
        if getnam(ma) > 15:
            heso = d[16]
        else: heso = d[getnam(ma)]
    m.append(NhanVien(ma,ten,luongcb,ngayc,heso))
for i in m:
    print(i.ma,i.ten,phongban[getpb(i.ma)],i.heso*i.luongcb*i.ngayc*1000)