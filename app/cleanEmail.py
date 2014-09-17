__author__ = 'glassman'
import extractDaysTimes
import getDates

classList = []
enrolledClasses = []

def getSchedule(msg):
    if 'COURSES AS OF:' in msg:
        cleaningFallSchedule = str(msg.split('COURSES AS OF:')[1])
        semester = str(msg.split('COURSES AS OF:')[0]).split('YOUR')[1]
        print semester
        year = semester[-5:-1]
        semester = semester[1:3]
        cleanerFallSchedule = str(cleaningFallSchedule).split('Please note:')[0]
        cleanerFallSchedule = str(cleanerFallSchedule).partition('AM')[::1]
        #cleanerFallSchedule = str(cleanerFallSchedule).replace('\\n','')
        cleanerFallSchedule = str(cleanerFallSchedule).replace('\\r','')
        classes = str(cleanerFallSchedule).split('Enrolled')
        i = 0
        j = len(classes)
        while (i<j-1):
            extractInfo(classes[i],year,semester)
            #classList.append(classes[i])
            #print classes[i]
            i+=1

def extractInfo(classInfo,year,semester):
    classInfo = classInfo.split('.0 ')[1]
    className = classInfo.split('\\n')[0]
    if str(className).startswith('Credit'):
        className = str(className).split('Credit ')[1]
    classInfo = classInfo.split('\\n')[-1]
    classLocation = classInfo.split(' -')[0]
    classTimes = classInfo
    if ' -' in str(classInfo):
        classInfo = classInfo.split(' -')[1]
    elif 'M-' in str(classInfo):
        classInfo = 'M-' + str(classInfo.split('M-')[1])
    classTime = classTimes.split('- ')[1:]
    classDays = classInfo.split(' ')[0]
    #classTime = str(classTimes.split(':')[0])+':'+str(classTimes.split(':')[1])+':'+str(classTimes.split(':')[2])
    print classTime
    classStartHour,classStartMinute,classEndHour,classEndMinute = extractDaysTimes.extractStartStopTimes(classTime)
    daysWithClass = extractDaysTimes.extractDaysOfWeek(classDays)
    firstMonth,firstDay,lastMonth,lastDay = getDates.findBeginEnd(semester,year) #Send this info to getDates to find when this specific semester starts and ends
    #print "Class " + str(className) + " meets in " + str(classLocation) + " on the days " + str(classDays) + ' from ' + str(classTime)

'''
def makeCalendar():
    enrolledClasses.append([className,classLocation,classYear,firstMonth,lastMonth,firstDay,lastDay,classStartHour,classStartMinute,classEndHour,classEndMinute,classDaysOfWeek])

makeCalendar.write(enrolledClasses) #Make this info into calendar events
'''