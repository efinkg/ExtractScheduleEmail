__author__ = 'glassman'

def extractStartStopTimes(classDayTime):
    classStartEnd = classDayTime[1].split('-')
    if classStartEnd[0].endswith('a'):
        classStartEnd[0] = classStartEnd[0][:-1]
        classStart = classStartEnd[0] #+ " AM"
        classStartHour = int(classStart.split(':')[0])
        classStartMinute = int(classStart.split(':')[1])
    if classStartEnd[0].endswith('p'):
        classStartEnd[0] = classStartEnd[0][:-1]
        classStart = classStartEnd[0] #+ " PM"
        if int(classStart.split(':')[0]) == 12:
            classStartHour = int(classStart.split(':')[0])
        else:
            classStartHour = int(classStart.split(':')[0]) + 12
        classStartMinute = int(classStart.split(':')[1])

    if classStartEnd[1].endswith('a'):
        classStartEnd[1] = classStartEnd[1][:-1]
        classEnd = classStartEnd[1] #+ " AM"
        classEndHour = int(classEnd.split(':')[0])
        classEndMinute = int(classEnd.split(':')[1])
    if classStartEnd[1].endswith('p'):
        classStartEnd[1] = classStartEnd[1][:-1]
        classEnd = classStartEnd[1] #+ " PM"
        if int(classEnd.split(':')[0]) == 12:
            classEndHour = int(classEnd.split(':')[0])
        else:
            classEndHour = int(classEnd.split(':')[0]) + 12
        classEndMinute = int(classEnd.split(':')[1])

    return classStartHour,classStartMinute,classEndHour,classEndMinute

def extractDaysOfWeek(classDayTime):
    classDays = classDayTime[0].split('-')
    daysWithClass = {'freq':'weekly'}
    daysInClass = []
    for item in classDays:
        if item == 'M':
            daysInClass.append('MO')
        if item == 'T':
            daysInClass.append('TU')
        if item == 'W':
            daysInClass.append('WE')
        if item == 'R':
            daysInClass.append('TH')
        if item == 'F':
            daysInClass.append('FR')
    daysWithClass.update({'byday':daysInClass})
    return daysWithClass