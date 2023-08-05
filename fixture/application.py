from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Applicaton:
    
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
    
    def new_contact(self, contact):
        wd = self.wd
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
        wd.find_element(By.NAME, ("home")).send_keys(contact.tel_home)
        wd.find_element(By.NAME, ("mobile")).send_keys(contact.tel_mobile)
        wd.find_element(By.NAME, ("work")).send_keys(contact.tel_work)
        wd.find_element(By.NAME, ("fax")).send_keys(contact.tel_fax)
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
        self.return_home_page()    

    def return_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, ("home page")).click()

    def destoy(self):
        self.wd.quit()