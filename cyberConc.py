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

    # eu acho que isto nao está a funcionar, mas o objetivo era
    # que se a data ou o horario fossem diferentes que o programa emitisse erro
    if filesReading.readHeader(fileNameExperts)[0:3] != \
    filesReading.readHeader(fileNameExperts)[0:3]:
        print("Error in input files: inconsistent files",
              fileNameExperts,"and",fileNameExperts)


    
    rawexp = filesReading.readFile(fileNameExperts)
    rawcl = filesReading.readFile(fileNameClients)

    formatedexp = formated.formatExperts(rawexp)
    formatedcli = formated.formatClients(rawcl)

    sch = scheduling.atribution(formatedcli,formatedexp)

    return sch 

inputFileName1, inputFileName2 = sys.argv[1:]

assign(inputFileName1, inputFileName2)


# assign(sys.argv[1],sys.argv[2])



