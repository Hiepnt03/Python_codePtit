
n,k = [int(x) for x in input().split()]
dau_cau = ",.?!:;()-/"

my_dict = dict()
for i in range(n):
    s = str(input()).lower()
    # Thay lần lượt các dấu câu bằng dấu cách 
    for dau in dau_cau:
        s = s.replace(dau," ")
    data = s.split()
    for tu in data:
        if tu in my_dict:
            my_dict[tu] +=1
        else:
            my_dict[tu] = 1
my_dict = sorted(my_dict.items(), key=lambda x : (-x[1],x[0]))
for key,value in my_dict:
    if value < k :
        break
    else:
        print(str(key) + " " + str(value))
    
