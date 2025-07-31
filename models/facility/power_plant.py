from .production import Production
from ..resource.electricity import Electricity
from ...tools.constants import *

class PowerPlant(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self):
        # all workers work
        super().produce()
        produced_qty = super().dayly_production(DAILY_ELECTRICITY_PRODUCTION_PER_WORKER)
        return Electricity(produced_qty)