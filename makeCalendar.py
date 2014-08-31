__author__ = 'glassman'
from icalendar import Calendar,Event
from pytz import timezone
import pytz
from datetime import datetime
from icalendar import LocalTimezone

def write(enrolledClasses):

    cal = Calendar()

    cal.add('version', '2.0') #http://icalendar.readthedocs.org/en/latest/
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('X-WR-CALNAME','WashU Classes' )

    utc = pytz.utc
    utc.zone
    central = timezone('US/Central') #We're always going to be going to classes in Central Timezone
    central.zone

    for item in enrolledClasses:
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
        event.add('summary', className)
        event.add('dtstart', datetime(year,classStartMonth,classStartDay,classStartHour,classStartMinute,0,tzinfo=central))
        event.add('dtend', datetime(year,classStartMonth,classStartDay,classEndHour,classEndMinute,0,tzinfo=central))
        day_Time = {'until':datetime(year,classEndMonth,classEndDay,classEndHour,classEndMinute,0,tzinfo=central)}
        day_Time.update(classDaysOfWeek)
        event.add('rrule',day_Time) #http://stackoverflow.com/questions/20143590/how-to-add-rrule-to-icalendar-event-in-python
        event['location'] = classLocation

        cal.add_component(event)

    import tempfile, os
    directory = tempfile.mkdtemp()
    f = open(os.path.join('/Users/glassman/SkyDrive/Silly Engineering/ExtractSchedule', 'MyClassSchedule.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()