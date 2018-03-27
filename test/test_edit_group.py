# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(group_name="Edited group", header="Header edited", footer="Footer edited"))
    old_groups = app.group.get_group_list()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(group_name="Cool"))
    old_groups = app.group.get_group_list()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(footer="Yeeep"))
    old_groups = app.group.get_group_list()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



