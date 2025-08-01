from models.facility.housing import Housing
from models.citizen.citizen import Citizen
from models.citizen.profession import Profession

# TEST FACILITY METHODS
house = Housing()
print(house.capacity, house.name, house.is_full, house.inhabitants)

roger = Citizen("Roger", 20, Profession.POWER_PLANT, 50)
house.add_inhabitant(roger)
print(house.capacity, house.name, house.is_full, [c.name for c in house.inhabitants])