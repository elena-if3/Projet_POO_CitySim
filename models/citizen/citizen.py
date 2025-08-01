from random import choice, randint
from models.citizen.work_info import WorkInfo
from models.facility.leisure import Leisure
from models.resource.food import Food
from models.resource.water import Water


class Citizen:
    def __init__(self, name: str, age: int, satisfaction: int, work_info: WorkInfo, is_alive: bool = True) -> None:
        self.__name = name
        self.__age = age
        self.__satisfaction = satisfaction
        self.work_info = work_info
        self.__is_alive = is_alive

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Value 'age' must be an integer")
        self.__age = value
    
    @property
    def satisfaction(self) -> int:
        return self.__satisfaction
    
    @satisfaction.setter
    def satisfaction(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Value 'satisfaction' must be an integer")
        self.__satisfaction = value

    @property
    def is_alive(self) -> bool:
        return self.__is_alive
    
    @is_alive.setter
    def is_alive(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("Value 'is_alive' must be a boolean")
        self.__is_alive = value


    def grow(self, food: Food, water: Water, is_night: bool) -> None:
        if not isinstance(food, Food):
            raise TypeError("Parameter 'food' must be an instance of Food")
        if not isinstance(water, Water):
            raise TypeError("Parameter 'water' must be an instance of Water")
        if not isinstance(is_night, bool):
            raise TypeError("Parameter 'is_night' must be a boolean")
        if not is_night:
            self.__get_older()
            self.__update_status()
            if self.work_info.day_worker:
                self.__use_resources(food, water)
            else:
                self.__sleep()
        else:
            if self.work_info.day_worker:
                self.__sleep()
            else:
                self.__use_resources(food, water)


    def __get_older(self) -> None:
        self.__age += 1

    def __use_resources(self, food: Food, water: Water) -> None:
        food.amount -= 1
        water.amount -= 1

    def __update_status(self) -> None:
        r = randint(1, 100)
        age = self.__age // 365
        # If aged between 20 and 40 -> 1% probability to die
        if 20 < age <= 40:
            if r == 100:
                self.__is_alive = False 
        # If aged between 40 and 50 -> 5% probability to die
        elif 40 < age <= 50:
            if r > 95:
                self.__is_alive = False
        # If aged between 50 and 60 -> 10% probability to die
        elif 50 < age <= 60:
            if r > 90:
                self.__is_alive = False
        # If aged between 60 and 70 -> 20% probability to die
        elif 60 < age <= 70:
            if r > 80:
                self.__is_alive = False
        # If aged between 70 and 80 -> 35% probability to die
        elif 70 < age <= 80:
            if r > 65:
                self.__is_alive = False
        # If aged between 80 and 90 -> 50% probability to die
        elif 80 < age <= 90:
            if r > 50:
                self.__is_alive = False
        # If aged between 90 and 100 -> 90% probability to die
        elif 90 < age <= 100:
            if r > 10:
                self.__is_alive = False
        # If aged between 100 and 110 -> 99% probability to die
        elif 100 < age <= 110:
            if r > 1:
                self.__is_alive = False
        # If over 110 -> dead by default
        else:
            self.__is_alive = False

    def __sleep(self) -> None:
        self.__satisfaction += 2    # increase by how many points???

    def leisure_time(self, facilities: list[Leisure]) -> None:
        if not isinstance(facilities, list):
            raise TypeError("Parameter 'facilities' must be a list")
        
        # If list empty (no available facilities) -> decrease satisfaction
        if len(facilities) == 0:
            self.__satisfaction -= 1
        elif len(facilities) > 1:
            facility = choice(facilities)
        else:
            facility = facilities[0]

        if park.is_full:
            self.__satisfaction -= 1
        # If available facility -> visit facility and increase satisfaction
        else:
            facility.add_user(self)
            self.__satisfaction += 2
            park.integrity -= 1    # Need integrity setter if I want to be able to do this