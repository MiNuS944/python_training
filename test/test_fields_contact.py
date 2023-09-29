import re
from model.contact import Contact
from random import randrange


def test_fields_contact_on_home_page_with_edit_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov",
                                   tel_home = "+89991", email="sssiv@tu.com"))
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact_from_home_page = all_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_fields_contact_on_home_page_with_db(app, db):
    contacts_on_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_list_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact_from_home_page in contacts_on_home_page:
        for contact_from_db in contacts_list_db:
            if contact_from_home_page.id == contact_from_db.id:
                assert contact_from_home_page.lastname == contact_from_db.lastname
                assert contact_from_home_page.firstname == contact_from_db.firstname
                assert contact_from_home_page.address == contact_from_db.address
                assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), 
                                filter(lambda x: x is not None, 
                                        [contact.tel_home, contact.tel_mobile, contact.tel_work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None, 
                                        [contact.email, contact.email2, contact.email3])))


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#
#    assert contact_from_view_page.tel_home == contact_from_edit_page.tel_home
#    assert contact_from_view_page.tel_mobile == contact_from_edit_page.tel_mobile
#    assert contact_from_view_page.tel_work == contact_from_edit_page.tel_work
#    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2
