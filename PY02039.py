n = int(input())
arr = []
TongTren, TongDuoi,index = [],[],0
for i in range(n):
    hang = [int(x) for x in input().split()]
    arr.append(hang)
k = int(input())
for hang in arr:
    for i in range(n):
        if i > index:
            TongTren.append(hang[i])
        if i < index:
            TongDuoi.append(hang[i])
    index +=1
result = abs(sum(TongTren) - sum(TongDuoi))
if result > k:
    print("NO\n" + str(result))
else:
    print("YES\n" + str(result))