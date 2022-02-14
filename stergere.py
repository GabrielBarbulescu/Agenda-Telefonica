
"""Open the file for reading and use file.readlines() to create a list where each element is a line from the file. Use 
the syntax del list[index] with list as the list of lines to delete the element at index. Write the edited list of lines 
to a file to create a new file without the deleted line."""

def delete(x):

    a_file = open("contacte.txt", "r") #deschide in citire
#get list of lines

    lines = a_file.readlines() #imi citeste liniile si le baga intr-un vector ca
    a_file.close()
    del lines[x-1]
#delete lines


    new_file = open("contacte.txt", "w+")
#write to file without line

    for line in lines:
        new_file.write(line)

    new_file.close()

#delete(3)




