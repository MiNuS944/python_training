import pytest
from fixture.application import Applicaton


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Applicaton()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Applicaton()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destoy()
    request.addfinalizer(fin)
    return fixture