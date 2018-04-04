from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        #self.wd = webdriver.Chrome("C:\Python\chromedriver.exe")
        #self.wd = webdriver.Edge("C:\Python\MicrosoftWebDriver.exe")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
