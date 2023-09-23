import os
from model.contact import Contact
import random


def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
    old_contacts = db.get_contact_list()
    contact_db = random.choice(old_contacts)
    contact = Contact(firstname="new Vanya123")
    contact.id = contact_db.id
    contact.lastname = contact_db.lastname
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()

    for i, cn in enumerate(old_contacts):
        if cn.id == contact.id:
            # Выполняем замену атрибутов
            old_contacts[i] = contact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_modify_contact_Birthday(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vanya", bday="1", bmonth="January", byear="1980"))
    old_contacts = db.get_contact_list()
    contact = Contact(bday="22", bmonth="May", byear="1975")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    
    for i, cn in enumerate(old_contacts):
        if cn.id == contact.id:
            # Выполняем замену атрибутов
            old_contacts[i] = contact
    
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)