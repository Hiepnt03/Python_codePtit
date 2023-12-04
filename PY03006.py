
n = int(input())
dau_cau = ",.?!:;()-/0123456789"

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
    print(str(key) + " " + str(value))
    
