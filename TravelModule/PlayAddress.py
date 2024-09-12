from Address import Address
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Float
from datetime import datetime


class PlayAddress(Address):
    id: Mapped[int] = mapped_column(primary_key=True)
    sight_name: Mapped[str] = mapped_column(String(30))
    ticket_prices: Mapped[float] = mapped_column(Float)
    start_time: Mapped[str] = mapped_column(String(20))

    def __init__(self, city, street: str, name: str, date: str, price: float):
        super(PlayAddress, self).__init__(city, street)
        self.name = name
        self.date = date
        self.price = price
