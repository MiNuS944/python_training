from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ConctactHelper

class Applicaton:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ConctactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destoy(self):
        self.wd.quit()