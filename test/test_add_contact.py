# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="My first", last_name="Contact", nickname="Nickname", email="test@gmail.com", homepage="www.pythontraining.com", homephone="+79261111111", workphone="+7888888", mobilephone="+3333333", secondaryphone="+222222222")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

"""
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="", last_name="", nickname="", homephone="", email="", homepage="", workphone="", mobilephone="", secondaryphone="")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
"""



