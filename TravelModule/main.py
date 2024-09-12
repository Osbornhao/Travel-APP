from Address import Address
from Hotel import Hotel
from datetime import datetime
from PlayAddress import PlayAddress
from RentalCarCompany import RentalCarCompany
from Restaurant import Restaurant
from TravelPlan import TravelPlan


# address1 = Address("Beijing","BoWuGuan")
#
# hotel1 = Hotel(address1.city,address1.street,datetime.now(),20)
#
# name="nowuguan"
# PlayAddress1 = PlayAddress(address1.city,address1.street,name,datetime.now(),160)
#
# # RentalCarCompany1 = RentalCarCompany(address1.city,address1.street,companyname,summary,companyaddress,workingtime)
# Restaurant1 = Restaurant

travelPlan1 = TravelPlan("Beijing",)
travelPlan2 = TravelPlan("Shanghai")

travelPlan1.cityList.append(1)
print(travelPlan1.cityList)
print(travelPlan2.cityList)
