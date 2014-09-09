__author__ = 'glassman'
from icalendar import Calendar,Event
from pytz import timezone
import pytz
from datetime import datetime

def write(enrolledClasses):
    cal = Calendar()

    cal.add('version', '2.0') #http://icalendar.readthedocs.org/en/latest/
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('X-WR-CALNAME','WashU Classes' )

    utc = pytz.utc
    utc.zone
    central = timezone('US/Central') #We're always going to be going to classes in Central Timezone
    central.zone

    for item in enrolledClasses: #Recall enrolledClasses is a list of lists
        className = item[0]
        classLocation = item[1]
        year = item[2]
        classStartMonth = item[3]
        classEndMonth = item[4]
        classStartDay = item[5]
        classEndDay = item[6]
        classStartHour = item[7]
        classStartMinute = item[8]
        classEndHour = item[9]
        classEndMinute = item[10]
        classDaysOfWeek = item[11]

        event = Event()
        event.add('summary', className) #Event name is the name of the class
        event.add('dtstart', datetime(year,classStartMonth,classStartDay,classStartHour,classStartMinute,0,tzinfo=central)) #Event start time
        event.add('dtend', datetime(year,classStartMonth,classStartDay,classEndHour,classEndMinute,0,tzinfo=central)) #Event end time
        day_Time = {'until':datetime(year,classEndMonth,classEndDay,classEndHour,classEndMinute,0,tzinfo=central)} #Make a dictionary with only the last day of the semester
        day_Time.update(classDaysOfWeek) #Update the dictionary with our dictionary of days of the week from extractDaysTimes
        event.add('rrule',day_Time) #http://stackoverflow.com/questions/20143590/how-to-add-rrule-to-icalendar-event-in-python
        event['location'] = classLocation #Event location

        cal.add_component(event) #Put this event into a calendar

    import tempfile, os
    directory = os.getcwd() #Pick the current local directory
    f = open(os.path.join(directory, 'MyClassSchedule.ics'), 'wb') #Make an iCal file
    f.write(cal.to_ical())
    f.close()