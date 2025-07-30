class Citizen:
    def __init__(self, name: str, age: int, profession: Profession, satisfaction: int, day_activity: bool = True):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__satisfaction = satisfaction
        self.__day_activity = day_activity

        
