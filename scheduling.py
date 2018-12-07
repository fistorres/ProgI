# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

from operator import itemgetter
import constants

def CompareTimes(timeCli,timeExp):
    """ Compares time and date of clients and Experts and returns the latest(???)
    Requires: timeCli and timeExp as a tuple, first element being date as str
    in YYYY-MM-DD format, and the second element being time as str in "HH:MM" format
    Ensures: tuple in the same format with the latest date
    """
    # ("2019-03-14","14:45") ("2018-03-15","16:36")

    Cli = "".join(timeCli).replace("-","").replace(":","")
    Exp = "".join(timeExp).replace("-","").replace(":","")

    if int(Cli) >= int(Exp):
        
        return timeCli
    else:
        return timeExp



def atributional(clients,experts):
    """
    Runs the attribution function for each of the clients
    in the clients list
    Requires: clients as list
    Requires: experts as list
    Ensures: a list in the following format
    (client name, expert name)
    """
    tup = []
    for i in clients:
        #print(i[0])
        expr = atribution(i,experts)[0]
     #   print(expr)
        tup = tup + [(i,expr),]
        #print(tup)
    return (tup,experts)



#tup[0][0] > nome do cliente
#tup[0][1][0] > nome do expert



def atribution (client, experts):
    """
    Matches a client request with a list of experts
    Requires: cient as a list with the atributes as stated in the project
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


    # tuplo com (data,hora) do client e exp para compara-los
    compareCli = (client[2],client[3])
    compareExp = (compatibleExperts[0][5],compatibleExperts[0][6])
    # compara função
    TimeSchedule = CompareTimes(compareCli,compareExp)

    #update da hora e do dia disponivel
    newTime = constants.timeCalculate(TimeSchedule[0],TimeSchedule[1],client[7])
    print(experts[indi][5],"1",client[2],client[0],experts[indi][0])
    experts[indi][5] = newTime[0] #data
    print(experts[indi][5])
    experts[indi][6] = newTime[1] #hora

    #update do dinheiro acumulado
    experts[indi][7] = experts[indi][7] + (client[4]*client[7])/60
    

    
    return (experts[indi],experts)


