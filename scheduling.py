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
        #print(i[0])
        expr = atributionuni(i,experts)[0]
        tup = tup + [(i[0],expr),]
        #print(tup)
    return tup

#tup[0][0] > nome do cliente
#tup[0][1][0] > nome do expert



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

    if len(compatibleExperts) == 0:
        return (["declined",],experts)
    
    # buscar indice do expert sorteado
    indi = experts.index(compatibleExperts[0])
    #ACHO QUE PRECISAMOS DE UMA FUNÇÃO PARA VERIFICAR QUAL HORA É A MENOR
    #PARA DEPOIS FAZER UPDATE NO SCHEDULE
          
    #update da hora e do dia disponivel
    newTime = constants.timeCalculate(experts[indi][5],experts[indi][6],client[7])
    experts[indi][5] = newTime[0]
    experts[indi][6] = newTime[1]

    #update do dinheiro acumulado
    experts[indi][7] = experts[indi][7] + client[4]*client[7]
    

    
    return (compatibleExperts[0],experts)




