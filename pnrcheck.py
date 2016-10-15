from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mailer
import datetime


class PNRMain:

    def __init__(self):
        self.status = []
        self.driver = webdriver.Firefox()
        self.mail = mailer.MailHandler()
        self.webAddress = "http://www.indianrail.gov.in/pnr_Enq.html"

    def launchBrowser(self):
        self.driver.get(self.webAddress)
        assert "Indian Railway" in self.driver.title
        self.driver.maximize_window()

    def enterPNR(self, pnr):
        box = self.driver.find_element_by_id("element")
        box.send_keys(pnr)
        box.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

    def getStatus(self):
        temp = []
        for row in self.driver.find_elements_by_xpath("//table[@id='center_table']/tbody/tr"):
            row_len = len(row.find_elements_by_tag_name("td"))
            if row_len == 3:
                temp.append(row.find_elements_by_tag_name("td")[-1].text)
        self.status = temp[1:]
        return self.status

    def composeMail(self, status):
        date = datetime.datetime.now()
        day = date.day
        month = date.month
        year = date.year
        date = str(day) + '/' + str(month) + '/' + str(year)
        sub = 'PNR status on ' + str(date)
        msg = 'Current status of your Tickets:'
        for ticket in status:
            msg += '\n' + ticket
        self.mail.sendMail(sub, msg)

    def closeTab(self):
        self.driver.close()

if __name__ == '__main__':
    obj = PNRMain()
    obj.launchBrowser()
    obj.enterPNR('<PNR number here>')
    status = obj.getStatus()
    #print(status)
    obj.composeMail(status)
    obj.closeTab()

