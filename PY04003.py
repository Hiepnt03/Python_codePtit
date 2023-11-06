from decimal import Decimal
import math


class PhanSo1:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
        
    def RutGon(self):
        GCD = math.gcd(self.tu,self.mau)
        self.tu = int(self.tu/GCD)
        self.mau = int(self.mau/GCD)
        
    def out(self):
        print( self.tu, end="/" )
        print( self.mau )
        
if __name__ == '__main__':
    arr = input().split()
    p = PhanSo1(int(arr[0]),int(arr[1]))
    p.RutGon()
    p.out()