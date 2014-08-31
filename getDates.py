__author__ = 'glassman'
import urllib3
import monthNumber
from BeautifulSoup import BeautifulSoup
#We want to get the most up to date academic calendar for this semester

def findBeginEnd(semester,year):
    http = urllib3.PoolManager()
    academicCalendar = http.request('GET','http://registrar.wustl.edu/academic-calendars/') #Pull down the academic calendar webpage
    calendarData = BeautifulSoup(academicCalendar.data)
    calendarTable = calendarData.find(id='content') #Find the academic calendar table

    listofcols = [] #Make a list of lists of each collumn in the table
    col1 = []
    listofcols.append(col1)
    col2 = []
    listofcols.append(col2)
    col3 = []
    listofcols.append(col3)
    col4 = []
    listofcols.append(col4)
    col5 = []
    listofcols.append(col5)

    rows = calendarTable.findAll('tr')
    for tr in rows:
        colNum = 0
        cols = tr.findAll('td')
        for td in cols:
            for item in td:
                text = str(item)
                if '<strong>' in text: #For some reason the years were not coming out with item.string
                    splitText = text.split('<strong>')[1] #Let's brute force rip out the information and hope no one removes the bold tags
                    splitText = splitText.split('</strong>')[0]
                    if splitText == '\xc2\xa0': #Replace ASCII tag for spaces with a space
                        splitText = ' '
                    if splitText.startswith('\xc2\xa0'): #Get rid of ASCII tags for spaces at the beginning of items
                        splitText = splitText[2:]
                    if splitText != '* no classes': #Iterate until the end of the table
                        if colNum < 5:
                            if colNum == 0:
                                if splitText.startswith('2'):
                                    listofcols[colNum].append(' ')
                                    colNum += 1
                            listofcols[colNum].append(splitText)
                            colNum += 1
    if semester == "FL": #Pull info for fall semster
        for i in range (0,5):
            if listofcols[i][0].startswith(year): #Find the year of interest
                firstDay = listofcols[i][1] #First day is
                lastDay = listofcols[i][5] #Last day is
    elif semester == "SP":
        for i in range (0,5):
            print year[-2:]
            if listofcols[i][0].endswith(year[-2:]):
                firstDay = listofcols[i][7]
                lastDay = listofcols[i][10]

    firstMonth = int(monthNumber.monthToNum(firstDay.split(' ')[0])) #Split the text into month names, pass to monthNumber
    firstDay = int(firstDay.split(' ')[1]) #Split the text into day int
    lastMonth = int(monthNumber.monthToNum(lastDay.split(' ')[0]))
    lastDay = int(lastDay.split(' ')[1])
    return firstMonth,firstDay,lastMonth,lastDay