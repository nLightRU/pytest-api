import allure
import requests

@allure.feature("API")
@allure.story("Delete")
@allure.title("Успешное удаление")
def test_delete(booking_auth_client, booking_sample_create_model):
    resp = booking_auth_client.post_booking(booking_sample_create_model)
    assert resp.status_code == requests.codes['ok']

    bookingid = resp.json()['bookingid']
    resp = booking_auth_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['created']


@allure.feature("API")
@allure.story("Delete")
@allure.title("Повторное удаление возвращает ошибку")
def test_delete_twice_404(booking_auth_client, booking_sample_create_model):
    resp = booking_auth_client.post_booking(booking_sample_create_model)
    bookingid = resp.json()['bookingid']

    resp = booking_auth_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['created']

    resp = booking_auth_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['method_not_allowed']


@allure.feature("API")
@allure.story("Delete")
@allure.title("Попытка удалить без авторизации")
def test_delete_no_auth(booking_client):
    bookingid = 1337
    resp = booking_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['forbidden'] 


@allure.feature("API")
@allure.story("Delete")
@allure.title("Успешное удаление")
def test_delete_not_existed(booking_auth_client):
    bookingid = 99999
    resp = booking_auth_client.delete_booking(bookingid)
    assert resp.status_code == requests.codes['method_not_allowed']