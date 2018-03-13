# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(first_name="My first", last_name="Contact", nickname="Mr.First", home_telephone="+79261111111", email="test@gmail.com", homepage="www.pythontraining.com"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.add(Contact(first_name="", last_name="", nickname="", home_telephone="", email="", homepage=""))
    app.session.logout()
