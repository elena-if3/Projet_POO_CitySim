from .production import Production
from ..resource.water import Water

class WaterFacility(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self):
        return (Water, len(self.workers))
