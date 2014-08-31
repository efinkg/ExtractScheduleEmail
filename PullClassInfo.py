__author__ = 'glassman'
import extractDaysTimes
import makeCalendar
import getDates
from BeautifulSoup import BeautifulSoup
#We plan to make iCal files Google Calendar can understand

classList = BeautifulSoup(open('Class Schedule.html')) #Open your download of the printer friendly version of your WebStac class schedule page

semester = classList.find(selected="selected") #Figure out what semester this schedule is for
fallSpring = semester.contents[0][0:2] #Semester name is in the first two char FL or SP
classYear = int(semester.contents[0][2:6]) #Year name is the 3rd -> 7th chars (ie 2014)
firstMonth,firstDay,lastMonth,lastDay = getDates.findBeginEnd(fallSpring,classYear) #Send this info to getDates to find when this specific semester starts and ends

enrolledClasses = []

classesTable = classList.find(id='tabSched') #Parse through the HTML table and put information for each class into a list of lists
rows = classesTable.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    classInfo = [] #Temporary list of info for each class
    for td in cols:
        for item in td:
            classInfo.append(item.string)
    if classInfo[0] == 'Enrolled': #We only want to add classes we are enrolled in
        classTime = classInfo[5]
        classDayTime = classTime.split(' ') #classDayTime[0] is the days of the week
                                            #classDatTime[1] is the start-end time
        classStartHour,classStartMinute,classEndHour,classEndMinute = extractDaysTimes.extractStartStopTimes(classDayTime) #Find when the class starts and stops
        classDaysOfWeek = extractDaysTimes.extractDaysOfWeek(classDayTime) #Find which days of the week this class is held
        className = classInfo[2]
        classLocation = classInfo[6]
        enrolledClasses.append([className,classLocation,classYear,firstMonth,lastMonth,firstDay,lastDay,classStartHour,classStartMinute,classEndHour,classEndMinute,classDaysOfWeek])

makeCalendar.write(enrolledClasses) #Make this info into calendar events