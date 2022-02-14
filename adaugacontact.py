import sortarelinii
import afisare

def adauga():
    fw = open('contacte.txt', 'a')
    print("Nume:")
    nume = input()
    print("Numar")
    numar =  int(input())
    contact = [nume ,numar]
    fw.write(str(contact ) +'\n')
    fw.close()
    print("Contact adaugat\n")
    sortarelinii.sortare()
