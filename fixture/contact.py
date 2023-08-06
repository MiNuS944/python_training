from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ConctactHelper:
    
    def __init__(self, app):
        self.app = app
    
    def new(self, contact):
        wd = self.app.wd
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

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element(By.NAME, ("selected[]")).click()
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        wd.switch_to.alert.accept()
    
    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element(By.ID, ("MassCB")).click()
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select edit first contact
        wd.find_element(By.CSS_SELECTOR, 'img[alt="Edit"]').click()
        # edit contact form
        wd.find_element(By.NAME, ("firstname")).clear()
        wd.find_element(By.NAME, ("firstname")).send_keys(contact.firstname)
        wd.find_element(By.NAME, ("middlename")).clear()
        wd.find_element(By.NAME, ("middlename")).send_keys(contact.middlename)
        wd.find_element(By.NAME, ("lastname")).clear()
        wd.find_element(By.NAME, ("lastname")).send_keys(contact.lastname)
        wd.find_element(By.NAME, ("nickname")).clear()
        wd.find_element(By.NAME, ("nickname")).send_keys(contact.nickname)
        wd.find_element(By.NAME, ("photo")).send_keys(contact.photo)
        wd.find_element(By.NAME, ("title")).clear()
        wd.find_element(By.NAME, ("title")).send_keys(contact.title)
        wd.find_element(By.NAME, ("company")).clear()
        wd.find_element(By.NAME, ("company")).send_keys(contact.company)
        wd.find_element(By.NAME, ("address")).clear()
        wd.find_element(By.NAME, ("address")).send_keys(contact.address)
        wd.find_element(By.NAME, ("home")).clear()
        wd.find_element(By.NAME, ("home")).send_keys(contact.tel_home)
        wd.find_element(By.NAME, ("mobile")).clear()
        wd.find_element(By.NAME, ("mobile")).send_keys(contact.tel_mobile)
        wd.find_element(By.NAME, ("work")).clear()
        wd.find_element(By.NAME, ("work")).send_keys(contact.tel_work)
        wd.find_element(By.NAME, ("fax")).clear()
        wd.find_element(By.NAME, ("fax")).send_keys(contact.tel_fax)
        wd.find_element(By.NAME, ("email")).clear()
        wd.find_element(By.NAME, ("email")).send_keys(contact.email)
        wd.find_element(By.NAME, ("email2")).clear()
        wd.find_element(By.NAME, ("email2")).send_keys(contact.email2)
        wd.find_element(By.NAME, ("email3")).clear()
        wd.find_element(By.NAME, ("email3")).send_keys(contact.email3)
        wd.find_element(By.NAME, ("homepage")).clear()
        wd.find_element(By.NAME, ("homepage")).send_keys(contact.homepage)
        Select(wd.find_element(By.NAME, ("bday"))).select_by_visible_text(contact.bday)
        Select(wd.find_element(By.NAME, ("bmonth"))).select_by_visible_text(contact.bmonth)
        wd.find_element(By.NAME, ("byear")).clear()
        wd.find_element(By.NAME, ("byear")).send_keys(contact.byear)
        Select(wd.find_element(By.NAME, ("aday"))).select_by_visible_text(contact.aday)
        Select(wd.find_element(By.NAME, ("amonth"))).select_by_visible_text(contact.amonth)
        wd.find_element(By.NAME, ("ayear")).clear()
        wd.find_element(By.NAME, ("ayear")).send_keys(contact.ayear)
        wd.find_element(By.NAME, ("address2")).clear()
        wd.find_element(By.NAME, ("address2")).send_keys(contact.address2)
        wd.find_element(By.NAME, ("phone2")).clear()
        wd.find_element(By.NAME, ("phone2")).send_keys(contact.phone2)
        wd.find_element(By.NAME, ("notes")).clear()
        wd.find_element(By.NAME, ("notes")).send_keys(contact.notes)
        # update contact
        wd.find_element(By.NAME, ("update")).click()
        self.return_home_page()   

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, ("home page")).click()