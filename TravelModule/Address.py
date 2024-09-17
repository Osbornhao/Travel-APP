from City import City
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from Base import Base


class Address(Base):
    __tablename__ = "Address"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    city: Mapped[City] = mapped_column(String(30))
    street: Mapped[str] = mapped_column(String(80))

    def __init__(self, city: City, street: str):
        self.city = city
        self.street = street