# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira

import filesReading

def newFile(date, time, fileType, company):
    """
    Opens a file in write mode and writes the required header in the first lines.
    Requires: date is str in YYYY-MM-DD format
    Requires: time is str in HH:MM format
    Requires: company is str, the name of the company
    Requires: fileType is str (must be either 'schedule' or 'experts').
    Ensures: the creation of a file with the required file name and header
    as stated in the project, the file is left open.
    """

    fileName = date[0:4]+'y'+date[5:7]+'m'+date[8:10] +\
               fileType + time[0:2]+'h'+time[3:5]+'.txt'
    file = open(fileName, 'w')  # opens a new file in write mode w/ fileName
    file.writelines(['Day: \n', date, '\n',
                     'Time: \n', time, '\n',
                     'Company: \n', company, '\n',
                     fileType.capitalize(), ': \n'])
    file.close()
    return fileName


def addSchedule(fileName, tupleClientExpert):
    """
    Opens a schedule file in append mode, adds a new entry, then closes the file
    Requires: fileName
    Requires: tupleClientExpert as tuple
    Ensures: Adds a new line to the corresponding schedule file with the inputted
    information
    """
    file = open(fileName, 'a')  # opens the corresponding file in append mode
    if len(tupleClientExpert[1]) == 1:  #  se o tuplo for declined
        file.write(
            filesReading.readHeader(fileName)[0] + ', ' +
            filesReading.readHeader(fileName)[1] + ', ' +
            tupleClientExpert[0][0] + ', ' +
            tupleClientExpert[1][0] + '\n'
        )
    else:
        file.write(
            tupleClientExpert[1][5] + ', ' +
            tupleClientExpert[1][6] + ', ' +
            tupleClientExpert[0][0] + ', ' +
            tupleClientExpert[1][0] + '\n'
        )
        file.close()

def addExpert(fileName, expert):
    """
    Adds an expert to a experts file from a specific date and time
    Requires: expert is a list
    Requires: fileName as str
    Ensures: The expert information is appended to a file from a specific date and
    time
    """
    file=open(fileName,'a')  # opens the corresponding file in append mode

    # writes the expert information, as well as the corresponding time
    file.write(
        str(expert[0]) + ', ' +
        str(expert[1]) + ', ' +
        str(expert[2]) + ', ' +
        str(expert[3]) + '*, ' +
        str(expert[4]) + ', ' +
        str(expert[5]) + ', ' +
        str(expert[6]) + ', ' +
        str(expert[7]) + '\n'
    )
    file.close()
