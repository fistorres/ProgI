# -*- coding: utf-8 -*-

# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

from constants import hourMinutes

def takeSpaces(listALL):
    """
    Edits a list of clients or experts and takes all the unnecessary blank spaces
    Requires: listALL as list 
    Ensures: listALL with no unnecessary spaces
    """
    # range starts at 1 because we don't want to eliminate
    # the spaces between the person's name
    for i in listALL:
        for j in range(1,len(i)):
            i[j] = str(i[j]).replace(" ","")
            
    return listALL


def formatExperts(listexp): # final list of experts to iterate on
    """
    Edits a list of lists of experts. Changes elements from str to another type better suited.
    Requires: listexp as a list of experts.
    Ensures: a list with: skills as tuple, star ratint and hourly pay as int
    and total amout earned as float.
    """

    listexp = takeSpaces(listexp)
    for i in listexp:
        i[2] = tuple(i[2].replace(";",",").replace("(","").replace(")","").split(",")) #skills
        i[3] = int(i[3]) #star rating
        i[4] = int(i[4]) #hourly pay
        i[7] = float(i[7]) #total amount earned
        
    return listexp

def formatClients(listcl): # final list of clients to itenerate on
    """
    Edits a list of lists of clients. Changes elements from str to another type
    better suited.
    Requires: listcl as a list of clients.
    Ensures: a list with: star ratint and hourly pay as int
    and work duration as int (in minutes).
    """
    
    listcl = takeSpaces(listcl)        
    for i in listcl:
        i[4] = int(i[4]) #hourly pay
        i[5] = int(i[5]) #star rating
        i[7] = int(i[7][0])*hourMinutes + int(i[7][2:4])  #work duration (in minutes)
        
    return listcl

