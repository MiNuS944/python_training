import os
from model.contact import Contact


def test_new_contact(app):
    app.contact.new(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov", 
                                   nickname="Ivan3000", photo= os.path.abspath("files/imya-ivan.jpg"), 
                                   title="QA", company="My Company", address="London, st.test 123", 
                                   tel_home="1234678", tel_mobile="81112223344", tel_work="+1234567", tel_fax="0987212", 
                                   email="ivan300@gmail.com", email2="ivan_300@gmail.com", email3="ivan_3000@gmail.com", 
                                   homepage="ivan.com", bday="1", bmonth="January", 
                                   byear="1980", aday="1", amonth="January", 
                                   ayear="2000", address2="London st.test 1 213", phone2="2134", 
                                   notes="Hello, world"
                                   ))
