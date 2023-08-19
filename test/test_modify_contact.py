import os
from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    print(index)
    contact = Contact(firstname="new Vanya123")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_Birthday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vanya", bday="1", bmonth="January", byear="1980"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(bday="22", bmonth="May", byear="1975")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
