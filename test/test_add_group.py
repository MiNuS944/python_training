from model.group import Group


def test_add_group(app):    
    app.group.create(Group(name="tttetst123", header="sasdas", footer="gfdgf"))

def test_add_empty_group(app): 
    app.group.create(Group(name="", header="", footer=""))

