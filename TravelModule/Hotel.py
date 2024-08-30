from datetime import datetime
from Address import Address
class Hotel(Address):
    def __init__(self,city,street:str,date:datetime,price:float):
        super(Hotel, self).__init__(city,street)
        self.date = date
        self.price = price