# Module for handling the Mail sending part
import smtplib


class MailHandler:

    def __init__(self):
        try:
            self.sender = '<Insert sender mail address here>'
            self.recipients = '<Insert recipient mail address here>'
            self.server = smtplib.SMTP('smtp.gmail.com:587')
            self.server.ehlo()
            self.server.starttls()
            self.server.login('<Sender Email address>', '<Password>')
        except Exception as e:
            print(str(e))

    def sendMail(self, subject, message):
        #print(message)
        msg = 'Subject: ' + subject + '\n' + message + '\n' + 'Thanks!\nXYZ'
        self.server.sendmail(self.sender, self.recipients, msg)

if __name__ == '__main__':
    obj = MailHandler()
    obj.sendMail("Testing", "A mail from myself")
