__author__ = 'glassman'
import sys
import imaplib
import getpass
import email
import datetime
import cleanEmail

M = imaplib.IMAP4_SSL('imap.gmail.com')
emailsToRespond = {}
def main():
    try:
        M.login('washuschedulemaker@gmail.com', getpass.getpass())
        rv, mailboxes = M.list()
        if rv == 'OK':
            rv, data = M.select("ScheduleMaker")
            process_mailbox(M) # ... do something with emails, see below ...
            M.close()
    except imaplib.IMAP4.error:
        print "LOGIN FAILED!!! "
        # ... exit or deal with failure...

def process_mailbox(M):
    rv, data = M.search(None, "All")
    #(rv, messages) = M.search(None, '(UNSEEN)')
    if rv != 'OK':
        print "No messages found!"
        return
    #if data == ['']:
    #    print "No unread messages"
    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return
        if rv == 'OK':
            msg = email.message_from_string(data[0][1])
            #print 'Message %s: %s' % (num, msg['Subject'])
            #print 'Raw Date:', msg['Date']
            date_tuple = email.utils.parsedate_tz(msg['Date'])
            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(
                    email.utils.mktime_tz(date_tuple))
                #print "Local Date:", \
                    #local_date.strftime("%a, %d %b %Y %H:%M:%S")
            cleanEmail.getSchedule(msg.as_string())
            '''
            addressCleaning = msg['From'].split('<')[1]
            cleanedAddress = addressCleaning.split('>')[0]
            emailsToRespond.update({cleanedAddress,msg.as_string()})
            '''

if __name__ == "__main__":
    main()