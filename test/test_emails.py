
from fixture.contact import Contact


def test_emails_on_home_page(app):
    contact = Contact(first_name="My first", last_name="Contact", nickname="Nickname", email="test@gmail.com",
                      homepage="www.pythontraining.com", homephone="+79261111111", workphone="+7888888",
                      mobilephone="+3333333", secondaryphone="+222222222")
    if app.contact.count() == 0:
        app.contact.add_new_contact(contact)
    contact_from_home_page = app.contact.get_contact_info_from_home_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    print("ooooooooooooooooooooooooo", contact_from_home_page.all_emails_from_home_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    print("AAAAAAAAAAAAAAAAAAA" , "\n".join(filter(lambda x: x !="",[contact.email, contact.email2, contact.email3])) )
    return "\n".join(filter(lambda x: x !="",[contact.email, contact.email2, contact.email3]))




