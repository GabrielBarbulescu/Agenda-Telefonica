import afisare
import stergere
import sortarelinii
def get_contact_number():

    x = int(input('Nr contact in lista   '))
    afisare.afisare_anume(x)
    print('1.Editare nume\n2.Editare numar')
    option = int(input())
    if option==1:
        editare_nume(x)
    elif option==2:
        editare_numar(x)
    else:
        print('Optiune invalida')
        get_contact_number()
    stergere.delete(x)
    sortarelinii.sortare()
def editare_nume(y):
    file = open("contacte.txt","r")
    lines= file.readlines()
    file.close()
    a = eval(lines[y-1])
    a[0]=input("Nume nou ")
    new_file = open('contacte.txt', 'a')
    new_file.write(str(a)+'\n')


def editare_numar(y):
    file = open("contacte.txt","r")
    lines= file.readlines()
    file.close()
    a = eval(lines[y-1])
    a[1]=int(input('Numar nou  '))
    new_file = open('contacte.txt', 'a')
    new_file.write(str(a)+'\n')
    new_file.close()



