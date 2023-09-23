import random
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

def test_del_contacts_in_group(app, db_orm):

    if len(db_orm.get_group_list()) == 0:
        app.group.create(Group(name="tttetst123"))
    if len(db_orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
    old_groups = db_orm.get_group_list() 
    old_contacts = db_orm.get_contact_list()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    old_contacts_in_group = db_orm.get_contacts_in_group(group)
    #Проверяем есть ли в группе контакты, если нет, то добавляем контакт в группу
    if len(old_contacts_in_group) == 0:
        app.contact.add_contact_in_group(contact, group)
        old_contacts_in_group = db_orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.del_contact_in_group(contact, group)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = db_orm.get_contacts_in_group(group)
    assert len(old_contacts_in_group) == len(new_contacts_in_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(
        new_contacts_in_group, key=Contact.id_or_max)