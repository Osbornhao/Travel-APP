from Base import Base
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class City(Base):
    __tablename__= "city"
    id: Mapped[int] = mapped_column(primary_key=True)
    city_name: Mapped[str] = mapped_column(String(30))

    def __init__(self, countryarea: str):
        self.countryarea = countryarea
