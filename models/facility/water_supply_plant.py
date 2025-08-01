from models.facility.factory import Factory
from models.resource.water import Water
from tools.constants import *

class WaterSupplyPlant(Factory):
    def __init__(self, name = "Water Supply Plant", **kwargs):
        super().__init__(name = name, **kwargs)
    
    def produce(self, day: int, is_day_shift: bool) -> "Water":
        # Get factory workers working on that shift
        working_workers = super().get_working_workers(day, is_night)
        # Make them work
        super.workers_work(working_workers)
        # Degrade factory
        super().damage(WATER_PRODUCTION_DAMAGE)
        # Get total quantity produced during that shift
        produced_qty = super().daily_production(WATER_DAILY_PRODUCTION_PER_WORKER, len(working_workers))
        return Water(produced_qty)
    
    def grow(self, electricity: "Electricity", water: "Water", is_night: bool) -> None:
        electricity.amount -= ELECTRICITY_LOSS_DAILY_POWER_PLANT
        super().grow()
