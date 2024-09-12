from datetime import datetime
from Address import Address
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Float, DateTime


class Hotel(Address):
    id: Mapped[int] = mapped_column(primary_key=True)
    prices: Mapped[float] = mapped_column(Float)
    date: Mapped[datetime] = mapped_column(DateTime)

    def __init__(self, city, street: str, date: datetime, price: float):
        super(Hotel, self).__init__(city, street)
        self.date = date
        self.price = price
