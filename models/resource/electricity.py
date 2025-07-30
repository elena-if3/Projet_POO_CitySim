from resource import Resource

class Electricity(Resource):
    def __init__(self, amount : int = 0):
        super().__init__(amount)