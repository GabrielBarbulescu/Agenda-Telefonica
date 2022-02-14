
def sortare():
    file = open("contacte.txt", "r")
    lines=file.readlines()
    file.close()
    lines.sort()

    new_file=open("contacte.txt","w")
    for line in lines:
        new_file.write(line)
    new_file.close()
