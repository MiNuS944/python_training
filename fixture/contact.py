from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ConctactHelper:
    
    def __init__(self, app):
        self.app = app 

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, ("selected[]")).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name in ["bday", "bmonth", "aday", "amonth"]:
                Select(wd.find_element(By.NAME, (field_name))).select_by_visible_text(text)
            else:
                wd.find_element(By.NAME, (field_name)).clear()
                wd.find_element(By.NAME, (field_name)).send_keys(text)
    
    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        self.change_field_value("work", contact.tel_mobile)
        self.change_field_value("fax", contact.tel_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("aday", contact.aday)
        self.change_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
    
    def delete_first_contact(self):
        wd = self.app.wd
        self.home_page()
        self.select_first_contact()
        self.submit_deletion()
        wd.switch_to.alert.accept()
    
    def delete_all_contacts(self):
        wd = self.app.wd
        self.home_page()
        # select all contacts
        wd.find_element(By.ID, ("MassCB")).click()
        self.submit_deletion()
        wd.switch_to.alert.accept()

    def submit_deletion(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element(By.LINK_TEXT, ("add new")).click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, ("submit")).click()
        self.return_home_page()
    
    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.home_page()
        # open modification form
        wd.find_element(By.CSS_SELECTOR, 'img[alt="Edit"]').click()
        self.fill_contact_form(contact)
        # update contact
        wd.find_element(By.NAME, ("update")).click()
        self.return_home_page()
   
    def count(self):
       wd = self.app.wd
       self.home_page()
       return len(wd.find_elements(By.NAME, ("selected[]")))  
    
    def home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, ("home")).click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, ("home page")).click()