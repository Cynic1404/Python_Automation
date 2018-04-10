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


constatnta = [
    Contact(first_name="First_name_1", last_name="Last_name1", nickname="Nickname1",email="Email1@mail.ru", homephone="123456"),
    Contact(first_name="First_name_2", last_name="Last_name2", nickname="Nickname2",email="Email2@mail.ru", homephone="7890")
]

testdata = [Contact(first_name="", middlename = "", last_name="", nickname="", email="", homephone="", address="")]+[
Contact(first_name=random_string("name", 15), last_name=random_string("last_name",15), nickname=random_string("nickname",15),
        email=random_email(), homephone=random_phone(), address=random_string("address",50))
for i in range(5)
]

