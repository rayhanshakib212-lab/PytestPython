import pytest


@pytest.fixture(scope='session')
def user_credentials(request):#request is a global parameter that allow global and local parameters
    return request.param