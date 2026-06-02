import os
from dotenv import load_dotenv
import datetime as dt
import pytest

from api.client import BookingClient
from models.booking import CreateBookingModel, BookingDates

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
def booking_sample_create_model():
    today = dt.date.today()

    start = today + dt.timedelta(days=10)
    end = today + dt.timedelta(days=20)

    checkin = start.strftime('%Y-%m-%d')
    checkout = end.strftime('%Y-%m-%d')

    fields = {
        'firstname': 'Naruto',
        'lastname': 'Uzumaki',
        'totalprice': 111,
        'depositpaid': True,
        'bookingdates': BookingDates(checkin=checkin,checkout=checkout)
    }

    model = CreateBookingModel(**fields)

    return model


@pytest.fixture(scope='function')
def booking_sample_update_model():
    today = dt.date.today()

    start = today + dt.timedelta(days=15)
    end = today + dt.timedelta(days=25)

    checkin = start.strftime('%Y-%m-%d')
    checkout = end.strftime('%Y-%m-%d')

    fields = {
        'firstname': 'Spike',
        'lastname': 'Spiegel',
        'totalprice': 222,
        'depositpaid': False,
        'bookingdates': BookingDates(checkin=checkin,checkout=checkout)
    }

    model = CreateBookingModel(**fields)

    return model
