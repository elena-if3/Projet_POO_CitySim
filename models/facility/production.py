from facility import Facility
from abc import abstractmethod

class Production(Facility):
    def __init__(self):
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @abstractmethod
    def produce():
        pass