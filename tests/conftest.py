from dotenv import load_dotenv
import os
import pytest
from api.client import BookingClient

load_dotenv()

@pytest.fixture(scope='session')
def auth_creds():
    return {
        'username': os.getenv('AUTH_USERNAME'),
        'password': os.getenv('AUTH_PASSWORD')
    }


@pytest.fixture(scope='function')
def booking_client():
    return BookingClient()


@pytest.fixture(scope='session')
def booking_auth_client():
    auth_creds = {
        'username': os.getenv('AUTH_USERNAME'),
        'password': os.getenv('AUTH_PASSWORD')
    }
    client = BookingClient()
    client.auth(username=auth_creds['username'], password=auth_creds['password'])
    return client
