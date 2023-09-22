from fixture.orm import ORMFixture
from model.group import Group

def test_1(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    try:
        l = db.get_contacts_not_in_group(Group(id="318"))
        for item in l:
            print(item)
        print(len(l))
    finally:
        pass
        #db.destroy()
