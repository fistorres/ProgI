# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

from operator import itemgetter
import constants


def atributional(clients,experts):
    """ """
    tup = []
    for i in clients:
        tup = tup + [(i[0],atributionuni(i,experts)[0]),]
    return tup

def atributionuni (client, experts):
    """
    Matches a client request with a list of experts
    Requires: client as a list with the atributes as stated in the project
    Requires: experts a list in which each item is a list of atributes of a specific expert,
    as stated in the project
    Ensures: a list with the atributes of the expert that best matches the request,
    according to the project.
    An empty list means a match isn't possible
    """
    compatibleExperts = []
    for i in experts:
        if client[6] in i[2] and i[3] >= client[5] and \
           i[4] <= client[4] and i[1] == client[1]:
            compatibleExperts.append(i)

    compatibleExperts = sorted(compatibleExperts, key=itemgetter(5, 6, 4, 7, 0))
    # sorts the compatibleExperts list by date, then by time, then by pay, then by name

    # buscar indice do expert sorteado
    indi = experts.index(compatibleExperts[0])
    print(indi,client[0])
          
    #update da hora e do dia disponivel
    experts[indi][5] = constants.timeCalculate(experts[indi][5],experts[indi][6],client[7])[0]
    experts[indi][6] = constants.timeCalculate(experts[indi][5],experts[indi][6],client[7])[1]
    #print(experts[indi][5],experts[indi][6])

    #update do dinheiro acumulado
    experts[indi][7] = experts[indi][7] + client[4]*client[7]
    #print(experts[indi])
    

    if len(compatibleExperts) == 0:
        return ([],experts)

    return (compatibleExperts[0],experts)





