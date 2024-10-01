from datetime import datetime
from Address import Address
from sqlalchemy import String, DateTime, Column, Integer, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from datetime import datetime
from Base import Base


class TravelProject(Base):
    __tablename__ = "TravelProject"
    id: Mapped[int] = mapped_column(primary_key=True)
    # address: Mapped[Address] = mapped_column((30))
    date: Mapped[datetime] = mapped_column(DateTime)
    travelplan = Column(Integer, ForeignKey('travelplan.id'))
    address = relationship("Address", uselist=False)
    address_id = Column(Integer, ForeignKey('Address.id'))

    def __init__(self, date: datetime, address: Address, travelplan: int):
        self.date = date
        self.address = address
        self.travelplan = travelplan
