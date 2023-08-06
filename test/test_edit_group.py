from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    # create group for edit
    app.group.create(Group(name="tttetst123", header="sasdas", footer="gfdgf"))    
    app.group.edit_first_group(Group(name="test_edit", header="edit123", footer="gfdgf"))   
    app.session.logout()