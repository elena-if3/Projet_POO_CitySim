import random
from ..models.citizen.citizen import Citizen
from ..models.citizen.profession import Profession

class Generator:
    @staticmethod
    def citizen_generator():
        first_names = [
        "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
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
        "Douglas", "Joan", "Zachary", "Christina", "Peter", "Kelly", "Kyle", "Cheryl"
        ]
        surnames = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
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
        "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez"
        ]
        name = f"{random.choice(first_names)} {random.choice(surnames)}"
        age = random.randint(0, 18)
        profession = Profession.JOBLESS
        satisfaction = 100
        day_worker = True
        return Citizen(name, age, profession, satisfaction, day_worker)
