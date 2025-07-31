from models.citizen.profession import Profession


class Work:

    def __init__(self, profession: Profession, is_day_worker: bool, off_days: list[int]) -> None:
        self.__profession = profession
        self.__is_day_worker = is_day_worker
        self.off_days = off_days

    
    @property
    def profession(self) -> Profession:
        return self.__profession
    
    @profession.setter
    def profession(self, value : Profession) -> None:
        if not isinstance(value, Profession):
            raise TypeError("Not an instance of Profession")
        self.__profession = value

    @property
    def is_day_worker(self) -> bool:
        return self.__is_day_worker