from City import City
from sqlalchemy import String, Column, Integer, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship, declared_attr
from Base import Base


class Address(Base):
    #  __abstract__ = True
    __tablename__ = "Address"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    street: Mapped[str] = mapped_column(String(80))
    city_id = Column(Integer, ForeignKey('city.id'))
    type: Mapped[str] = mapped_column(String(30))

    __mapper_args__ = {
        "polymorphic_identity": "Address",
        "polymorphic_on": "type",
    }

    def __init__(self, city: City, street: str, name: str):
        self.city = city
        self.street = street
        self.name = name

    @declared_attr
    def city(cls):
        return relationship("City")
