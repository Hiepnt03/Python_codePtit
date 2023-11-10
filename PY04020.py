class HoaDon:
    def __init__(self) -> None:
        self.id = str(input())
        self.name = str(input())
        self.number_buy = int(input())
        self.cost = int(input())
        self.sale = int(input())
        self.total = self.PhaiTra()
        
    def PhaiTra(self) -> int:
        return self.cost*self.number_buy-self.sale
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+str(self.number_buy)+' '+str(self.cost)+' '+str(self.sale)+' '+str(self.total)
    
if __name__ == '__main__':
    n = int(input())
    ds_hd = []
    for i in range(n):
        ds_hd.append(HoaDon())
    ds_hd = sorted(ds_hd, key=lambda x : -x.total)
    print(*ds_hd, sep="\n")