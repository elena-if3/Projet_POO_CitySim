import random

class City:
    def __init__(self, name="Springfield", facilities={}, resources={}):
        self.day = 0
        self.daily_log = []
        self.name = name
        self.facilities = facilities
        self.resources = resources
        self.homeless_citizens = []

    @property
    def capacity(self):
        return sum(housing.capacity for housing in self.facilities[Housing])

    @property
    def weekday(self):
        return self.day % 7

    @property
    def citizens(self):
        citizens = [inhabitant for inhabitant in housing.inhabitants for housing in self.facilities[Housing]]
        citizens.extend(self.homeless_citizens)
        return citizens

    @property
    def happiness(self):
        return sum(citizen.satisfaction for citizen in self.citizens) // len(self.citizens)

    def add_facility(self, facility):
        if not issubclass(type(facility), Facility):
            raise TypeError("Not a subclass of Facility")
        self.facilities[type(facility)].append(facility)

    def add_citizen(self, citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Not an instance of citizen")
        housing_available = [housing for housing in self.facilities[Housing] if housing.capacity > len(housing.inhabitants)]
        if housing_available:
            random.choice(housing_available).add_inhabitant(citizen)
        else:
            self.homeless_citizens.append(citizen)

    def add_resource(self, resource):
        if not issubclass(type(resource), Resource):
            raise TypeError("Not a subclass of Resource")
        self.resources[type(resource)] += self.resources.get(type(resource), 0) + resource.amount

    def live_day(self):
        production_facilities = [facility for facility in self.facilities if issubclass(type(facility), Production)]
        for production_facility in production_facilities:
            resource = production_facility.produce()
            self.add_resource(resource)
