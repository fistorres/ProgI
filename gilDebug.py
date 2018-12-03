"""
This is my debugging script - it is not to be submitted for evaluation
-Gil
"""
import datetime
import filesWriting
import scheduling
import filesReading
import constants

expert1 = [
    'Dan Tufis', # 0 - name
    'lisbon',  # 1
    ('heating', 'doors', 'windows'),  # 2
    5,  # 3
    10,  # 4
    '2018-10-11', # 5
    '9:15',  # 6
    2879]  # 7

expert2 = [
    'Toze Manel', # 0
    'lisbon',  # 1
    ('heating', 'doors', 'windows'),  # 2
    2,  # 3
    20,  # 4
    datetime.date(2018, 10, 2), # 5
    datetime.time(9,15),  # 6
    2879]  # 7

experts = [expert1, expert2]

client = [
    'Guillaume Dutroux',
    'lisbon',
    datetime.date(2019,3,12),
    datetime.time(10,0),
    1000000000,
    0,
    'doors',
    datetime.time(1,0)
]

#  print('Os experts possiveis sao:', scheduling.atribution(client, experts))


#debug filesWriting
date = '2018-10-20'
time = '04:20'

filesWriting.newFile(date, time, 'schedule', 'iCageDoree')
filesWriting.addSchedule(date, time, 'John Smith', 'Jane Doe')



filesWriting.newFile(date, time, 'experts','iCageDoree')
filesWriting.addExpert(date,time,expert1)


'''
#debug attribution
m = format.formatdateClients("2019y03m20clients12h30.txt")
n = format.formatdateExperts("2019y03m20experts12h30.txt")
print(scheduling.attribution(m[2], n))

'''

'''
print(constants.timeCalculate('2018-10-20', '20:00', 12*60))
'''


