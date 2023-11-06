with open('CONTACT.in','r') as file:
    lines = file.readlines()
    a= []
    for line in lines:
        a.append(line.strip().lower())
    l = sorted(set(a))
    for i in l:
        print(i)