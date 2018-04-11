# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contacts import testdata



#@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])

def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



