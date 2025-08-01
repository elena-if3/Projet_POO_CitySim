from random import choice, randint
from models.citizen.work_info import WorkInfo
from models.facility.leisure import Leisure
from models.resource.electricity import Electricity
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


    def grow(self, is_night: bool, electricity: Electricity, food: Food, water: Water) -> None:
        if not isinstance(is_night, bool):
            raise TypeError("Parameter 'is_night' must be a boolean")
        if not isinstance(electricity, Electricity):
            raise TypeError("Parameter 'electricity' must be a list")
        if not isinstance(food, Food):
            raise TypeError("Parameter 'food' must be a list")
        if not isinstance(water, Water):
            raise TypeError("Parameter 'water' must be a list")
        if not is_night:
            if self.work_info.day_worker:
                self.__use_resources(electricity, food, water)
            else:
                self.__sleep()
                self.__get_older()
                self.__update_status()
        else:
            if not self.work_info.day_worker:
                self.__use_resources(electricity, food, water)
            else:
                self.__sleep()
                self.__get_older()
                self.__update_status()

    def __get_older(self) -> None:
        self.__age += 1

    def __use_resources(self, electricity: Electricity, food: Food, water: Water) -> None:
        pass

    def __update_status(self) -> None:
        r = randint(1, 100)
        if 20 < self.__age < 40:
            if r == 100:
                self.__is_alive = False
        if self.__age >= 40:
            if r > 95:
                self.__is_alive = False
        if self.__age >= 50:
            if r > 90:
                self.__is_alive = False
        if self.__age >= 60:
            if r > 80:
                self.__is_alive = False
        if self.__age >= 70:
            if r > 65:
                self.__is_alive = False
        if self.__age >= 80:
            if r > 50:
                self.__is_alive = False
        if self.__age >= 90:
            if r > 20:
                self.__is_alive = False
        if self.__>= 100:
            if r > 1:
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

        if facility.is_full:
            self.__satisfaction -= 1
        else:
            self.__satisfaction += 2
            facility.damage(1)    # damage by how many points???