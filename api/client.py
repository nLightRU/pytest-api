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
        return r.get(self.base_url + '/booking')
    
    def get_booking_id(self, _id: int):
        return r.get(self.base_url + '/booking/' + str(_id))
    
    def post_booking(self, model: CreateBookingModel):
        payload = model.model_dump()
        resp = r.post(self.base_url + '/booking', json=payload)
        return resp
    
    def put_booking(self, bookingid, model:UpdateBookingModel):
        url = self.base_url + f'/booking/{bookingid}'
        payload = model.model_dump()
        resp = r.put(url=url, cookies=self.auth_cookies, json=payload)
        return resp

    def patch_booking(self, _id, payload):
        ...
    
