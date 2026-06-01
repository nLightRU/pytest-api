import pytest
from models.booking import CreateBookingModel, BookingDates, CreateBookingModelNoField

def test_create_ok(booking_client):
    model = CreateBookingModel(
        firstname='Naruto',
        lastname='Uzumaki',
        totalprice=111,
        depositpaid=True,
        bookingdates=BookingDates(checkin='2026-06-15', checkout='2026-06-20'),
        addtionalneeds='ramen'
    )

    resp = booking_client.post_booking(model=model)

    assert resp.status_code == 200


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

    assert resp.status_code == 500