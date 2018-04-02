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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("phone2", contact.secondaryphone)



    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def add_new_contact(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # start to create a contact
        self.fill_contact_form(contact)
        # confirm adding contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contacts_cache = None


    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.modify_contact_by_index(0, contact)


    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contacts_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[7]/a/img").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contacts_cache = None


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None


    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                first_name = element.find_elements_by_tag_name("td")[2].text
                last_name = element.find_elements_by_tag_name("td")[1].text
                self.contacts_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
                print(id,first_name,last_name)
        return list(self.contacts_cache)


    def get_first_contact_last_name(self):
        wd = self.app.wd
        self.open_home_page()
        last_name = wd.find_elements_by_name("entry")[0].find_elements_by_tag_name("td")[1].text
        return last_name


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id = id, homepage=homephone, workphone=workphone,mobilephone=mobilephone, secondaryphone=secondaryphone)


