import os
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_numbers(maxlen):
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_emails(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@ru.com"

testdata = [
    Contact(firstname=random_string("Vanya", 10), middlename=random_string("Ivan", 10), lastname=random_string("Ivanov", 10),
            nickname=random_string("Ivan3000", 10), photo=os.path.abspath("files/imya-ivan.jpg"),
            title=random_string("QA", 10), company=random_string("My Company", 10), address=random_string("London,", 10),
            tel_home=random_numbers(10), tel_mobile=random_numbers(10), tel_work=random_numbers(10), 
            tel_fax=random_numbers(10),email=random_emails(10), email2=random_emails(10), bday="1", 
            bmonth="January", byear="1980", aday="1", amonth="January", ayear="2000", 
            email3=random_emails(10), homepage=random_string("ivan.", 20), address2=random_string("London", 10), 
            phone2=random_numbers(10), notes=random_string("Hello,", 20))
    for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
