import math


class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, k) :
        return math.sqrt((self.x - k.x) ** 2 + (self.y - k.y) ** 2)
        
class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def cnt(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if a+b<=c or a+c<=b or b+c<=a:
            print("INVALID")
        else : print( "%.3f"%(a+b+c) )

if __name__ == '__main__':
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        triagle.cnt()
        i += 6
        