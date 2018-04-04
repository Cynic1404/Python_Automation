# -*- coding: utf-8 -*-
from model.group import Group
import pytest

testdata = [Group(group_name="My_first_group", header="Header", footer="Footer"),
            Group(group_name="", header="", footer="")]

@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])



def test_add_group(app, group):
    pass

    """
    old_groups = app.group.get_group_list()
    group = Group(group_name="My_first_group", header="Header", footer="Footer")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) +1 == app.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
"""
