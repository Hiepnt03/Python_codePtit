import math

def check_snt(n) :
    if n == 1 : return False
    if n == 2 or n ==3 : return True
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0:
            return False
    return True

def check_number_snt(n) :
    s = str(n)
    for i in s :
        if i!= "2" and i!= "3" and i!= "5" and i!= "7" :
            return False
    return True
    
def solve(n):
    if check_snt(n) == False :
        return False
    s = str(n)
    sum = 0
    for i in s :
        sum += int(i)
    if check_snt(sum) == False:
        return False
    if check_snt(int(s[::-1])) == False :
        return False
    if check_number_snt(n) == False :
        return False
    return True

t = int(input())
while t>0:
    t -=1
    n = int(input())
    if solve(n) == True : print("Yes")
    else : print("No")