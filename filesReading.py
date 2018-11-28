# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira


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
        outputList.append(fileIn.readline().replace("\n", "").split(","))
        i = i+1

    return outputList


def tupexp(fileName):
    """ Turn string of fields of experts into a tuple
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures : tuple of fields of all the experts in the list """
    explist = readExpertsFile("2019y01m12experts09h00.txt")
    for i in explist:
        i[2] = tuple(i[2].replace(";",",").replace("(","").replace(")","").split(","))
        
        
def readHeader(fileName):
    """
    Converts a given file listing experts and returns day, time,
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
    
    return (day, time, company)

print(readExpertsFile("2019y01m12experts09h00.txt"))





