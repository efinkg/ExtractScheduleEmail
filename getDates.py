__author__ = 'glassman'
import urllib3
import csv
import monthNumber
from BeautifulSoup import BeautifulSoup

def findBeginEnd(semester,year):
    http = urllib3.PoolManager()
    academicCalendar = http.request('GET','http://registrar.wustl.edu/academic-calendars/')
    calendarData = BeautifulSoup(academicCalendar.data)

    calendarTable = calendarData.find(id='content')

    listofcols = []
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
                if '<strong>' in text:
                    splitText = text.split('<strong>')[1]
                    splitText = splitText.split('</strong>')[0]
                    if splitText == '\xc2\xa0':
                        splitText = ' '
                    if splitText.startswith('\xc2\xa0'):
                        splitText = splitText[2:]
                    if splitText != '* no classes':
                        if colNum < 5:
                            if colNum == 0:
                                if splitText.startswith('2'):
                                    listofcols[colNum].append(' ')
                                    colNum += 1
                            listofcols[colNum].append(splitText)
                            colNum += 1
    if semester == "FL":
        for i in range (0,5):
            if listofcols[i][0].startswith(year):
                firstDay = listofcols[i][1]
                #print "First day is " + listofcols[i][1]
                lastDay = listofcols[i][5]
                #print "Last day is " + listofcols[i][5]
    elif semester == "SP":
        for i in range (0,5):
            print year[-2:]
            if listofcols[i][0].endswith(year[-2:]):
                firstDay = listofcols[i][7]
                #print "First day is " + listofcols[i][7]
                lastDay = listofcols[i][10]
                #print "Last day is " + listofcols[i][10]

    firstMonth = int(monthNumber.monthToNum(firstDay.split(' ')[0]))
    firstDay = int(firstDay.split(' ')[1])
    lastMonth = int(monthNumber.monthToNum(lastDay.split(' ')[0]))
    lastDay = int(lastDay.split(' ')[1])
    return firstMonth,firstDay,lastMonth,lastDay