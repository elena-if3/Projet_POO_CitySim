from .facility import Facility

class Leisure(Facility):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)