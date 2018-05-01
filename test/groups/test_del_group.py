from model.group import Group
from random import randrange
import random



def test_delete_some_group_compare_db(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


"""

def test_del_all_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.delete_all_groups()
    new_groups = len(app.group.get_group_list())
    assert new_groups == 0
    
"""