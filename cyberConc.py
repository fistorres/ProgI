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
    rawexp = filesReading.readFile(fileNameExperts)
    rawcl = filesReading.readFile(fileNameClients)

    formatedexp = formated.formatExperts(rawexp)
    formatedcli = formated.formatClients(rawcl)

    sch = scheduling.atribution(formatedcli,formatedexp)

    return sch ## Eu estou a por aqui tudo até oque funciona. Já experimentei correr na command line e acho que está bem :P
    ## se quiseres correr na cmd line escreve > cyberConc.py inputFileName1 inputFileName2





inputFileName1, inputFileName2 = sys.argv[1:]

assign(inputFileName1, inputFileName2)


# assign(sys.argv[1],sys.argv[2])


