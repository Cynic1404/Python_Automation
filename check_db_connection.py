import pymysql.cursors
from fixture.db import DbFixture

db = DbFixture(host ="127.0.0.1", name ="addressbook", user ="root", password ="")

"""
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()

"""
try:
    d = db.get_contacts_list()
    for contact in d:
        print(contact)
    print(len(d))

finally:
    db.destroy()


