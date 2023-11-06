t = int(input())
while t>0 :
    t -=1
    s = str(input())
    result = []
    tmp =''
    for i in s :
        if i>="0" and i<="9" :
            tmp = tmp + i
        else :
            if tmp != '' :
                result.append(int(tmp))
                tmp = ''
    result.sort()
    print(result[0])