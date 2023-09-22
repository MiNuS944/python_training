from model.group import Group
import random

def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="tttetst123"))
    old_groups = db.get_group_list() 
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)  
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups     


def test_delete_all_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="tttetst123"))     
    app.group.delete_all_groups()
    assert len(db.get_group_list()) == 0
