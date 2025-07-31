from models.citizen.work_info import WorkInfo
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


    def grow() -> None:
        pass

    def __get_older() -> None:
        pass

    def __use_resources(electricity: Electricity, food: Food, water: Water) -> None:
        pass

    def __update_status() -> None:
        pass

    def __sleep() -> None:
        pass

    def leisure_time() -> None:
        pass
    