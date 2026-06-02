import pytest
import requests

@pytest.mark.skip
def test_delete(booking_auth_client):
    bookingid = 1337
    resp = booking_auth_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['ok']


@pytest.mark.skip
def test_delete_404(booking_auth_client):
    bookingid = 123
    resp = booking_auth_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['ok']

    resp = booking_auth_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['not_found']


def test_delete_no_auth(booking_client):
    bookingid = 1337
    resp = booking_client.delete_booking(bookingid=bookingid)
    assert resp.status_code == requests.codes['forbidden'] 