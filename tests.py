from models.facility.housing import Housing
from models.facility.water_supply_plant import WaterSupplyPlant
from models.facility.food_factory import FoodFactory
from models.facility.power_plant import PowerPlant
from models.citizen.citizen import Citizen
from models.citizen.profession import Profession
from models.citizen.work_info import WorkInfo

# Create a citizen
roger = Citizen("Roger", 20, 80, WorkInfo(profession = Profession.WATER_SUPPLY_PLANT))

# TEST FACILITY METHODS

# HOUSING
facility = Housing()
facility.add_inhabitant(roger)
print(facility.name, facility.capacity, facility.is_full, [c.name for c in facility.inhabitants])

# WATER SUPPLY PLANT
facility = WaterSupplyPlant()
facility.add_worker(roger)
print(facility.name, facility.capacity, facility.is_full, [c.name for c in facility.workers])

# POWER PLANT
facility = PowerPlant()
facility.add_worker(roger)
print(facility.name, facility.capacity, facility.is_full, [c.name for c in facility.workers])

# FOOD FACTORY
facility = FoodFactory()
facility.add_worker(roger)
print(facility.name, facility.capacity, facility.is_full, [c.name for c in facility.workers])