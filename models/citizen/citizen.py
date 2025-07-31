
class Citizen:
    def __init__(self, name: str, age: int, satisfaction: int, day_activity: bool = True) -> None:
        self.__name = name
        self.__age = age
        self.__satisfaction = satisfaction
        self.__day_activity = day_activity

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Not an integer")
        self.__age = value
    
    @property
    def satisfaction(self) -> int:
        return self.__satisfaction
    
    @satisfaction.setter
    def satisfaction(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Not an integer")
        self.__satisfaction = value

    @property
    def day_activity(self) -> bool:
        return self.__day_activity
