import random
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

def test_add_contacts_in_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="tttetst123"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
    
    old_groups = db.get_group_list() 
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_in_group(contact, group)
    old_contacts_in_group.append(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) == len(new_contacts_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(
        new_contacts_in_group, key=Contact.id_or_max)
    
    

