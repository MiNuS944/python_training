from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="tttetst123"))
    old_groups = db.get_group_list()
    group_db = random.choice(old_groups)
    group = Group(name="new group")
    group.id = group_db.id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups.remove(group_db)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="sasdas"))
    old_groups = db.get_group_list() 
    group = Group(header="New header")
    group.name = old_groups[0].name
    group.id = old_groups[0].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups.remove(old_groups[0])
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)  
    