class Film:
    def __init__(self,id) -> None:
        self.id = "P{0:0>3}".format(id) 
        self.id_type = str(input())
        date = str(input())
        self.day = int(date[0:2])
        self.month = int(date[3:5])
        self.year = int(date[6:10])
        self.date = "{0:0>2}".format(self.day) + '/' + "{0:0>2}".format(self.month)+'/'+str(self.year)
        self.name = str(input())
        self.episode_number_film = int(input())
        
if __name__ == '__main__' :
    
    n,m = [int(x) for x in input().split()]
    
    my_dict = {}
    for i in range(n):
        id = "TL{0:0>3}".format(i+1) 
        name = str(input())
        my_dict[id] = name
        
    my_film = []
    for i in range(m):
        my_film.append(Film(i+1))
    
    my_film = sorted(my_film, key=lambda x : (x.year, x.month , x.day ,x.name, -x.episode_number_film ) )
    
    for i in my_film:
        for key in my_dict:
            if i.id_type == key:
                print(i.id+' '+my_dict[key]+' '+i.date+' '+i.name+' '+str(i.episode_number_film))
                break