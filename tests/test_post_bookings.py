import pytest
from models.booking import CreateBookingModel, BookingDates

def test_create_ok(booking_client):
    dates = BookingDates(
        checkin='2026-06-15',
        checkout='2026-06-20'
    )

    model = CreateBookingModel(
        firstname='Naruto',
        lastname='Uzumaki',
        totalprice=111,
        depositpaid=True,
        bookingdates=dates,
        addtionalneeds='ramen'
    )

    resp = booking_client.post_booking(model=model)

    assert resp.status_code == 200
