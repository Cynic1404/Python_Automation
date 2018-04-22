# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random


def test_edit_some_group_compare_db(app, db):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(group_name="Edited some group", header="Header edited", footer="Footer edited")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == new_group.id:
            old_groups[i] = new_group
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""
def test_modify_first_group_name_compare_db(app, db):
    if app.group.count() == 0:
        app.group.create(Group(group_name="new group"))
    old_groups_from_db = db.get_group_list()
    old_groups = app.group.app.group.get_group_list()
    group = Group(group_name="Modified cool name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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


"""