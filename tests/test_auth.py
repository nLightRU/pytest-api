import allure
import pytest
import requests

@allure.feature("API")
@allure.story("Auth")
@allure.title('Успешная авторизация')
def test_auth_ok(booking_client, auth_creds):
    booking_client.auth(username=auth_creds['username'], password=auth_creds['password'])
    
    assert booking_client.token is not None


@allure.feature("API")
@allure.story("Auth")
@allure.title('Авторизация без кредов')
def test_auth_no_creds(booking_client):
    resp = booking_client.try_auth(username=None, password=None)

    assert resp.status_code == requests.codes['ok']
    assert resp.json()['reason'] == 'Bad credentials'


@allure.feature("API")
@allure.story("Auth")
@allure.title('Авторизация с неправильными данными')
@pytest.mark.parametrize('invalid_field', ['username', 'password'])
def test_auth_invalid_field(booking_client, auth_creds, invalid_field):
    auth_creds[invalid_field] = 'xxx'
    resp = booking_client.try_auth(username=auth_creds['username'], password=auth_creds['password'])

    assert resp.status_code == requests.codes['ok']
    assert resp.json()['reason'] == 'Bad credentials'


@allure.feature("API")
@allure.story("Auth")
@allure.title('Авторизация без необходимого поля')
@pytest.mark.parametrize('missing_field', ['username', 'password'])
def test_auth_missing_field(booking_client, auth_creds, missing_field):
    auth_creds[missing_field] = None
    resp = booking_client.try_auth(
            username=auth_creds['username'],
            password=auth_creds['password']
    )

    assert resp.status_code == requests.codes['ok']
    assert resp.json()['reason'] == 'Bad credentials'
