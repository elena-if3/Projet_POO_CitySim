from models.facility.facility import Facility
from tools.constants import *
import random

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
    
    def grow(self, electricity: Electricity, water: Water, is_night: bool) -> None:
        if is_night:
            self.users = []
        else:
            damage = round(self.users * DAMAGE_DAILY_PER_LEISURE_USER)
            super().grow(damage)