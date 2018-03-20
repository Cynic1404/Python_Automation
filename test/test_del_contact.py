from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(first_name="test first name", last_name="test last name", home_telephone="000000000000000000000000000000000000"))
    app.contact.delete_first_contact()
