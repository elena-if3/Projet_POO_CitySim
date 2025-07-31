from random import choice
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
            raise TypeError("age must be an integer")
        self.__age = value
    
    @property
    def satisfaction(self) -> int:
        return self.__satisfaction
    
    @satisfaction.setter
    def satisfaction(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("satisfaction must be an integer")
        self.__satisfaction = value

    @property
    def is_alive(self) -> bool:
        return self.__is_alive
    
    @is_alive.setter
    def is_alive(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("is_alive must be a boolean")
        self.__is_alive = value


    def grow(self, is_night: bool, electricity: Electricity, food: Food, water: Water) -> None:
        if not isinstance(is_night, bool):
            raise TypeError("parameter 'is_night' must be a boolean")
        if not isinstance(electricity, Electricity):
            raise TypeError("parameter 'electricity' must be a list")
        if not isinstance(food, Food):
            raise TypeError("parameter 'food' must be a list")
        if not isinstance(water, Water):
            raise TypeError("parameter 'water' must be a list")
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
        pass

    def __use_resources(self, electricity: Electricity, food: Food, water: Water) -> None:
        pass

    def __update_status(self) -> None:
        pass

    def __sleep(self) -> None:
        pass

    def leisure_time(self, parks: list[Leisure]) -> None:
        if not isinstance(parks, list):
            raise TypeError("parameter 'parks' must be a list")
        if len(parks) > 1:
            park = choice(parks)
        elif len(parks) == 1:
            park = parks[0]
        else:
            # What if list if empty?
            pass
        # How do we check if max capacity reached???
        
        pass
    