from model.group import Group
import random
import string


testdata = [
    Group(group_name="Name1", header="Header1", footer="Footer1"),
    Group(group_name="Name2", header="Header2", footer="Footer2"),
    Group(group_name="Name3", header="Header3", footer="Footer3")
]



"""
def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(group_name="", header="", footer="")] + [
    Group(group_name=random_string("name", 10), header = random_string("Header", 20) , footer=random_string("Footer", 20))
    for i in range(5)
]
"""