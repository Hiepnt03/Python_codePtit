import math


def check_snt(n) :
    if n == 1 : return False
    if n == 2 or n ==3 : return True
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0:
            return False
    return True

def solve(i,n) :
    if i == int(str(i)[::-1]) :
        return False
    if int(str(i)[::-1]) > n :
        return False
    if check_snt(i) == False :
        return False
    if check_snt(int(str(i)[::-1])) == False :
        return False
    return True

t = int(input())
while t>0 :
    result =[]
    t-=1
    n = int(input())
    for i in range(10,int(n)) :
        if solve(i,n) : 
            result.append(i)
    result.sort()
    for i in range(int(len(result)/2)) :
        print(result[0],end=" ")
        print(int(str(result[0])[::-1]),end=" ")
        tmp = int(str(result[0])[::-1])
        result.remove(tmp)
        result.remove(result[0])
    print('')
        