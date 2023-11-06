class Rectangle:
    def __init__(self,cd,cr,color) :
        self.cd = cd
        self.cr = cr
        self.color = color[0:1:].upper() + color[1::].lower()
        
    def perimeter(self):
        return self.cd * self.cr
    def area(self):
        return 2*(self.cd+self.cr)
    
        
        
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))