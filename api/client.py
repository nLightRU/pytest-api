import os
from dotenv import load_dotenv
import requests as r

from models.booking import CreateBookingModel, UpdateBookingModel

load_dotenv()

class BookingClient:
    def __init__(self):
        self.base_url = os.getenv('BOOKING_BASE_URL')
        self.token = None
        self.auth_cookies = None
    
    def _make_url(self,bookingid: int | None = None):
        url = f'{self.base_url}/booking'

        if bookingid:
            url += f'/{bookingid}'
        
        return url

    def auth(self):
        url = self.base_url + '/auth'
        username, password = os.getenv('AUTH_USERNAME'), os.getenv('AUTH_PASSWORD')
        creds = {
            'username': username,
            'password': password
        }
        self.token = r.post(url=url, json=creds).json()['token']
        self.auth_cookies = {'token': self.token}

    def clear_auth(self):
        self.token = None
        self.auth_cookies = None

    def get_bookings(self):
        url = self._make_url()
        return r.get(url=url)
    
    def get_booking_id(self, _id: int):
        url = self._make_url(bookingid=_id)
        return r.get(url=url)
    
    def post_booking(self, model: CreateBookingModel):
        payload = model.model_dump()
        url = self._make_url()
        resp = r.post(url=url, json=payload)
        return resp
    
    def put_booking(self, bookingid, model:UpdateBookingModel):
        url = self._make_url(bookingid=bookingid)
        payload = model.model_dump()
        resp = r.put(url=url, cookies=self.auth_cookies, json=payload)
        return resp

    def patch_booking(self, bookingid: int, payload):
        ...
    
    def delete_booking(self, bookingid: int):
        url = self._make_url(bookingid=bookingid)
        resp = r.delete(url=url, cookies=self.auth_cookies)
        return resp
    
