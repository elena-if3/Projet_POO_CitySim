from .production import Production
from ..resource.water import Water
from ...tools.constants import *

class WaterFacility(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self):
        # all workers work
        super().produce()
        produced_qty = super().dayly_production(DAILY_WATER_PRODUCTION_PER_WORKER)
        return Water(produced_qty)
