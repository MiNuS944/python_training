# -*- coding: utf-8 -*-
import time, os
import pytest

from model.group import Group
from model.contact import Contact
from fixture.application import Applicaton


@pytest.fixture
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destoy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")       
    app.create_group(Group(name="tttetst123", header="sasdas", footer="gfdgf"))        
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")   
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.new_contact(Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov", 
                                   nickname="Ivan3000", photo= os.path.abspath("files/imya-ivan.jpg"), 
                                   title="QA", company="My Company", address="London, st.test 123", 
                                   tel_home="1234678", tel_mobile="81112223344", tel_work="+1234567", tel_fax="0987212", 
                                   email="ivan300@gmail.com", email2="ivan_300@gmail.com", email3="ivan_3000@gmail.com", 
                                   homepage="ivan.com", bday="1", bmonth="January", 
                                   byear="1980", aday="1", amonth="January", 
                                   ayear="2000", address2="London st.test 1 213", phone2="2134", 
                                   notes="Hello, world"
                                   ))
    app.session.logout()

