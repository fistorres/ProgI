# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

import datetime

def newFile(date, time, fileType, company):
    """
    Opens a file in write mode and writes the required header in the first lines.
    Requires: date is datetime.date, time is datetime.time, company is str
     and fileType is str (must be either 'schedule' or 'experts').
    Ensures: the creation of a file with the required file name and header
    as stated in the project, the file is left open.
    """
    fileName = str(date.year)+'y'+str(date.month)+'m'+str(date.day) +\
               fileType+str(time.hour)+'h'+str(time.minute)+'.txt'
    file = open(fileName, 'w')  # opens a new file in write mode w/ fileName
    file.writelines(['Day: \n', str(date), '\n', 'Time: \n', str(time.hour),':', str(time.minute),
                     '\n', 'Company: \n', company, '\n', fileType.capitalize(), ': \n'])
    file.close()


def addSchedule(date, time, customer, expert):
    """
    Opens a schedule file in append mode, adds a new entry, then closes the file
    Requires: date is datetime.date, time is datetime.time, customer, worker are str
    Ensures: Adds a new line to the corresponding schedule file with the inputted
    information
    """
    fileName = str(date.year)+'y'+str(date.month)+'m'+str(date.day) +\
               'schedule'+str(time.hour)+'h'+str(time.minute)+'.txt'
    file = open(fileName, 'a')  # opens the corresponding file in append mode
    file.write(str(date) + ', ' + str(time.hour) + ':' + str(time.minute) + ', ' +
               customer + ', ' + expert)
    file.close()

def addExpert(date, time, expert):
    """
    Adds an expert to a experts file from a specific date and time
    Requires: expert is a dictionary, date is datetime.date, time is datetime.time
    Ensures: The expert information is appended to a file from a specific date and
    time
    """
    fileName = str(date.year)+'y'+str(date.month)+'m'+str(date.day) +\
               'experts'+str(time.hour)+'h'+str(time.minute)+'.txt'
    file=open(fileName,'a')  # opens the corresponding file in append mode
    file.write(str(expert['name'])+ ', ' +
               str(expert['location']) + ', ' +
               str(expert['skills']) + ', ' +
               str(expert['rating']) + ', ' +
               str(expert['rate']) + '*, ' +
               str(expert['freeDate']) + ', ' +
               str(expert['freeTime']) + ', ' +
               str(expert['earnings']))
    file.close()
