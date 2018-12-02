# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

import filesReading
import datetime


def formatExperts(fileName): #final list of experts to itenerate on
    """ Edits a list of lists of experts. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: ranking and pay as int and earnings as float and the experts areas as a tuple """
    explist = filesReading.readFile(fileName)
    for i in explist:
        i[2] = tuple(i[2].replace(";",",").replace("(","").replace(")","").split(","))
        i[4] = int(i[4])
        i[7] = float(i[7])
    return explist

def formatClients(fileName): #final list of clients to itenerate on
    """Edits a list of lists of clients. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: ranking and pay as int """
    cllist = filesReading.readFile(fileName)
    for i in cllist:
        i[4] = int(i[4])
        i[5] = int(i[5])
        i[7] = int(i[7][0])*60 + int(i[7][2:4])
    return cllist





"""
EXPERTS
[0] > nome STR
[1] > cidade STR
[2] > dominios TUPLE
[3] > stars INT
[4] > pay INT
[5] > data DATETIME
[6] > hora DATETIME
[7] > €acumulado INT

CLIENTS
[0] > nome STR
[1] > localidade
[2] > data DATETIME
[3] > hora DATETIME
[4] > pay INT
[5] > estrela INT
[6] > dominio TUPLE
[7] > horas contrato I
"""
