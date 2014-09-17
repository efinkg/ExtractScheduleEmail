__author__ = 'glassman'

def getSchedule(msg):
    cleaningFallSchedule = msg.split('YOUR FL2014 COURSES AS OF:')[1]
    cleanerFallSchedule = cleaningFallSchedule.split('\n')[2]
    print cleanerFallSchedule
    cleanedFallSchedule = cleaningFallSchedule.split('Please note:')[0]
    #print cleanedFallSchedule