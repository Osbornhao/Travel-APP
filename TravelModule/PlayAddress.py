from Address import Address
class PlayAddress(Address):
    def __init__(self,city,street:str,name:str,date:str,price:float):
        super(PlayAddress, self).__init__(city,street)
        self.name = name
        self.date = date
        self.price = price