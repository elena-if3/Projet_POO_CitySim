from models.facility.factory import Factory
from models.resource.food import Food
from models.resource.electricity import Electricity
from models.resource.water import Water
from tools.constants import *

class FoodFactory(Factory):
    def __init__(self, name = "Food Factory", **kwargs):
        super().__init__(name = name, **kwargs)
    
    def produce(self, weekday: int, is_night: bool) -> Food:
        # Get factory workers working on that shift
        working_workers = super().get_working_workers(weekday, is_night)
        # Make them work
        super().workers_work(working_workers)
        # Degrade factory
        super().damage(FOOD_PRODUCTION_DAMAGE)
        # Get total quantity produced during that shift
        produced_qty = super().daily_production(FOOD_DAILY_PRODUCTION_PER_WORKER, len(working_workers))
        return Food(produced_qty)
    
    def grow(self, electricity: Electricity, water: Water, is_night: bool) -> None:
        water.amount -= WATER_LOSS_DAILY_FOOD_FACTORY
        electricity.amount -= ELECTRICITY_LOSS_DAILY_FOOD_FACTORY
        super().grow()
