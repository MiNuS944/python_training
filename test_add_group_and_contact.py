# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest, time

from group import Group
from contact import Contact

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element(By.NAME, ("user")).click()
        wd.find_element(By.NAME, ("user")).clear()
        wd.find_element(By.NAME, ("user")).send_keys(username)
        wd.find_element(By.NAME, ("pass")).click()
        wd.find_element(By.NAME, ("pass")).clear()
        wd.find_element(By.NAME, ("pass")).send_keys(password)
        wd.find_element(By.XPATH, ("//input[@value='Login']")).click()
    
    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, ("groups")).click()
    
    def create_group(self, wd, group):
        # init group creation
        wd.find_element(By.NAME, ("new")).click()
        # fill group form
        wd.find_element(By.NAME, ("group_name")).click()
        wd.find_element(By.NAME, ("group_name")).clear()
        wd.find_element(By.NAME, ("group_name")).send_keys(group.name)
        wd.find_element(By.NAME, ("group_header")).click()
        wd.find_element(By.NAME, ("group_header")).clear()
        wd.find_element(By.NAME, ("group_header")).send_keys(group.header)
        wd.find_element(By.NAME, ("group_footer")).click()
        wd.find_element(By.NAME, ("group_footer")).clear()
        wd.find_element(By.NAME, ("group_footer")).send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, ("submit")).click()
    
    def return_to_group_page(self, wd):
        wd.find_element(By.LINK_TEXT, ("group page")).click()

    def return_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, ("home page")).click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, ("Logout")).click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="tttetst123", header="sasdas", footer="gfdgf"))
        self.return_to_group_page(wd)
        self.logout(wd)
    
    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.logout(wd)

    def new_contact(self, wd, contact):
        # init contact creation
        wd.find_element(By.LINK_TEXT, ("add new")).click()
        wd.find_element(By.NAME, ("firstname")).send_keys(contact.firstname)
        wd.find_element(By.NAME, ("middlename")).send_keys(contact.middlename)
        wd.find_element(By.NAME, ("lastname")).send_keys(contact.lastname)
        wd.find_element(By.NAME, ("nickname")).send_keys(contact.nickname)
        wd.find_element(By.NAME, ("photo")).send_keys(contact.photo)
        wd.find_element(By.NAME, ("title")).send_keys(contact.title)
        wd.find_element(By.NAME, ("company")).send_keys(contact.company)
        wd.find_element(By.NAME, ("address")).send_keys(contact.address)
        wd.find_element(By.NAME, ("home")).send_keys(contact.home)
        wd.find_element(By.NAME, ("mobile")).send_keys(contact.mobile)
        wd.find_element(By.NAME, ("work")).send_keys(contact.work)
        wd.find_element(By.NAME, ("fax")).send_keys(contact.fax)
        wd.find_element(By.NAME, ("email")).send_keys(contact.email)
        wd.find_element(By.NAME, ("email2")).send_keys(contact.email2)
        wd.find_element(By.NAME, ("email3")).send_keys(contact.email3)
        wd.find_element(By.NAME, ("homepage")).send_keys(contact.homepage)
        Select(wd.find_element(By.NAME, ("bday"))).select_by_visible_text(contact.bday)
        Select(wd.find_element(By.NAME, ("bmonth"))).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, ("byear")).send_keys(contact.byear)
        Select(wd.find_element(By.NAME, ("aday"))).select_by_visible_text(contact.aday)
        Select(wd.find_element(By.NAME, ("amonth"))).select_by_visible_text(contact.amonth)
        wd.find_element(By.NAME, ("ayear")).send_keys(contact.ayear)
        wd.find_element(By.NAME, ("address2")).send_keys(contact.address2)
        wd.find_element(By.NAME, ("phone2")).send_keys(contact.phone2)
        wd.find_element(By.NAME, ("notes")).send_keys(contact.notes)
        # submit contact creation
        wd.find_element(By.NAME, ("submit")).click()

    def test_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        # Do not forget to specify the correct PATH to upload photo
        self.new_contact(wd, Contact(firstname="Vanya", middlename="Ivan", lastname="Ivanov", 
                                   nickname="Ivan3000", photo="C:\\1My_Python\\python_lessons\\python_training\\imya-ivan.jpg", 
                                   title="QA", company="My Company", address="London, st.test 123", 
                                   home="1234678", mobile="81112223344", work="+1234567", fax="0987212", 
                                   email="ivan300@gmail.com", email2="ivan_300@gmail.com", email3="ivan_3000@gmail.com", 
                                   homepage="ivan.com", bday="1", bmonth="January", 
                                   byear="1980", aday="1", amonth="January", 
                                   ayear="2000", address2="London st.test 1 213", phone2="2134", 
                                   notes="Hello, world"
                                   ))
        self.return_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
