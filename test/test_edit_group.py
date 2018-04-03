# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange





def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="new group"))
    old_groups = app.group.get_group_list()
    group = Group(group_name="Modified cool name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="Edited some group", header="Header edited", footer="Footer edited")
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()


def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="new group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="Modified cool name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    name = app.group.get_first_group_name()
    group = Group(header="Super Header", group_name=name)
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()



