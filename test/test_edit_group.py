# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(group_name="Edited group", header="Header edited", footer="Footer edited"))




def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(group_name="Cool"))

    


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(footer="Yeeep"))

