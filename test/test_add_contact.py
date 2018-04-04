# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
from random import randint

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone():
    return "+" + str(randint(1,10)) + "-" + "".join([random.choice(string.digits) for i in range(3)]) + "-" + "".join([random.choice(string.digits) for i in range(3)])+"-"+"".join([random.choice(string.digits) for i in range(2)])+"-"+"".join([random.choice(string.digits) for i in range(2)])

def random_email():
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1,10))])+"@"+ "".join([random.choice(symbols) for i in range(random.randrange(1,10))]) + random.choice([".ru", ".com"])


testdata = [Contact(first_name="", middlename = "", last_name="", nickname="", email="", homephone="", address="")]+[
Contact(first_name=random_string("name", 15), last_name=random_string("last_name",15), nickname=random_string("nickname",15),
        email=random_email(), homephone=random_phone(), address=random_string("address",50))
for i in range(5)
]



@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



