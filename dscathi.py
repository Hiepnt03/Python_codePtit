class Exam:
    def __init__(self,ma,date,time,room):
        self.ma = ma
        self.date = date
        self.time = time
        self.room = room
    def __str__(self) :
        return f"{self.ma} {self.date} {self.time} { self.room}"
def get_ma(ma):
    return int(ma[1:])
with open('CATHI.in','r') as file:
    n = int(file.readline().strip())
    a = []
    for i in range(n):
        ma = "C" + str(i+1).zfill(3)
        date = file.readline().strip()
        time = file.readline().strip()
        room = file.readline().strip()
        exam = Exam(ma, date, time, room)
        a.append(exam)
    a.sort(key = lambda exam:(exam.date, exam.time, get_ma(exam.ma)))
    for i in a:
        print(i)
file.close()