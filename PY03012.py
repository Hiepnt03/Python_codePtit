# class SinhVien:
#     def __init__(self) -> None:
#         self.full_name = str(input())
#         self.name = self.full_name.split()[2]
#         num = [int(x) for x in input().split()]
#         self.number_ac = num[0]
#         self.number_submit = num[1]
        
#     def __str__(self) -> str:
#         return self.full_name+' '+str(self.number_ac)+' '+str(self.number_submit)

# if __name__ == "__main__":
#     n = int(input()) 
#     list_sv = []
#     while n>0:
#         n-=1   
#         list_sv.append(SinhVien())
#     list_sv = sorted(list_sv, key=lambda x : (-x.number_ac,x.number_submit,x.name))
#     for i in list_sv :
#         print(i)

import functools

class SV :
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit

def cmp(a, b) :
    if a.ac < b.ac : return 1
    elif a.ac == b.ac :
        if a.submit > b.submit : return 1
        elif a.submit == b.submit :
            if a.name > b.name : return 1
            else : return -1
        else : return -1
    else : return -1

n = int(input())
a = []
for i in range(n) :
    name = input()
    ac, submit = [int(x) for x in input().split()]
    a.append(SV(name, ac, submit))
a = sorted(a, key = functools.cmp_to_key(cmp))
for i in a :
    print(i.name, i.ac, i.submit)
