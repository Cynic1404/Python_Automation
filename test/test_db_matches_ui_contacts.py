from model.contact import Contact

def test_contacts_list(app, db):
    ui_list = app.contact.get_contacts_list()
    db_list = db.get_contacts_list()

    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


