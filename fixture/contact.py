from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def open_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(
                wd.find_elements_by_xpath("//form[@id='LoginForm']/input[3]")) > 0 and len(
                wd.find_elements_by_xpath("//table[@id='maintable']//a[.='All e-mail']")) > 0:
            return
        wd.find_element_by_link_text("home").click()


    def open_new_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 1:
            return
        wd.find_element_by_link_text("add new").click()


    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.home_telephone)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def add_new_contact(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # start to create a contact
        self.fill_contact_form(contact)
        # confirm adding contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()


    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        #confirm edition
        wd.find_element_by_name("update").click()
        self.return_home_page()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            first_name = element.find_elements_by_tag_name("td")[2].text
            last_name = element.find_elements_by_tag_name("td")[1].text
            contacts.append(Contact(first_name=first_name, last_name=last_name, id=id))
            print(id,first_name,last_name)
        return contacts

        """
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(group_name=text, id=id))
        return groups
        """