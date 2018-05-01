from model.contact import Contact


def test_contacts_list(app, orm):
    ui_list = app.contact.get_contacts_list()
    db_list = orm.get_contact_list()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    assert sorted(app.contact.get_emails_from_home_page()) == sorted(orm.get_emails_list())
    assert sorted(app.contact.get_phones_from_home_page()) == sorted(orm.get_phones_list())
    assert sorted(app.contact.get_address()) == sorted(orm.get_address())


