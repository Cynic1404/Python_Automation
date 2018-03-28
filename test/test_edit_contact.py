# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="test first name", last_name="test last name", home_telephone="000000000000000000000000000000000000"))
    old_cotacts = app.contact.get_contacts_list()
    app.contact.modify_first_contact(Contact(first_name="craetwsdasfasfhsahflas first name", last_name="changed last name", nickname="changed nickname", home_telephone="changed +79261111111", email="changed test@gmail.com", homepage="changed www.pythontraining.com"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_cotacts) == len(new_contacts)


def test_edit_first_contact_name(app):
    contact = Contact(last_name="Lomonosov")
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="new contact"))
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_first_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="test last name"))
    old_contacts = app.contact.get_contacts_list()
    last_name = app.contact.get_first_contact_last_name()
    contact = Contact(home_telephone="428348273478231748231742731847231749", last_name = last_name)
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

