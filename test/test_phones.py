from fixture.contact import Contact
import re

def test_phones_on_home_page(app):
    contact = Contact(first_name="My first", last_name="Contact", nickname="Nickname", email="test@gmail.com",
                      homepage="www.pythontraining.com", homephone="+79261111111", workphone="+7888888",
                      mobilephone="+3333333", secondaryphone="+222222222")
    if app.contact.count() == 0:
        app.contact.add_new_contact(contact)
    #contact_from_home_page = app.contact.get_contact_info_from_home_page(0)
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)



def test_phones_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]","",s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x), filter(lambda x: x is not None,[clear(contact.homephone), clear(contact.mobilephone), clear(contact.workphone), clear(contact.secondaryphone)]))))

