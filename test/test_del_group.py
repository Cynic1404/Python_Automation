from model.group import Group
from random import randrange
import random



def test_delete_some_group_compare_db(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups



"""
def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups

def test_del_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.delete_all_groups()
    new_groups = len(app.group.get_group_list())
    assert new_groups == 0

"""

