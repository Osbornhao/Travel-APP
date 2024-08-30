from City import City
from Transportation import Transportation
from TravelProject import TravelProject
from typing import List

class TravelPlan:
   def __init__(self, planName: List[str]):
      self.planName = planName
      self.cityList = []
      self.transportationList = []
      self.travelProjectList = []


