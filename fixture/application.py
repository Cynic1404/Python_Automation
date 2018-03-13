from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # start to create a group
        wd.find_element_by_name("new").click()
        # fill forms
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_group_page()


    def return_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()



    def open_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()


    def add_contact(self, contact):
        wd = self.wd
        self.open_contacts_page()
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
        self.return_contacts_page()


    def return_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def destroy(self):
        self.wd.quit()
