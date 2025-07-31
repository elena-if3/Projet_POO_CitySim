from .facility import Facility

class Leisure(Facility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__users = []

    @property
    def users(self) -> list("Citizen"):
        return self.__users
    
    @property
    def is_full(self) -> bool:
        return len(self.users) >= self.capacity