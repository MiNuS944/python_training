from model.contact import Contact
import os.path
import random
import string
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_numbers(maxlen):
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_emails(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@ru.com"

testdata = [
    Contact(firstname=random_string("Vanya", 10), middlename=random_string("Ivan", 10), lastname=random_string("Ivanov", 10),
            nickname=random_string("Ivan3000", 10), photo=os.path.abspath("files/imya-ivan.jpg"),
            title=random_string("QA", 10), company=random_string("My Company", 10), address=random_string("London,", 10),
            tel_home=random_numbers(10), tel_mobile=random_numbers(10), tel_work=random_numbers(10), 
            tel_fax=random_numbers(10),email=random_emails(10), email2=random_emails(10), bday="1", 
            bmonth="January", byear="1980", aday="1", amonth="January", ayear="2000", 
            email3=random_emails(10), homepage=random_string("ivan.", 20), address2=random_string("London", 10), 
            phone2=random_numbers(10), notes=random_string("Hello,", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
        
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))