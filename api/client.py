import os
from dotenv import load_dotenv
import requests as r

from models.booking import CreateBookingModel, UpdateBookingModel

load_dotenv()

class AuthenticationError(Exception):
    pass

class BookingClient:
    def __init__(self, timeout=10):
        self.base_url = os.getenv('BOOKING_BASE_URL')
        self.timeout = timeout
        self.token = None
        self.session = r.Session()
        self.session.headers.update({'Content-Type':'application/json'})
        self.auth_cookies = None
    
    def _make_url(self,bookingid: int | None = None):
        url = f'{self.base_url}/booking'

        if bookingid:
            url += f'/{bookingid}'
        
        return url

    def _do_auth_request(self, username:str, password:str):
        url = f'{self.base_url}/auth'
        creds = dict()
        if username:
            creds['username'] = username
        if password:
            creds['password'] = password

        return self.session.post(url=url, json=creds, timeout=self.timeout)

    def auth(self, username: str = None, password:str = None):
        """
            Авторизует клиента (получает и сохраняет токен).
            Выбрасывает ValueError, если не переданы учётные данные.
        """
        if not username:
            raise ValueError('missing username')
        if not password:
            raise ValueError('missing password')

        resp = self._do_auth_request(username=username, password=password)

        if resp.status_code != r.codes['ok']:
            raise AuthenticationError(
                f"Ошибка авторизации: {resp.status_code}, тело: {resp.text}"
            )
        
        data = resp.json()
        if "token" not in data:
            raise AuthenticationError("В ответе отсутствует поле 'token'")
        
        self.token = data['token']
        self.auth_cookies = {'token': self.token}

    def try_auth(self, username: str = None, password: str = None):
        '''
            Тестовый метод: выполняет запрос к /auth без сохранения токена
            и без проверок.
        '''
        return self._do_auth_request(username=username, password=password)

    def clear_auth(self):
        self.token = None
        self.auth_cookies = None

    def get_bookings(self):
        url = self._make_url()
        return self.session.get(url=url, timeout=self.timeout)
    
    def get_booking_id(self, _id: int):
        url = self._make_url(bookingid=_id)
        return self.session.get(url=url, timeout=self.timeout)
    
    def post_booking(self, model: CreateBookingModel):
        payload = model.model_dump()
        url = self._make_url()
        resp = self.session.post(url=url, json=payload, timeout=self.timeout)
        return resp
    
    def put_booking(self, bookingid, model:UpdateBookingModel):
        url = self._make_url(bookingid=bookingid)
        payload = model.model_dump()
        resp = self.session.put(url=url, cookies=self.auth_cookies, json=payload, timeout=self.timeout)
        return resp

    def patch_booking(self, bookingid: int, payload):
        ...
    
    def delete_booking(self, bookingid: int):
        url = self._make_url(bookingid=bookingid)
        resp = r.delete(url=url, cookies=self.auth_cookies, timeout=self.timeout)
        return resp
    
