from .production import Production
from ..resource.food import Food

class FoodFactory(Production):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def produce(self):
        return (Food, len(self.workers))
