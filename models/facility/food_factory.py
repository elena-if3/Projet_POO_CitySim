from .production import Production
from ..resource.food import Food
from ...tools.constants import *

class FoodFactory(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self, day: int, is_day_shift: bool) -> Food:
        # Get factoy workers working on that shift
        working_workers = super().get_working_workers(day, is_night)
        # Get total quantity produced during that shift
        produced_qty = super().dayly_production(DAILY_FOOD_PRODUCTION_PER_WORKER, working_workers)
        return Food(produced_qty)
