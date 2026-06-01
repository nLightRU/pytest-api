from pydantic import BaseModel, Field
from datetime import date

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int = Field(gt=0)
    depositpaid: bool
    bookingdates: BookingDates
    addtionalneeds: str | None = None


class BookingResponseModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int = Field(gt=0)
    depositpaid: bool
    bookingdates: BookingDates
    addtionalneed: str | None = None


class CreateBookingModel(BookingModel):
    ...