from .production import Production
from ..resource.food import Food
from ...tools.constants import *

class FoodFactory(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self):
        # all workers work
        super().produce()
        produced_qty = super().dayly_production(DAILY_FOOD_PRODUCTION_PER_WORKER)
        return Food(produced_qty)
