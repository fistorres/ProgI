# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

import os
os.chdir('C:\\Users\\Sofia Torres\\Desktop\\3A1S\\PROGI\\projeto\\tests\\example1')
import datetime

def readExpertsFile(fileName):
    """
    Converts a given file listing experts into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is the first expert and its resume up until the last expert
    """

    fileIn = open(fileName, 'r')
    filetwo = open(fileName, 'r')
    lenfile = len(filetwo.readlines())
    
    outputList = []
    
    i = 0
    while i < 7:
        fileIn.readline()
        i = i+1

    i = 0
    while i < lenfile-7:
        outputList.append(fileIn.readline().replace("*","").replace(" ","").replace("\n", "").split(","))
        i = i+1

    return outputList



def readHeader(fileName):
    """
    Converts a given file listing experts or clients and returns day, time,
    company as variables.
    Requires : fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: day, time and company as str. """

    fileIn = open(fileName, 'r')

    fileIn.readline()
    day = fileIn.readline().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().replace("\n", "")
    fileIn.readline()
    
    return (datetime.date(int(day[0:4]),int(day[5:7]),int(day[8:10])), datetime.time(int(time[0:2]),int(time[3:5])), company)





