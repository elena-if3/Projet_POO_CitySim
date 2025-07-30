from production import Production
from ..resource.water import Water

class WaterFacility(Production):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
    
    def produce(self):
        return (Water, len(self.workers))
