"""
This is my debugging script - it is not to be submitted for evaluation
-Gil
"""
import datetime
import filesWriting

date = datetime.date(2018,10,20)
time = datetime.time(4,20)

filesWriting.newFile(date, time, 'schedule', 'iCageDoree')
filesWriting.addSchedule(date, time, 'John Smith', 'Jane Doe')

expert = {
    'name': 'Dan Tufis',
    'location': 'lisbon',
    'skills': ('heating','doors','windows'),
    'rating': 2,
    'rate': 20,
    'freeDate': datetime.date(2018, 10, 30),
    'freeTime': datetime.time(9, 00),
    'earnings': 2879
}

filesWriting.newFile(date, time, 'experts','iCageDoree')
filesWriting.addExpert(date,time,expert)