from City import City
from Transportation import Transportation
from TravelProject import TravelProject
from typing import List
from sqlalchemy import String, DateTime, Integer ,ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from Base import Base
from sqlalchemy.orm import relationship
from PlayAddress import PlayAddress


class TravelPlan(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(30))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
    city = relationship('City')
    play_address_id = mapped_column(ForeignKey('play_address.id'))
    visit_day = mapped_column(Integer)

    def __init__(self, planName: List[str]):
        self.planName = planName
        self.cityList = []
        self.transportationList = []
        self.travelProjectList = []


# sight1 = City(name='BeiJing', TravelName=[PlayAddress(
#     name='GuGong'), PlayAddress(name='TianTan')])
# sight2 = City(name='Shanghai', TravelName=[PlayAddress(
#     name='PuDong'), PlayAddress(name='HongQiao')])