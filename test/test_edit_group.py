# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="Edited group", header="Header edited", footer="Footer edited"))
    app.session.logout()



def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="New name"))
    app.session.logout()
    


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="New header"))
    app.session.logout()
