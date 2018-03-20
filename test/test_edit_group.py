# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(group_name="Edited group", header="Header edited", footer="Footer edited"))
    app.session.logout()
