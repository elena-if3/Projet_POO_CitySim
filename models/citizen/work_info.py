from models.citizen.profession import Profession


class WorkInfo:

    def __init__(self, profession: Profession = Profession.JOBLESS, employed: bool = False, day_worker: bool = True, off_days: list = list(range(7))) -> None:
        self.__profession = profession
        self.__employed = employed
        self.__day_worker = day_worker
        self.off_days = off_days

    
    @property
    def profession(self) -> Profession:
        return self.__profession
    
    @property
    def employed(self) -> bool:
        return self.__employed

    @profession.setter
    def profession(self, value : Profession) -> None:
        if not isinstance(value, Profession):
            raise TypeError("Not an instance of Profession")
        self.__profession = value

    @property
    def is_day_worker(self) -> bool:
        return self.__day_worker