import numpy

class matrix1:
    def __init__(self) -> None:
        n,m = [int(x) for x in input().split()]
        self.n = n
        self.m = m
        self.arr = numpy.zeros((n,m))
        for i in range(n):
            self.arr[i] = [int(x) for x in input().split()]
                
    def multi_with_cv(self) -> None:
        matrix = numpy.zeros((self.m,self.n))
        matrix_ans = numpy.zeros((self.n,self.n))
        
        for i in range(self.n):
            for j in range(self.m):
                matrix[j][i] = self.arr[i][j]  
                
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    matrix_ans[i][j] += self.arr[i][k]*matrix[k][j]
                    
        for i in range(self.n):
            for j in range(self.n):
                print(int(matrix_ans[i][j]),end=" ")
            print()
    
if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        MaTrix = matrix1()
        MaTrix.multi_with_cv()