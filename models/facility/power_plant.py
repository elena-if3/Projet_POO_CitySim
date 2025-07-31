from .production import Production
from ..resource.electricity import Electricity

class PowerPlant(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self):
        return (Electricity, len(self.workers))
