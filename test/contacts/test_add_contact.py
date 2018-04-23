# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_with_json_compare_db(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.add_new_contact(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


def test_add_contact_with_data_compare_db(app, db, data_contacts, check_ui):
    contact = data_contacts
    old_contacts = db.get_contacts_list()
    app.contact.add_new_contact(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)


    
def test_add_contact_with_json(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_add_contact_with_data(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

