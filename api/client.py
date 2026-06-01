import os
from dotenv import load_dotenv
import requests as r

from models.booking import CreateBookingModel

load_dotenv()

class BookingClient:
    def __init__(self):
        self.base_url = os.getenv('BOOKING_BASE_URL')
    
    def get_bookings(self):
        return r.get(self.base_url + '/booking')
    
    def get_booking_id(self, _id: int):
        return r.get(self.base_url + '/booking/' + str(_id))
    
    def post_booking(self, model: CreateBookingModel):
        payload = model.model_dump()
        resp = r.post(self.base_url + '/booking',
            json=payload)
        return resp
    
    def put_booking(self, _id, payload):
        ...

    def patch_booking(self, _id, payload):
        ...
    
