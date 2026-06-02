import pytest

def test_auth(booking_client, auth_creds):
    booking_client.auth(username=auth_creds['username'], password=auth_creds['password'])

    assert booking_client.token != None

    booking_client.clear_auth()

@pytest.mark.skip
def test_auth_no_creds(booking_client):
    booking_client.auth()
    