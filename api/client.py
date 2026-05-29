import os
from dotenv import load_dotenv
import requests as r

load_dotenv()

class BookingClient:
    def __init__(self):
        self.base_url = os.getenv('BOOKING_BASE_URL')
    
    def get_booking_id(self, _id: int):
        return r.get(self.base_url + '/booking/' + str(_id))
    
    def get_bookings(self):
        return r.get(self.base_url + '/booking')
    
