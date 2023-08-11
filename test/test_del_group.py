import pytest

def test_delete_first_group(app):   
    app.group.delete_first_group()       

@pytest.mark.skipif(reason="Not needed yet")
def test_delete_all_group(app):     
    app.group.delete_all_groups()       