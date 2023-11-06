
def add_phay(s) :
    tmp = 0
    result = ""
    for i in range(len(s)-1,-1,-1) :
        if tmp == 3 :
            result += ','
            tmp = 0
        result += s[i]
        tmp += 1
    return result   
        

s = str(input())
result = add_phay(s)
result = result[::-1] # đảo ngươcj chuỗi result
print(result)