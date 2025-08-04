import random

from models.citizen.work_info import WorkInfo
from models.city import City
from models.citizen.citizen import Citizen
from models.facility.food_factory import FoodFactory
from models.facility.power_plant import PowerPlant
from models.facility.water_supply_plant import WaterSupplyPlant
from models.facility.leisure import Leisure
from models.facility.housing import Housing
from models.resource.electricity import Electricity
from models.resource.food import Food
from models.resource.water import Water

class Generator:
    @staticmethod
    def citizen_generator():
        first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
                "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph",
                "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy",
                "Daniel", "Lisa", "Matthew", "Betty", "Anthony", "Helen", "Mark", "Sandra",
                "Paul", "Donna", "Steven", "Carol", "Andrew", "Ruth", "Kenneth", "Sharon",
                "Joshua", "Michelle", "Kevin", "Laura", "Brian", "Kimberly", "George", "Dorothy",
                "Timothy", "Brenda", "Ronald", "Amy", "Jason", "Ashley", "Edward", "Rebecca",
                "Jeffrey", "Deborah", "Ryan", "Lauren", "Jacob", "Stephanie", "Gary", "Shirley",
                "Nicholas", "Cynthia", "Eric", "Angela", "Jonathan", "Melissa", "Stephen", "Anna",
                "Larry", "Amanda", "Justin", "Kathleen", "Scott", "Christine", "Brandon", "Kelly",
                "Benjamin", "Samantha", "Samuel", "Debra", "Gregory", "Victoria", "Frank", "Martha",
                "Raymond", "Debra", "Patrick", "Catherine", "Alexander", "Nicole", "Jack", "Megan",
                "Dennis", "Virginia", "Jerry", "Maria", "Tyler", "Heather", "Aaron", "Diane",
                "Jose", "Julie", "Adam", "Joyce", "Henry", "Evelyn", "Nathan", "Frances",
                "Douglas", "Joan", "Zachary", "Christina", "Peter", "Kelly", "Kyle", "Cheryl"]
        surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
                "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
                "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Clement",
                "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen",
                "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera",
                "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner",
                "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris",
                "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
                "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox",
                "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett",
                "Gray", "Mendoza", "Ruiz", "Hughes", "Price", "Myers", "Long", "Foster",
                "Sanders", "Ross", "Russell", "Patterson", "Coleman", "Powell", "Diaz", "Washington",
                "Bell", "Gonzales", "Scott", "Cooper", "Bailey", "Reed", "Kelly", "Howard",
                "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez"]
        name = f"{random.choice(first_names)} {random.choice(surnames)}"
        age = random.randint(0, 18)

        work_info = WorkInfo()
        satisfaction = 100
        return Citizen(name, age, satisfaction, work_info)

    @staticmethod
    def generate_city():
        prefixes = ["Aero", "Aqua", "Aven", "Breeze", "Bright", "Cloud", "Coral", "Crimson", "Crystal",
                "Dawn", "Deep", "Emerald", "Ever", "Fair", "Fallen", "Golden", "Grand", "Green",
                "Harbor", "Iron", "Jade", "Lake", "Light", "Lumi", "Mist", "Moon", "Neo",
                "New", "North", "Old", "Opal", "Pacific", "Pearl", "Pine", "Port", "Ridge",
                "River", "Rose", "Royal", "Sacred", "Silver", "Sky", "South", "Star", "Stone",
                "Sun", "Terra", "Thorn", "Titan", "Umbra", "Vesper", "Whisper", "Wild", "Willow",
                "Wind", "Winter", "Zephyr", "Azure", "Blaze", "Cinder", "Dusk", "Echo", "Frost",
                "Glimmer", "Helix", "Ivory", "Juno", "Kestrel", "Lyric", "Mystic", "Nova", "Onyx",
                "Phoenix", "Quasar", "Riven", "Seraph", "Twilight", "Utopia", "Vortex", "Woven",
                "Xenon", "Yield", "Zenith"]
        middles = ["dale", "ville", "ton", "borough", "wood", "field", "crest", "haven", "brook",
                "bridge", "cliff", "glen", "hollow", "land", "mere", "mont", "moor", "port",
                "ridge", "rise", "run", "shade", "shire", "side", "spring", "summit", "vale",
                "view", "water", "wick", "cross", "gate", "path", "pinnacle", "peak",
                "point", "station", "stop", "town", "valley", "way", "bend", "bluff", "cove",
                "falls", "forks", "grove", "heights", "isle", "lagoon", "mesa", "oasis", "plain",
                "rapids", "reef", "shore", "terrace", "tide", "traverse", "vance",
                "vortex", "walk", "wind", "light", "spark", "pulse", "core", "nexus",
                "spire", "beacon", "citadel", "domain", "enclave", "forge", "garden", "harbor",
                "keep", "labyrinth", "metropolis", "outpost", "paradise", "sanctuary", "sanctum",
                "stronghold", "terminus"]
        suffixes = ["ia", "ton", "ville", "bury", "ham", "ford", "ington", "borough", "wood", "land",
                "field", "dale", "shire", "port", "burg", "mouth", "wick", "bridge", "castle",
                "don", "holm", "ley", "minster", "oaks", "pine", "ridge", "stone", "view",
                "water", "well", "haven", "glen", "crest", "peak", "point", "city", "polis",
                "topia", "landia", "gard", "stead", "mere", "hold", "marsh", "moor", "strand",
                "bend", "bluff", "cove", "docks", "falls", "forks", "grove", "heights", "isle",
                "lagoon", "mesa", "oasis", "plain", "rapids", "reef", "shore", "summit", "terrace",
                "tide", "traverse", "valley", "walk", "wind", "zone", "core", "edge", "gate",
                "nexus", "orb", "prism", "shard", "spark", "spire", "vault", "vista", "zero"]
        city_name = f"{random.choice(prefixes)}{random.choice(middles)}{random.choice(suffixes)}"
        factory_types = [PowerPlant, FoodFactory, WaterSupplyPlant]
        facilities = {}
        for factory_type in factory_types:
            for _ in range(2):
                facilities.setdefault(factory_type, []).append(factory_type())
        facilities[Leisure] = [Leisure()]
        for _ in range(30):
            facilities.setdefault(Housing, []).append(Housing())
        resources = {Water:Water(100), Food:Food(100), Electricity:Electricity(100)}
        city = City(name=city_name, facilities=facilities, resources=resources)
        for _ in range(100):
            city.add_citizen_housing(Generator.citizen_generator())
        return city
