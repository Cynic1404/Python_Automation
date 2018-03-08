# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")


    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def open_contacts_page(self, wd):
        wd.find_element_by_link_text("add new").click()


    def add_contact(self, wd, contact):
        # start to create a contact
        wd.find_element_by_name("firstname").click()
        # fill forms
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.home_telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # confirm adding contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def return_contacts_page(self, wd):
        wd.find_element_by_link_text("add new").click()


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contacts_page(wd)
        self.add_contact(wd, Contact(first_name="My first", last_name="Contact", nickname="Mr.First", home_telephone="+79261111111", email="test@gmail.com", homepage="www.pythontraining.com"))
        self.return_contacts_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_contacts_page(wd)
        self.add_contact(wd, Contact(first_name="", last_name="", nickname="", home_telephone="", email="", homepage=""))
        self.return_contacts_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
