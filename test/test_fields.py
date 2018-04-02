from random import randrange

def test_fields_for_some_contact(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contact_info_from_home_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    print(contact_from_home_page.last_name, contact_from_home_page.first_name, contact_from_home_page.address)
    print(contact_from_edit_page.last_name, contact_from_edit_page.first_name, contact_from_edit_page.address)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
