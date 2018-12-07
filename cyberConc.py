# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

import sys
import filesReading
import formated
import constants
import filesWriting
import scheduling
import constants


def checkError(fileNameExperts, fileNameClients):
    """ """

    # Testar se os cabeçalhos são correspondentes entre Client e Expert
    headExp = filesReading.readHeader(fileNameExperts) 
    headCli = filesReading.readHeader(fileNameClients)
    if headCli[0:3] != headExp[0:3]:
        print("Error in input files: inconsistent files",
              fileNameExperts,"and",fileNameExperts)
        return False

    # testar se cabeçalho é igual ao nome do ficheiro
    # ex:2019y03m20clients12h30.txt = ('2019-02-20', '12:30', 'iCageDoree', 'Clients')   <<< deve dar erro neste exemplo
    for i in sys.argv[1:]:
        if i.replace("y","-").replace("m","-")[0:10] != (filesReading.readHeader(i))[0] or \
           str(i[10:17]) != lower.filesReading.readHeader(i)[3] or \
           str(i.replace("h",":")[17:22]) != filesReading.readHeader(i)[1]:
           print("Error in input file: inconsistent name and header in file", i)
           return False
        else:
            print("Yupi")
            return True


def assign(fileNameExperts, fileNameClients):
    """
    Assign given experts given to given clients.
    Requires: fileNameExperts, fileNameClients are str, with the names
    of the files representing the list of experts and clients, respectively,
    following the format indicated in the project.
    Ensures: Two output files, respectively, with the listing of schedules
    tasks and the updated listing of experts, following the format
    and naming convention indicated in the project.
    """

    # Reads the files into the variables
    rawexp = filesReading.readFile(fileNameExperts)
    rawcl = filesReading.readFile(fileNameClients)

    formatedexp = formated.formatExperts(rawexp)
    formatedcli = formated.formatClients(rawcl)

    tupleClientExpert = scheduling.atributional(formatedcli,formatedexp)

    # Calculates the timestamp of the new file, 30 min
    # after the input file
    timestamp = constants.timeCalculate(
        filesReading.readHeader(fileNameExperts)[0],
        filesReading.readHeader(fileNameExperts)[1],
        30  # time increment from input file
    )

    # Creates a new file for the schedule
    Schedule = filesWriting.newFile(
        timestamp[0],
        timestamp[1], 
        'schedule',
        filesReading.readHeader(fileNameClients)[2]
    )

    for i in tupleClientExpert:
        filesWriting.addSchedule(Schedule, i)



#  start of program:

inputExperts, inputClients = sys.argv[1:]

if checkError(inputExperts, inputClients):
    assign(inputExperts, inputClients)













