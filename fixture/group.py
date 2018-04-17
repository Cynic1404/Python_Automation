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
        self.group_cache = None


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_name("selected[]")[index].click()


    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # start to edit first group
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill forms
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_groups_page()
        self.group_cache = None


    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def delete_first_group(self):
        self.delete_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_groups_page()
        self.group_cache = None


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache = None


    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, id=id))
        return list(self.group_cache)


    def get_first_group_name(self):
        wd = self.app.wd
        self.open_groups_page()
        name = (wd.find_elements_by_css_selector("span.group"))[0].text
        return name




    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        for i in range(len(self.app.wd.find_elements_by_name("selected[]"))):
            wd.find_elements_by_name("selected[]")[i].click()
        wd.find_element_by_name("delete").click()
        self.return_groups_page()
        self.group_cache = None


    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_ccs_selector("input[value='%s']" % id).click()
