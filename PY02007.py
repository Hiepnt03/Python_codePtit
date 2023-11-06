arr = []
count = 0
result = set()
while count < 10 :
    arr = [ int(x) for x in input().split()]
    count += len(arr)
    for i in arr :
        result.add(i%42)
print(len(result))