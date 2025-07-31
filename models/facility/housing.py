from .facility import Facility

class Housing(Facility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__inhabitants = []

    @property
    def inhabitants(self) -> list("Citizen"):
        return self.__inhabitants
    
    @property
    def is_full(self) -> bool:
        return len(self.inhabitants) >= self.capacity

    def add_inhabitant(citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Only citizens can be added as housing inhabitants")
        if len(self.__inhabitants) == self.capacity:
            raise Exception("This housing is full already")

        if self.capacity > len(self.__inhabitants):
            self.inhabitants.append(citizen) 