from model.contact import Contact
from random import randrange
import random

"""
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="Vladimir", last_name="Lenin", home_telephone="000000000000000000000000000000000000"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="Vladimir", last_name="Lenin", homephone="000000000000000000000000000000000000"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


"""
def test_delete_some_contact_compare_db(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.add_new_contact(Contact(first_name="Vladimir", last_name="Lenin", homephone="000000000000000000000000000000000000"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
