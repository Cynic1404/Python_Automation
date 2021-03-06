from random import randrange
import re

def test_fields_for_some_contact(app):
    index = randrange(app.contact.get_lenght_contacts_list())
    contact_hp = app.contact.get_contact_info_from_home_page(index)
    contact_ep = app.contact.get_contact_info_from_edit_page(index)
    print(contact_hp.all_emails_from_home_page)
    assert contact_hp.address == contact_ep.address
    assert contact_hp.first_name == contact_ep.first_name
    assert contact_hp.last_name == contact_ep.last_name
    assert contact_hp.all_phones == merge_phones_like_on_home_page(contact_ep)
    assert contact_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_ep)


def clear(s):
    return re.sub("[() -]","",s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",[contact.email, contact.email2, contact.email3]))