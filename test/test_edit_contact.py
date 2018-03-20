# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="test first name", last_name="test last name", home_telephone="000000000000000000000000000000000000"))
    app.contact.modify_first_contact(Contact(first_name="craetwsdasfasfhsahflas first name", last_name="changed last name", nickname="changed nickname", home_telephone="changed +79261111111", email="changed test@gmail.com", homepage="changed www.pythontraining.com"))

def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="test last name"))
    app.contact.modify_first_contact(Contact(first_name="pabaaam first name"))


def test_edit_first_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="test last name"))
    app.contact.modify_first_contact(Contact(home_telephone="428348273478231748231742731847231749"))
