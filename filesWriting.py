# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira


def newFile(year, month, day, hour, minute, fileType, company):
    """
    Opens a file in write mode and writes the required header in the first lines.
    Requires: y,mo,d,h, min are int, and company is str, fileType is str.
    Ensures: the creation of a file with the required file name and header
    as stated in the project, the file is left open.
    """
    fileName = str(year)+'y'+str(month)+'m'+str(day)+fileType+str(hour)+'h'+str(minute)+'.txt'
    file = open(fileName, 'w')  # opens a new file in write mode w/ fileName
    date = str(year)+'-'+str(month)+'-'+str(day)
    time = str(hour)+':'+str(minute)
    file.writelines(['Day: \n', date, '\n', 'Time: \n', time, '\n',
                     'Company: \n', company, '\n', fileType.capitalize(), ': \n'])
    file.close()


def addSchedule(year, month, day, hour, minute, customer, worker):
    """
    Opens a schedule file in append mode, adds a new entry, then closes the file
    Requires: year, month, day, hour, minute are int, customer, worker are str
    Ensures: Adds a new line to the corresponding schedule file with the inputted
    information
    """
    fileName = str(year)+'y'+str(month)+'m'+str(day)+'schedule'+str(hour)+'h'+str(minute)+'.txt'
    file = open(fileName, 'a')  # opens the corresponding file in append mode
    file.write(str(year) + '-' + str(month) + '-'+str(day) + ', ' +
               str(hour) + ':' + str(minute)+', ' + customer + ', ' + worker)
    file.close()
