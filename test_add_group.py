# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        wd.find_element(By.NAME, ("user")).click()
        wd.find_element(By.NAME, ("user")).clear()
        wd.find_element(By.NAME, ("user")).send_keys("admin")
        wd.find_element(By.NAME, ("pass")).click()
        wd.find_element(By.NAME, ("pass")).clear()
        wd.find_element(By.NAME, ("pass")).send_keys("secret")
        wd.find_element(By.XPATH, ("//input[@value='Login']")).click()
    
    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, ("groups")).click()
    
    def create_group(self, wd):
        # init group creation
        wd.find_element(By.NAME, ("new")).click()
        # fill group form
        wd.find_element(By.NAME, ("group_name")).click()
        wd.find_element(By.NAME, ("group_name")).clear()
        wd.find_element(By.NAME, ("group_name")).send_keys("tttetst")
        wd.find_element(By.NAME, ("group_header")).click()
        wd.find_element(By.NAME, ("group_header")).clear()
        wd.find_element(By.NAME, ("group_header")).send_keys("asfsa")
        wd.find_element(By.NAME, ("group_footer")).click()
        wd.find_element(By.NAME, ("group_footer")).clear()
        wd.find_element(By.NAME, ("group_footer")).send_keys("gfdgdd")
        # submit group creation
        wd.find_element(By.NAME, ("submit")).click()
    
    def return_to_group_page(self, wd):
        wd.find_element(By.LINK_TEXT, ("group page")).click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, ("Logout")).click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_group_page(wd)
        self.logout(wd)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
