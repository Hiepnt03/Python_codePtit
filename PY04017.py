class VDV:
    def __init__(self) -> None:
        self.name = str(input())
        self.dv = str(input())
        datas = self.dv.split(" ") + self.name.split(" ")
        self.id = ""
        for i in datas :
            self.id += i[0]
        time = str(input())
        self.time = float(time[0]) - 6  + float( float(time[2::])/60 )
        self.vt = float( 120/self.time )
            
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.dv+' '+str("%.0f"%self.vt) + ' Km/h'
    
if __name__ == "__main__" :
    n = int(input())
    lish_VDV = []
    for i in range(n):
        lish_VDV.append(VDV())
    lish_VDV = sorted(lish_VDV, key=lambda x: -x.vt )
    print(*lish_VDV, sep="\n")