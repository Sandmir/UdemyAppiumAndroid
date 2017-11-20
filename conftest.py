from fixture.application import Application
import pytest


# fixture for user mode
@pytest.fixture(scope='module')
def appLogin(request):
    fixture = Application()
    fixture.session.login()
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

#  general fixture
@pytest.fixture(scope='function')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


