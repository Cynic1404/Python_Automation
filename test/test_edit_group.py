# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.group.modify_first_group(Group(group_name="Edited group", header="Header edited", footer="Footer edited"))




def test_modify_group_name(app):
    app.group.modify_first_group(Group(group_name="New name"))

    


def test_modify_group_header(app):
    app.group.modify_first_group(Group(footer="New header"))

