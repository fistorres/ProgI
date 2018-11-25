"""
This is my debugging script - it is not to be submitted for evaluation
-Gil
"""
import datetime
import filesWriting

date = datetime.date(2018,10,20)
time = datetime.time(4,20)

filesWriting.newFile(date, time,'schedule','iCageDoree')
filesWriting.addSchedule(date, time,'John Smith','Jane Doe')
