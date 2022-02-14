import adaugacontact
import afisare
import editare
import stergere


def meniu():
    afisare.afisare_lista()
    print("-----------------\n  1.Add contact \n  2.Del contact\n  3.Edit contact\n  4.Exit")
meniu()
o = int(input('Option  '))
while True:
    if o==1:
        adaugacontact.adauga()

        meniu()
    elif o==2:
        s=int(input("Line number of the contact"))
        stergere.delete(s)
        meniu()
    elif o==3:
        editare.get_contact_number()
        meniu()
    elif o==4:
        break
    else:
        print("Invalid option")
    o = int(input('Option  '))


