
def find(n) :
    count = 0
    if n%7 == 0:
        print(n)
        return
    while n%7 !=0 and count <= 1000 :
        if len(str(n)) == 1 :
            n = 2*n
        else :
            n = n + int(str(n)[::-1])
        count += 1
    if(n%7 == 0):
        print(n)
    else : print("-1")
t = int(input())
for x in range(t):
    n = int(input())
    find(n)
    