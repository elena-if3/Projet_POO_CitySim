from .resource import Resource

class Electricity(Resource):
    def __init__(self, amount : int = 0) -> None:
        super().__init__(amount)
