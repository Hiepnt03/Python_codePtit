t = int(input())
while t>0 :
    t-=1
    s = str(input())
    result = ''
    for i in range(len(s)) :
        if s[i]>="1" and s[i]<='9' :
            for x in range(int(s[i])) :
                result += s[i-1]
    print(result)