# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(group_name="Edited group", header="Header edited", footer="Footer edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()


def test_modify_group_name(app):
    group = Group(group_name="Cool")
    if app.group.count() == 0:
        app.group.create(Group(group_name="new group"))
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    name = app.group.get_first_group_name()
    group = Group(header="Turbo Header", group_name=name)
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
