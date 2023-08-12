import os
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
    app.contact.modify_first_contact(Contact(firstname="new Vanya123"))

def test_modify_contact_Birthday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vanya", bday="1", bmonth="January", byear="1980"))
    app.contact.modify_first_contact(Contact(bday="22", bmonth="May", byear="1975"))