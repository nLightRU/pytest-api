import pytest

def test_bookings(booking_client):
    resp = booking_client.get_bookings()
    assert resp.status_code == 200


@pytest.mark.parametrize('booking_id', [1, 15])
def test_bookings_id(booking_client, booking_id):
    resp = booking_client.get_booking_id(str(booking_id))
    assert resp.status_code == 200


@pytest.mark.parametrize('booking_id', ['abc'])
def test_booking_id_negative(booking_client, booking_id):
    resp = booking_client.get_booking_id(str(booking_id))
    assert resp.status_code == 404
    
    
