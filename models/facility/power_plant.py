from production import Production
from ..resource.electricity import Electricity

class PowerPlant(Production):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
    
    def produce(self):
        return (Electricity, len(self.workers))