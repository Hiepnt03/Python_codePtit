number = "0123456789"
def check(s):
    for i in s:
        if i not in number:
            return True
    if abs(int(s)) > 2147483647:
        return True
    return False
result = []
with open('DATA.in','r') as file:
    for line in file:
        arr = line.split()
        for i in range(len(arr)):
            if check(arr[i]):
                result.append(arr[i])
result.sort()
for i in result:
    print(i,end=" ")
