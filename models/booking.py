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
    additionalneeds: str | None = None


class BookingResponseModel(BaseModel):
    bookingid: int
    booking: CreateBookingModel


class CreateBookingModel(BookingModel):
    ...


class CreateBookingModelNoField(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    totalprice: int | None = None
    depositpaid: bool | None = None
    bookingdates: BookingDates | None = None
    addtionalneeds: str | None = None


class UpdateBookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int = Field(gt=0)
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None