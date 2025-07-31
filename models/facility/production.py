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

    @abstractmethod
    def produce():
        pass

    def produce():
        for worker in self.workers:
            worker.work()

    def dayly_production(self, daily_production_per_worker) -> int:
        if self.integrity < PRODUCTION_SHUTDOWN_THRESHOLD:
            # no production possible
            return 0
        else:
            # total production based on workers count and facility's integrity 
            return round(len(self.workers) * daily_production_per_worker * (self.integrity / 100))

