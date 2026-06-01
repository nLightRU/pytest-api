from api.client import BookingClient
import pytest


@pytest.fixture(scope='session')
def booking_client():
    return BookingClient()

@pytest.fixture(scope='session')
def booking_auth_client():
    client = BookingClient()
    client.auth()
    return client