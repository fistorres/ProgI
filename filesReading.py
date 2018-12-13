# -*- coding: utf-8 -*-

# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira


def readFile(fileName):
    """
    Converts a given file listing experts or clients into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is the first expert or client and its resume up until the last expert
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
        outputList.append(fileIn.readline().replace("*","").replace("\n", "").split(","))
        i = i+1

    return outputList

def readHeader(fileName):
    """
    Converts a given file listing experts or clients and returns day, time,
    company as variables.
    Requires : fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: a tuple of company,day and time as str"""

    fileIn = open(fileName, 'r')

    fileIn.readline()
    day = fileIn.readline().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().replace("\n", "")
    scope = fileIn.readline().replace("\n", "").replace(":","")
    
    return (day,time,company,scope)




