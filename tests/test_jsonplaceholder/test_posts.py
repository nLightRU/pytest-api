import requests as r

def test_post_id():
    base_url = 'https://jsonplaceholder.typicode.com'
    path = '/posts/1'
    resp = r.get(base_url + path)
    assert resp.status_code == 200