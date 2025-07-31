from .production import Production
from ..resource.electricity import Electricity
from ...tools.constants import *

class PowerPlant(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self, day: int, is_day_shift: bool) -> Electricity:
        # Get factoy workers working on that shift
        working_workers = super().get_working_workers(day, is_night)
        # Get total quantity produced during that shift
        produced_qty = super().daily_production(DAILY_ELECTRICITY_PRODUCTION_PER_WORKER, working_workers)
        return Electricity(produced_qty)