# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

import filesReading
import datetime


def formatExperts(fileName): #final list of experts to itenerate on
    """ Edits a list of lists of experts. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: date and time as datetime format,ranking and pay as int and earnings as float and the experts areas to a tuple """
    explist = filesReading.readFile(fileName)
    for i in explist:
        i[2] = tuple(i[2].replace(";",",").replace("(","").replace(")","").split(","))
        i[5] = datetime.date(int(i[5][0:4]),int(i[5][5:7]),int(i[5][8:10]))
        i[6] = datetime.time(int(i[6][0:2]),int(i[6][3:5]))
        i[3] = int(i[3])
        i[4] = int(i[4])
        i[7] = float(i[7])
    return explist

def formatClients(fileName): #final list of clients to itenerate on
    """Edits a list of lists of clients. Changes elements from str to another type better suited.
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: date and time as datetime format,ranking and pay as int """
    cllist = filesReading.readFile(fileName)
    for i in cllist:
        i[2] = datetime.date( int (i[2][0:4]) , int(i[2][5:7]) , int(i[2][8:10]) )
        i[3] = datetime.time(int(i[3][0:2]),int(i[3][3:5]))
        i[7] = datetime.time(int(i[7][0:1]),int(i[7][2:4]))
        i[4] = int(i[4])
        i[5] = int(i[5])
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
