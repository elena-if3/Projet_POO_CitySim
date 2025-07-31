from enum import Enum
from models.facility.food_factory import FoodFactory
from models.facility.power_plant import PowerPlant
from models.facility.water_supply_plant import WaterSupplyPlant



class Profession(Enum):
    FOOD_FACTORY = FoodFactory
    POWER_PLANT = PowerPlant
    WATER_FACILITY = WaterFacility
    JOBLESS = jobless