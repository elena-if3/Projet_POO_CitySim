from models.citizen.profession import Profession


class WorkInfo:

    def __init__(self, profession: Profession = Profession.JOBLESS, employed: bool = False, day_worker: bool = True, off_days: list = list(range(7))) -> None:
        self.__profession = profession
        self.employed = employed
        self.__day_worker = day_worker
        self.__off_days = off_days


    @property
    def profession(self) -> Profession:
        return self.__profession
    
    @profession.setter
    def profession(self, value: Profession) -> None:
        if not isinstance(value, Profession):
            raise TypeError("Value 'profession' must be an instance of Profession")
        self.__profession = value

    @property
    def day_worker(self) -> bool:
        return self.__day_worker
    
    @day_worker.setter
    def day_worker(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("Value 'day_worker' must be a boolean")
        self.__day_worker = value

    @property
    def off_days(self) -> list:
        return self.__off_days
    
    @off_days.setter
    def off_days(self, value: list) -> None:
        if not isinstance(value, list):
            raise TypeError("Value 'off_days' must be a list")
        self.__off_days = value
