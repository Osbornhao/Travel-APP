from datetime import datetime
from Address import Address
from sqlalchemy import String, DateTime
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime


class TravelProject:
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(30))
    date: Mapped[datetime] = mapped_column(DateTime)

    def __init__(self, time: datetime, address: Address):
        self.time = time
        self.address = address
