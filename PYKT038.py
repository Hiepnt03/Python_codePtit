my_dict = {"000":0,"001":1,"010":2,"011":3,"100":4,"101":5,"110":6,"111":7}
s = str(input())
result = 0

for i in range(3-len(s)%3):
    s = "0" + s

for i in range(int(len(s)/3)):
    for key,value in my_dict.items():
        if key == s[3*i:3*i+3]:
            result = result*10 + value
            break
        
print(result)