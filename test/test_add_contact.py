# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(first_name="My first", last_name="Contact", nickname="Mr.First", home_telephone="+79261111111", email="test@gmail.com", homepage="www.pythontraining.com"))
    app.logout()

def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.add_contact(Contact(first_name="", last_name="", nickname="", home_telephone="", email="", homepage=""))
    app.logout()
