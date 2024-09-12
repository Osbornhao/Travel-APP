from Address import Address
from sqlalchemy import String, DateTime
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime


class Restaurant(Address):
    id: Mapped[int] = mapped_column(primary_key=True)
    cuisine_name: Mapped[str] = mapped_column(String(30))
    date: Mapped[datetime] = mapped_column(DateTime)

    def __init__(self, city, street: str, date: str, dish: str):
        super(Restaurant, self).__init__(city, street)
        self.date = date
        self.dish = dish
