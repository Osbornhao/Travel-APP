from City import City
from Transportation import Transportation
from TravelProject import TravelProject
from typing import List
from sqlalchemy import String, DateTime, Integer, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from Base import Base
from sqlalchemy.orm import relationship
from PlayAddress import PlayAddress
from TravelPlan_City import association_table


class TravelPlan(Base):
    __tablename__ = "travelplan"
    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(30))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    # city = relationship('City')
    play_address_id = mapped_column(ForeignKey('PlayAddress.id'))
    visit_day = mapped_column(Integer)
    city = relationship("City",
                        secondary=association_table)
    travelproject = relationship("TravelProject")

    def __init__(self, planName: str, start_time: datetime, end_time: datetime):
        self.plan_name = planName
        self.start_time = start_time
        self.end_time = end_time
        self.cityList = []
        self.transportationList = []
        self.travelProjectList = []


# sight1 = City(name='BeiJing', TravelName=[PlayAddress(
#     name='GuGong'), PlayAddress(name='TianTan')])
# sight2 = City(name='Shanghai', TravelName=[PlayAddress(
#     name='PuDong'), PlayAddress(name='HongQiao')])
