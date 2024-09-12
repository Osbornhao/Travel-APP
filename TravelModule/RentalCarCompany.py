from Address import Address
from sqlalchemy import String
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class RentalCarCompany(Address):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(60))
    start_time: Mapped[str] = mapped_column(String(20))

    def __init__(self, city, street: str, companyname: str, summary: str, companyaddress: str, workingtime: str):
        super(RentalCarCompany, self).__init__(city, street)
        self.companyname = companyname
        self.summary = summary
        self.companyaddress = companyaddress
        self.workingtime = workingtime
