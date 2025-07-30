from models.citizen.profession import Profession


class Citizen:
    def __init__(self, name: str, age: int, profession: Profession, satisfaction: int, day_activity: bool = True):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__satisfaction = satisfaction
        self.__day_activity = day_activity

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value: int):
        self.__age = value
    
    @property
    def profession(self):
        return self.__profession
    
    @profession.setter
    def profession(self, value : Profession):
        self.__profession = value
    
    @property
    def satisfaction(self):
        return self.__satisfaction
    
    @satisfaction.setter
    def satisfaction(self, value: int):
        self.__satisfaction = value

    @property
    def day_activity(self):
        return self.__day_activity
