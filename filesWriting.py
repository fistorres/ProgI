# 2018-2019 Programação 1 (LTI)
# Grupo 38
# 49187 Sofia Torres
# 49269 Mário Gil Oliveira


def writeHeader(fileName,day,time,type,company):
    """
    Opens a file in write mode and writes the required header in the first lines.
    Requires: fileName is str of a .txt file, day is str in YYYY-MM-DD format,
    time is str in HH:MM format, and company is str, type is str.
    Ensures: the creation of a file with the required header as stated in the project
    which states the day, time, time and type of file (e.g. schedule).
    """
    file = open(fileName, 'w')
    File.writelines(['Day: \n', day, 'Time: \n', time, 'Company: \n', company, type': \n'])
    file.close()