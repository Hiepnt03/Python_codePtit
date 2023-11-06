def sum(s):
    sum= 0
    for i in range(0,len(s),2):
        sum += int(s[i])
    return sum

def multiplication(s):
    mutipl,count,count0 = 1,0,0
    for i in range(1,len(s),2):
        if s[i] != '0':
            mutipl *= int(s[i])
        else:
            count0 +=1
        count+=1
    if count == count0:
        return 0
    else :
        return mutipl
    
    
t = int(input())
while t>0:
    t-=1
    s = str(input())
    print(sum(s),end=" ")
    print(multiplication(s))