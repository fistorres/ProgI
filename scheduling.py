# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

from operator import itemgetter

def atribution (client, experts):
    """
    Matches a client request with a list of experts
    Requires: client as a list with the atributes as stated in the project
    Requires: experts a list in which each item is a list of atributes of a specific expert, as stated in the project
    Ensures: a list with the atributes of the expert that best matches the request, according to the project.
    An empty list means a match isn't possible
    """
    compatibleExperts = []
    for i in experts:
        if client[6] in i[2] and i[3] >= client[5] and i[4] <= client[4] and i[1] == client[1]:
            compatibleExperts.append(i)

    compatibleExperts = sorted(compatibleExperts, key=itemgetter(5, 6, 4, 7, 0))
    # sorts the compatibleExperts list by date, then by time, then by pay, then by name

    if len(compatibleExperts) == 0:
        return []
    else:
        return compatibleExperts[0]


