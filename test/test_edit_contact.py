# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.modify_first_contact(Contact(first_name="changed first name", last_name="changed last name", nickname="changed nickname", home_telephone="changed +79261111111", email="changed test@gmail.com", homepage="changed www.pythontraining.com"))

