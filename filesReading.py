# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira




import os
os.chdir('C:\\Users\\Sofia Torres\\Desktop\\3A1S\\PROGI\\projeto\\tests\\example1')

def readExpertsFile(fileName):
    """
    Converts a given file listing experts into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is ... <to complete>
    """
    outputList = []
    
    outputList.append(readHeader(fileName))
    
    fileIn = open(fileName, 'r')

    # ... <to complete>

    return outputList



def readHeader(fileName):
    
    # ... <to complete> ... contrato

    fileIn = open(fileName, 'r')

    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()

    #scope = fileIn.readline().strip().replace("\n", "")
    
    scope = {}
    i = 0
    #lenFileIn = sum(1 for line in fileIn)
    #while i < lenFileIn:
    while i < 5:   ## não sei parar este loop. len(fileIn) nao funciona
        listex = fileIn.readline().replace("\n", "").split(",")
        scope[listex[0]] = listex[1:]
        i = i+1
    
    return (day, time, company, scope)




