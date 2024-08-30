from datetime import datetime
from Address import Address
class TravelProject:
    def __init__(self, time: datetime, address: Address):
        self.time = time
        self.address = address