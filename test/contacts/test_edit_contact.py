# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random





def test_edit_some_contact_compare_db(app, orm, check_ui):

    contact = Contact(first_name="Some account first name", last_name="changed last name", nickname="changed nickname", homephone="+79260000000", email2="second@gmail.com", homepage="changed www.pythontraining.com", mobilephone="222222222")
    old_contacts_list = orm.get_contact_list()
    random_contact = random.choice(old_contacts_list)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts_list = orm.get_contact_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    for n in range(len(old_contacts_list)):
        if old_contacts_list[n].id == contact.id:
            old_contacts_list[n] = contact
            break
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




"""

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="test first name", last_name="test last name", homephone="000000000000000000000000000000000000"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Some account first name", last_name="changed last name", nickname="changed nickname", homephone="+79260000000", email2="second@gmail.com", homepage="changed www.pythontraining.com", mobilephone="222222222")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_first_contact_name(app):
    contact = Contact(last_name="Lomonosov")
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="new contact"))
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact_name(app):
    contact = Contact(last_name="Lomonosov")
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="new contact"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact_homephone(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name="test last name"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(homephone="428348273478231748231742731847231749")
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == app.contact.count()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

"""