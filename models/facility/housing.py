from .facility import Facility

class Housing(Facility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__inhabitants = []

    @property
    def inhabitants(self):
        return self.__workers

    def add_inhabitant(citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Only citizens can be added as housing inhabitants")
        if len(self.__inhabitants) == self.capacity:
            raise Exception("This housing is full already")

        if self.capacity > len(self.__inhabitants):
            self.inhabitants.append(citizen) 