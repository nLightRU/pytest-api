import allure
import pytest
import requests
from models.booking import BookingDates, CreateBookingModelNoField, BookingResponseModel

@allure.feature("API")
@allure.story("Create")
@allure.title('Успешное создание бронирования')
def test_create(booking_client, booking_sample_create_model):
    resp = booking_client.post_booking(model=booking_sample_create_model)

    resp_model = BookingResponseModel(**resp.json())
    
    assert resp.status_code == requests.codes['ok']
    assert resp_model.booking == booking_sample_create_model

@allure.feature("API")
@allure.story("Create")
@allure.title('Попытка создать без обязательного поля')
@pytest.mark.parametrize('missing_field', ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates'])
def test_booking_no_field(booking_client, missing_field):
    fields = {
        'firstname': 'Naruto',
        'lastname': 'Uzumaki',
        'totalprice': 111,
        'depositpaid': True,
        'bookingdates': BookingDates(checkin='2025-06-15',checkout='2025-06-20')
    }

    fields.pop(missing_field, None)

    model = CreateBookingModelNoField(**fields)

    resp = booking_client.post_booking(model=model)

    assert resp.status_code == requests.codes['internal_server_error']