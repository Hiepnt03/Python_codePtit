import datetime


class GameThu:
    def __init__(self) -> None:
        self.id = str(input())
        self.name = str(input())
        
        time_in = str(input())
        start = int(time_in[0]+time_in[1])*60 + int(time_in[3]+time_in[4]) 
        time_out = str(input())
        end = int(time_out[0] + time_out[1])*60 + int(time_out[3] + time_out[4]) 
        self.time = end-start
        self.time_str = str(self.time//60)+' gio '+str(self.time%60)+' phut'
        
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.time_str

if __name__ == "__main__":
    n = int(input())
    list_gamethu = []
    for i in range(n):
        list_gamethu.append(GameThu())
    list_gamethu = sorted(list_gamethu, key=lambda x : -x.time)
    
    for i in list_gamethu:
        print(i)