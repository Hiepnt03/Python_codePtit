import datetime
cost_room = [25,34,50,80]

class KhachHang:
    def __init__(self,id) -> None:
        self.id = id
        
        self.name = str(input())
        
        self.number_room = str(input())
        
        day_in = str(input())
        day_out = str(input())
        self.day_in = datetime.datetime.strptime(day_in, "%d/%m/%Y")
        self.day_out = datetime.datetime.strptime(day_out, "%d/%m/%Y")
        self.day = (self.day_out - self.day_in).days + 1
            
        self.cost_add = int(input())
        
        self.cost_all = cost_room[int(self.number_room[0])-1]*self.day + self.cost_add
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.number_room+' '+str(self.day)+' '+str(self.cost_all)
    
if __name__ == "__main__" :
    n = int(input())
    ds_kh = []
    for i in range(1,n+1):
        if i < 10:
            id = "KH0" + str(i)
        else :
            id = "KH" + str(i)
        ds_kh.append(KhachHang(id))
    
    ds_kh = sorted(ds_kh, key= lambda x : -x.cost_all)
    for i in ds_kh:
        print(i)