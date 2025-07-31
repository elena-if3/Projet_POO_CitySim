from .factory import Factory
from ..resource.electricity import Electricity
from ...tools.constants import *

class PowerPlant(Factory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self, day: int, is_day_shift: bool) -> Electricity:
        # Get factory workers working on that shift
        working_workers = super().get_working_workers(day, is_night)
        # Make them work
        super.workers_work(working_workers)
        # Degrade factory
        super().damage(ELECTRICITY_PRODUCTION_DAMAGE)
        # Get total quantity produced during that shift
        produced_qty = super().daily_production(ELECTRICITY_DAILY_PRODUCTION_PER_WORKER, len(working_workers))
        return Electricity(produced_qty)