ma_uu_tien = { '1':2.0 , '2':1.5, '3':1.0 , '4':0 }
mon_hoc = { 'A':"TOAN" , 'B':"LY" , 'C':"HOA" }

class GiaoVien:
    def __init__(self,id) -> None:
        self.id = 'GV{0:0>2}'.format(id)
        self.name = str(input())
        self.ma_xt = str(input())
        self.score_sum( float( input() ) , float( input() ) )
    
    def score_sum(self,score_th, score_cm) -> None:
        sum = score_th * 2 + score_cm
        for key in ma_uu_tien :
            if key == self.ma_xt[1]:
                sum += ma_uu_tien[key]
                break
        self.sum = sum
        
        for key in mon_hoc :
            if key == self.ma_xt[0]:
                self.subject =  mon_hoc[key]
                break
        
        if self.sum <18 : self.type = "LOAI"
        else : self.type = "TRUNG TUYEN"
        
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.subject+' '+str( "%.1f"%self.sum )+' '+self.type;    
    
if __name__ == "__main__" :
    n = int(input())
    list_gv = []
    for i in range(n):
        list_gv.append(GiaoVien(i+1))
    list_gv = sorted(list_gv, key=lambda x : -x.sum)
    print(*list_gv, sep="\n")