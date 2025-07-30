from production import Production
from ..resource.food import Food

class FoodFactory(Production):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
    
    def produce(self):
        return (Food, len(self.workers))
