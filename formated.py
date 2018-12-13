# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira


import filesReading
import datetime

def takeSpaces(listALL):
    """
    Edits a list of clients or experts and takes all the unnecessary blank spaces
    Requires: listALL as list 
    Ensures: listALL with no unnecessary spaces
    """
    for i in listALL:
        for j in range(1,len(i)):
            i[j] = str(i[j]).replace(" ","")
            
    return listALL


    
def formatExperts(listexp): #final list of experts to itenerate on
    """ Edits a list of lists of experts. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: ranking and pay as int and earnings as float and the experts areas as a tuple """


    listexp = takeSpaces(listexp)
    for i in listexp:
        i[2] = tuple(i[2].replace(";",",").replace("(","").replace(")","").split(","))
        i[3] = int(i[3])
        i[4] = int(i[4])
        i[7] = float(i[7])
        
    return listexp

def formatClients(listcl): #final list of clients to itenerate on
    """Edits a list of lists of clients. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: ranking and pay as int """
    
    listcl = takeSpaces(listcl)        
    for i in listcl:
        i[4] = int(i[4])
        i[5] = int(i[5])
        i[7] = int(i[7][0])*60 + int(i[7][2:4])  #horas em minutos
        
    return listcl

