import allure
import pytest
import requests

@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка статус кода")
def test_bookings(booking_client):
    resp = booking_client.get_bookings()
    assert resp.status_code == 200


@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка чтения бронирования по ID")
def test_bookings_id(booking_auth_client, booking_sample_create_model):
    resp = booking_auth_client.post_booking(booking_sample_create_model)
    if resp.status_code != requests.codes['ok']:
        raise Exception()

    bookingid = resp.json()['bookingid']
    resp = booking_auth_client.get_booking_id(bookingid)
    assert resp.status_code == 200


@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка чтения c ID типа str")
@pytest.mark.parametrize('booking_id', ['abc'])
def test_booking_id_negative(booking_client, booking_id):
    resp = booking_client.get_booking_id(booking_id)
    assert resp.status_code == 404


@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка чтения по несуществующему ID")
def test_get_booking_not_exists(booking_client):
    bookingid = 99999
    resp = booking_client.get_booking_id(bookingid)
    assert resp.status_code == 404
