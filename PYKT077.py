import datetime


class LichThi:
    def __init__(self,id) -> None:
        self.ma_cathi = "T{0:0>3}".format(id)
        datas = [ str(s) for s in input().split(" ") ]
        self.ma_mh = datas[0]
        self.time_thi = datetime.datetime.strptime(datas[1]+' '+datas[2],"%d/%m/%Y %H:%M")  
        self.nhom_thi = datas[3]
    
        
if __name__ == "__main__" :
    n,m = [int(x) for x in input().split()]
    
    mon_hoc = {}
    for i in range(n):
        id = str(input())
        name = str(input())
        mon_hoc[id] = name
        
    list_lichthi = []
    for i in range(m):
        list_lichthi.append(LichThi(i+1))
    
    list_lichthi = sorted(list_lichthi, key=lambda x: (x.time_thi , x.ma_mh))
    
    for i in list_lichthi:
        for key in mon_hoc:
            if i.ma_mh == key:
                print(i.ma_cathi+' '+i.ma_mh+' '+mon_hoc[key]+' '+i.time_thi.strftime("%d/%m/%Y %H:%M")+' '+i.nhom_thi)
                break