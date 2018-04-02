from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middlename = None, last_name=None, address = None, nickname=None, company = None, homephone=None, email=None, email2=None, email3=None, homepage=None, id=None,
                 all_phones_from_home_page = None, workphone = None, mobilephone = None, secondaryphone = None, all_emails_from_home_page = None):
        self.first_name = first_name
        self.middlename = middlename
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.homepage = homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone


    def __repr__(self):
        return "%s:%s,%s" % (self.id, self.last_name, self.first_name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize