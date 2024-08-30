from Address import Address
class Restaurant(Address):
    def __init__(self,city,street:str,date:str,dish:str):
        super(Restaurant, self).__init__(city,street)
        self.date = date
        self.dish = dish