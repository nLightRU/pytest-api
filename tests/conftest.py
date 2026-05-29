from api.client import BookingClient
import pytest


@pytest.fixture(scope='session')
def booking_client():
    return BookingClient()