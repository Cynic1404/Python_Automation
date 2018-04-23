from model.contact import Contact

def test_contacts_list(app, db):
    ui_list = app.contact.get_contacts_list()
    db_list = db.get_contacts_list()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    assert sorted(app.contact.get_emails_from_home_page()) == sorted(db.get_emails_list())



def test_phones(app, db):
    print(sorted(app.contact.get_phones_from_home_page()))
    print(sorted(sorted(db.get_phones_list())))
    assert sorted(app.contact.get_phones_from_home_page()) == sorted(db.get_phones_list())

