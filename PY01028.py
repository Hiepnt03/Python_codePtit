s= str(input()) + ' '
tmp = ""
for i in s :
    if i == ' ' :
        print(tmp)
        tmp = ''
    else :
        tmp += i

