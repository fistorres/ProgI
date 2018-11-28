import filesReading
import datetime

def tupexp(fileName):
    """ Turn string of fields of experts into a tuple
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures : tuple of fields of all the experts in the list """
    explist = filesReading.readExpertsFile(fileName)
    for i in explist:
        i[2] = tuple(i[2].replace(";",",").replace("(","").replace(")","").split(","))
    return explist


def formatdate(fileName):
    """ Turn date and time from str to datetime format
    Requires: fileName is str, the name of a .txt file listing experts,
    Ensures: date and time as datetime format """
    explist = tupexp(fileName)
    for i in explist:
        i[5] = datetime.date(int(i[5][1:5]),int(i[5][6:8]),int(i[5][9:11]))
        i[6] = datetime.time(int(i[6][1:3]),int(i[6][4:6]))
    return explist
  
    
    
