def thaphn(n,A,C,B) :
    if n == 1 :
        print(A,"->",C)
        return
    thaphn(n-1,A,B,C)
    thaphn(1,A,C,B)
    thaphn(n-1,B,C,A)
    
n = int(input())
thaphn(n,'A','C','B')

