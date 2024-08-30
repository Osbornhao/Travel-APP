from Address import Address
class RentalCarCompany(Address):
    def __init__(self,city,street:str,companyname:str,summary:str,companyaddress:str,workingtime:str):
        super(RentalCarCompany, self).__init__(city,street)
        self.companyname = companyname
        self.summary = summary
        self.companyaddress = companyaddress
        self.workingtime = workingtime