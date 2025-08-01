from models.facility.facility import Facility
from abc import abstractmethod
from tools.constants import *
from models.resource.electricity import Electricity
import random

class Factory(Facility):
    def __init__(self, capacity: int = FACTORY_DEFAULT_CAPACITY, **kwargs):
        super().__init__(capacity, **kwargs)
        self.__workers = []

    @property
    def workers(self) -> list("Citizen"):
        return self.__workers
    
    @property
    def is_full(self) -> bool:
        return len(self.workers) >= self.capacity

    @property
    

    @abstractmethod
    def produce():
        pass

    def workers_work(self, working_workers: list("Citizen")) -> None:
        for worker in working_workers:
            worker.work()
    
    def get_working_workers(self, day: int, is_day_shift: bool) -> list("Citizen"):
        working_workers = [
            worker for worker in self.workers if (
                worker.work_info.is_day_worker == is_day_shift and
                day not in worker.work_info.off_days)
        ]
        return working_workers

    def daily_production(self, daily_production_per_worker: int, working_workers_count: int) -> int:
        if self.integrity < PRODUCTION_SHUTDOWN_THRESHOLD:
            # no production possible
            return 0
        else:
            # total production based on workers count and facility's integrity 
            return round(working_workers_count * daily_production_per_worker * (self.integrity / 100))

    def add_worker(self, citizen: "Citizen") -> bool:
        if self.is_full:
            return False
        self.workers.append(citizen)
        return True
    
    def grow(self):
        daily_damage = random.randint(0, DAMAGE_MAX_DAILY_FACTORY)
        super().grow(daily_damage)