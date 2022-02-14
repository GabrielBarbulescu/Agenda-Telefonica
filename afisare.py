
def afisare_lista():
        file = open("contacte.txt")
        lines = file.readlines()
        a=0
        for line in lines:
            b=eval(line)
            print(a+1,".",b[0],"->",b[1])
            a+=1



def afisare_anume(x):
    file = open("contacte.txt")
    line = file.readlines()
    b=eval(line[x-1])
    print(b[0],"-->",b[1])

#afisare_anume(2)