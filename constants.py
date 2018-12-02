# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

def formatNumber(x):
    """
    Converts an int to a str and adds a 0 before if < 10
    Requires: x as int < 100
    Ensures: an str '0x' if < 10, 'x' otherwise, assuring an output of 2 chars
    """

    if x < 10:
        return '0' + str(x)
    else:
        return str(x)


def timeCalculate (inDate, inTime, increment):
    """
    Receives a time and date of origin and increments a certain amount of minutes,
    within the working hours of 8:00 to 20:00
    Requires: inTime as str in hh:mm format within the working hours.
    Requires: inDate as str in yyyy-mm-dd format
    Requires: increment as int - the amount of minutes to be added
    Ensures: a tuple of two str the first with the end date, and the second with
    the end time in the (yyyy-mm-dd, hh:mm) format.
    """

    # converts time into a tuple of int (h, m)
    time = (int(inTime[0:2]), int(inTime[3:]))

    # converts date into a tuple of int (y, m, d)
    date = (int(inDate[0:4]), int(inDate[5:7]), int(inDate[8:]))

    endMinutes = time[1] + increment
    endHours = time[0]
    endDay = date[2]
    endMonth = date[1]
    endYear = date[0]

    if endMinutes > 59:
        endHours = endHours + endMinutes // 60
        endMinutes = endMinutes % 60
    
    while (endHours == 20 and endMinutes > 0) or endHours > 20:
        print(endHours)
        endHours = 8 + (20-endHours)
        endDay += 1 #corrigir um erro aqui

    while endDay > 30:
        endDay = 30 - endDay
        endMonth += 1

    while endMonth > 12:
        endMonth = 12 - endMonth
        endYear += 1

    return (
        str(endYear)+'-'+str(formatNumber(endMonth))+'-'+str(formatNumber(endDay)),
        str(formatNumber(endHours))+':'+str(formatNumber(endMinutes))
    )



def convertTime (inTime):
    """
    Converts an hh:mm string to minutes
    Requires: intime as str in hh:mm
    Ensures: the amount of minutes as int
    """

    return int(inTime[3:]) + 60*int(inTime[0:2])
