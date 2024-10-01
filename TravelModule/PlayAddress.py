from sqlalchemy import String, ForeignKey, Column, Integer
from Base import Base
from sqlalchemy.orm import relationship
from Address import Address
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Float
from datetime import datetime


class PlayAddress(Address):
    __tablename__ = "PlayAddress"
    # sight_name: Mapped[str] = mapped_column(String(30))
    ticket_prices: Mapped[float] = mapped_column(Float)
    start_time: Mapped[str] = mapped_column(String(20))
    # address = relationship('Address')
    city_id = Column(Integer, ForeignKey('city.id'))
    id = mapped_column(ForeignKey('Address.id'), primary_key=True)
    __mapper_args__ = {
        "polymorphic_identity": "PlayAddress",
    }

    def __init__(self, city, street: str, name: str, date: str, price: float, start_time: str):
        super(PlayAddress, self).__init__(city, street, name)
        # self.sight_name = name
        self.date = date
        self.ticket_prices = price
        self.start_time = start_time
