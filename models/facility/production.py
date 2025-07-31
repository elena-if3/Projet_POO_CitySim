from .facility import Facility
from abc import abstractmethod
from ...tools.constants import *

class Production(Facility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__workers = []

    @property
    def workers(self):
        return self.__workers
    
    @property
    def is_full(self) -> bool:
        return len(self.workers) >= self.capacity

    @abstractmethod
    def produce():
        pass

    def get_working_workers(self, day: int, is_day_shift: bool) -> list("Citizen"):
        working_workers = [
            worker for worker in self.workers if (
                worker.work_info.is_day_worker == is_day_shift and
                day not in worker.work_info.off_days)
        ]
        for worker in working_workers:
            worker.work()
        return working_workers

    def dayly_production(self, daily_production_per_worker: int, working_workers_count: int) -> int:
        if self.integrity < PRODUCTION_SHUTDOWN_THRESHOLD:
            # no production possible
            return 0
        else:
            # total production based on workers count and facility's integrity 
            return round(working_workers_count * daily_production_per_worker * (self.integrity / 100))

    def add_worker(self, citizen) -> bool:
        pass