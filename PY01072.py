n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
my_list = sorted(list(set(arr)))
n = len(my_list)
tmp= []
for i in range(1,k+1):
    tmp.append(i)
    
def xuat(tmp,my_list):
    for i in range(k):
        print(my_list[tmp[i]-1],end=" ")
    print()

def SinhToHop(k,n,tmp):
    xuat(tmp,my_list)
    ok = 0
    for i in range(k):
        if tmp[i] == (n-k+i+1):
            ok += 1
    if ok == k:
        return
    for i in range(k-1,-1,-1):
        if tmp[i] < (n-k+i+1) :
            tmp[i] +=1
            for j in range(i+1,k):
                tmp[j] = tmp[j-1]+1
            break
    SinhToHop(k,n,tmp)
if __name__ == '__main__':
    if n<k:
        print(-1)
    else:
        SinhToHop(k,n,tmp)
    
