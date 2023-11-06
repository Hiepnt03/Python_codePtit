class SinhVien:
    def __init__(self) -> None:
        self.id = str(input())
        self.name = str(input())
        self.lop = str(input())
        self.diem = ""
    def GetId(self) -> None:
        return str(self.id)
    def SetDiem(self,s) -> None:
        diem = int(10)
        for i in s:
            if i == 'v':
                diem -=2
            if i == 'm':
                diem -=1
        if int(diem) <= 0: self.diem = "0 KDDK"
        else : self.diem = str(diem)
 
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.lop+' '+self.diem
    
if __name__ == '__main__':
    n = int(input())
    
    list_sv = []
    for i in range(n):
        list_sv.append(SinhVien())
        
    id_sv = []
    data = []
    for i in range(n):
        arr = [str(s) for s in input().split()]
        id_sv.append(arr[0])
        data.append(arr[1])
        
    for i in range(n):
        for j in list_sv:
            if id_sv[i] == j.GetId() :
                j.SetDiem(data[i])
                break
            
    for i in list_sv:
        print(i)
