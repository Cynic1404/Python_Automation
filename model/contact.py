from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last_name=None, nickname=None, home_telephone=None, email=None, homepage=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.home_telephone = home_telephone
        self.email = email
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "%s:%s,%s" % (self.id, self.last_name, self.first_name)



    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize