from model.contact import Contact


def test_contacts_list(app, db):
    ui_list = app.contact.get_contacts_list()
    db_list = db.get_contact_list()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    assert sorted(app.contact.get_emails_from_home_page()) == sorted(db.get_emails_list())
    assert sorted(app.contact.get_phones_from_home_page()) == sorted(db.get_phones_list())
    assert sorted(app.contact.get_address()) == sorted(db.get_address())



def test_contact_info_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_one_contact()
    contacts_ui = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_ui) == len(contacts_db)
    for i in range(len(contacts_ui)):
        assert contacts_ui[i].first_name == contacts_db[i].first_name
        assert contacts_ui[i].last_name == contacts_db[i].last_name
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contacts_db[i])