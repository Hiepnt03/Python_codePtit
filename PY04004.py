import math

class PhanSo2:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
        
    def RutGon(self):
        GCD = math.gcd(self.tu,self.mau)
        self.tu = int(self.tu/GCD)
        self.mau = int(self.mau/GCD)     
        
    def add(self,p) :
        a = self.tu * p.mau + self.mau * p.tu
        b = self.mau * p.mau
        self.tu = a
        self.mau = b
        self.RutGon() 
        self.out()
    
    def out(self):
        print( self.tu, "/",self.mau,sep="" )
   
        
if __name__ == '__main__':
    arr = input().split()
    p1 = PhanSo2(int(arr[0]),int(arr[1]))
    p2 = PhanSo2(int(arr[2]),int(arr[3]))
    p1.add(p2)