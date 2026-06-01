import allure
import pytest

@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка статус кода")
def test_bookings(booking_client):
    resp = booking_client.get_bookings()
    assert resp.status_code == 200


@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка чтения бронирования по ID")
@pytest.mark.parametrize('booking_id', [1, 15])
def test_bookings_id(booking_client, booking_id):
    resp = booking_client.get_booking_id(str(booking_id))
    assert resp.status_code == 200


@allure.feature("API")
@allure.story("Read")
@allure.title("Проверка чтения c ID типа str")
@pytest.mark.parametrize('booking_id', ['abc'])
def test_booking_id_negative(booking_client, booking_id):
    resp = booking_client.get_booking_id(str(booking_id))
    assert resp.status_code == 404
    
    
