import os
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret") 
    # create contact for edit
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
    app.contact.edit_first_contact(Contact(firstname="Vanya123", middlename="Ivan123", lastname="Ivanov123", 
                                   nickname="Ivan123", photo= os.path.abspath("files/imya-ivan.jpg"), 
                                   title="QA123", company="My Company123", address="London123, st.test 123", 
                                   tel_home="1234678123", tel_mobile="81112223123", tel_work="+1234123", tel_fax="0987123", 
                                   email="ivan123@gmail.com", email2="ivan_123@gmail.com", email3="ivan_123@gmail.com", 
                                   homepage="ivan123.com", bday="2", bmonth="February", 
                                   byear="1981", aday="2", amonth="February", 
                                   ayear="2123", address2="London123 st.test 1 213", phone2="2134123", 
                                   notes="Hello, world123"
                                   ))
    app.session.logout()