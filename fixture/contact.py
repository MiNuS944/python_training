import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from model.contact import Contact

class ConctactHelper:
    
    def __init__(self, app):
        self.app = app 

    def home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") or wd.current_url.endswith("addressbook/") and 
                len(wd.find_elements(By.CSS_SELECTOR, 'input[value="Send e-Mail"]')) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()
    
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click() 
    
    def select_contact_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.CSS_SELECTOR, 'img[alt="Edit"]')[index].click()
    
    def select_contact_edit_by_id(self, id):
        wd = self.app.wd
        contact = wd.find_element(By.CSS_SELECTOR, "tr:has(input[value='%s'])" % id)
        contact.find_element(By.CSS_SELECTOR, 'img[alt="Edit"]').click()
        
    def select_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.CSS_SELECTOR, 'img[alt="Details"]')[index].click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name in ["bday", "bmonth", "aday", "amonth"]:
                Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)
            else:
                wd.find_element(By.NAME, field_name).clear()
                wd.find_element(By.NAME, field_name).send_keys(text)
    
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
        self.change_field_value("mobile", contact.tel_mobile)
        self.change_field_value("work", contact.tel_work)
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
    
    def delete_by_index_contact(self, index):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_index(index)
        self.submit_deletion()
        wd.switch_to.alert.accept()
        self.contact_cache = None
    
    def delete_first_contact(self):
        self.delete_by_index_contact(0)
    
    def delete_all_contacts(self):
        wd = self.app.wd
        self.home_page()
        # select all contacts
        wd.find_element(By.ID, "MassCB").click()
        self.submit_deletion()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def submit_deletion(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_home_page()
        self.contact_cache = None
    
    def modify_first_contact(self, new_data_contact):
        self.modify_contact_by_index(0, new_data_contact)

    def modify_contact_by_index(self, index, new_data_contact):
        wd = self.app.wd
        self.home_page()
        # open modification form
        self.select_contact_edit_by_index(index)
        self.fill_contact_form(new_data_contact)
        # update contact
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_data_contact):
        wd = self.app.wd
        self.home_page()
        # open modification form
        self.select_contact_edit_by_id(id)
        self.fill_contact_form(new_data_contact)
        # update contact
        wd.find_element(By.NAME, "update").click()
        self.return_home_page()
        self.contact_cache = None
   
    def count(self):
       wd = self.app.wd
       self.home_page()
       return len(wd.find_elements(By.NAME, "selected[]"))  

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    contact_cache = None     

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, 'tr:has(td.center)'):
                tds = element.find_elements(By.TAG_NAME, "td")
                text_last_name = tds[1].text
                text_first_name = tds[2].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                text_aaddress = tds[3].text
                all_emails = tds[4].text
                all_phones = tds[5].text
                self.contact_cache.append(Contact(firstname=text_first_name, lastname=text_last_name, id=id, 
                                                  all_phones_from_home_page=all_phones, address=text_aaddress,
                                                  all_emails_from_home_page=all_emails))
        
        return list(self.contact_cache)

        
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.home_page()
        self.select_contact_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        tel_home = wd.find_element(By.NAME, "home").get_attribute("value")
        tel_mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        tel_work = wd.find_element(By.NAME, "work").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, 
                       address = address, tel_home=tel_home, tel_mobile=tel_mobile,
                        tel_work= tel_work, phone2=phone2, email=email,
                        email2=email2, email3=email3)
    
    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.home_page()
        self.select_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        tel_home = re.search("H: (.*)", text).group(1)
        tel_mobile = re.search("M: (.*)", text).group(1)
        tel_work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(tel_home=tel_home, tel_mobile=tel_mobile,
                        tel_work= tel_work, phone2=phone2)
    

    def delete_by_id_contact(self, id):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_id(id)
        self.submit_deletion()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def add_contact_in_group(self, contact, group):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_id(contact.id)
        Select(wd.find_element(By.NAME, 'to_group')).select_by_value(group.id)
        wd.find_element(By.CSS_SELECTOR, "input[value='Add to']").click()
        wd.find_element(By.PARTIAL_LINK_TEXT, "group page").click()
    
    def del_contact_in_group(self, contact, group):
        wd = self.app.wd
        self.home_page()
        Select(wd.find_element(By.NAME, 'group')).select_by_value(group.id)
        self.select_contact_by_id(contact.id)
        wd.find_element(By.NAME, "remove").click()
        wd.find_element(By.PARTIAL_LINK_TEXT, "group page").click()