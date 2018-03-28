from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # start to create a group
        wd.find_element_by_name("new").click()
        # fill forms
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_page()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # start to edit first group
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        # fill forms
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_groups_page()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_groups_page()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(group_name=text, id=id))
        return groups

    def get_first_group_name(self):
        wd = self.app.wd
        self.open_groups_page()
        name = (wd.find_elements_by_css_selector("span.group"))[0].text
        return name
