from model.contact import Contact
import random
import time

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id_contact(contact.id)
    #Добавил задержку т.к. у меня падает тест, данные в ДБ не успевают обновиться
    time.sleep(0.2)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)        

#def test_delete_all_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov"))
#    app.contact.delete_all_contacts()
#    assert app.contact.count() == 0       