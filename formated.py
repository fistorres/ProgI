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
    Ensures: listALL as list with no unnecessary spaces
    """
    # range starts at 1 because we don't want to eliminate
    # the spaces between the person's name
    for i in listALL:
        for j in range(1, len(i)):
            i[j] = str(i[j]).replace(" ", "")
            
    return listALL


def formatExperts(listexp): # final list of experts to iterate on
    """
    Edits a list of lists of experts. Changes elements from str to another type better suited.
    Requires: listexp as a list of experts,
    Ensures: a list with: skills as tuple, star rating and hourly pay as int, earnings as float
    """

    listexp = takeSpaces(listexp)
    for i in listexp:
        i[2] = tuple(i[2].replace(";", ",").replace("(", "").replace(")", "").split(","))  # skills as tuple
        i[3] = int(i[3])  # star rating as int
        i[4] = int(i[4])  # hourly pay as int
        i[7] = float(i[7])  # earnings as float
        
    return listexp


def formatClients(listcl):  # final list of clients to itenerate on
    """
    Edits a list of lists of clients. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: ranking and pay as int
    """
    
    listcl = takeSpaces(listcl)        
    for i in listcl:
        i[4] = int(i[4])
        i[5] = int(i[5])
        i[7] = int(i[7][0])*hourMinutes + int(i[7][2:4])  # hours in minutes
        
    return listcl

