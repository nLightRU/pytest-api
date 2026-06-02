import os
from dotenv import load_dotenv
import pytest

from api.client import BookingClient
from models.booking import CreateBookingModel

load_dotenv()

@pytest.fixture(scope='session')
def auth_creds():
    return {
        'username': os.getenv('AUTH_USERNAME'),
        'password': os.getenv('AUTH_PASSWORD')
    }


@pytest.fixture(scope='session')
def booking_auth_client():
    auth_creds = {
        'username': os.getenv('AUTH_USERNAME'),
        'password': os.getenv('AUTH_PASSWORD')
    }
    client = BookingClient(timeout=20)
    client.auth(username=auth_creds['username'], password=auth_creds['password'])
    return client


@pytest.fixture(scope='function')
def booking_client():
    return BookingClient(timeout=20)


@pytest.fixture(scope='function')
def booking_model():
    return 



