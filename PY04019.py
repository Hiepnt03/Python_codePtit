class NhanVien:
    def __init__(self,id) -> None:
        self.id = id
        self.name = str(input())
        
        score_lt = float(input())
        if score_lt > 10:
            score_lt = score_lt/10
        
        score_th = float(input())
        if score_th > 10:
            score_th = score_th/10
            
        self.score = (score_lt+score_th)/2
        
        if self.score > 9.5 :
            self.type = "XUAT SAC"
        elif self.score >=8:
            self.type = "DAT"
        elif self.score >= 5:
            self.type = 'CAN NHAC'
        else :
            self.type = 'TRUOT'
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+"%.2f"%self.score+' '+self.type
    
if __name__ == '__main__':
    n = int(input())
    list_nv = []
    for i in range(1,n+1):
        id = 'TS0' + str(i)
        list_nv.append(NhanVien(id))
    list_nv = sorted(list_nv, key= lambda x : - x.score)
    for i in list_nv:
        print(i)
    