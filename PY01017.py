t = int(input())
while t>0 :
    t-=1
    s = str(input())+"!"
    result = ''
    index = 0
    for i in range(len(s)):
        if s[i] != s[index] :
            result = result+str(i-index)+s[index]
            index = i
    print(result)