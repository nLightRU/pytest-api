import pytest

def test_auth(booking_client):
    booking_client.auth()

    assert booking_client.token != None

    booking_client.clear_auth()

@pytest.mark.skip
def test_auth_no_creds(booking_client):
    ...