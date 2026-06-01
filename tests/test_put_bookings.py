import allure
import requests

from models.booking import BookingDates, UpdateBookingModel

@allure.feature("API")
@allure.story("Update")
@allure.title('Успешное изменение')
def test_update_ok(booking_auth_client):
    bookingid = 1337
    fields = {
        'firstname':'Naruto',
        'lastname':'Uzumaki',
        'totalprice':111,
        'depositpaid':True,
        'bookingdates':BookingDates(checkin='2026-06-15', checkout='2026-06-20'),
        'additionalneeds':'ramen'
    }

    model = UpdateBookingModel(**fields)

    resp = booking_auth_client.put_booking(bookingid=bookingid, model=model)
    
    assert resp.status_code == requests.codes['ok']


@allure.feature("API")
@allure.story("Update")
@allure.title('Попытка изменения без авторизации')
def test_update_no_auth(booking_client):
    bookingid = 1337
    fields = {
        'firstname':'Naruto',
        'lastname':'Uzumaki',
        'totalprice':111,
        'depositpaid':True,
        'bookingdates':BookingDates(checkin='2026-06-15', checkout='2026-06-20'),
        'additionalneeds':'ramen'
    }

    model = UpdateBookingModel(**fields)

    resp = booking_client.put_booking(bookingid=bookingid, model=model)

    assert resp.status_code == requests.codes['forbidden']