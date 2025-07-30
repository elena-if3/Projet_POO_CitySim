import random

class City:
    def __init__(self, name="Springfield", facilities={}, resources={}):
        self.__day = 0
        self.__daily_log = []
        self.__name = name
        self.__facilities = facilities
        self.__resources = resources
        self.__homeless_citizens = []

    @property
    def day(self):
        return self.__day

    @property
    def name(self):
        return self.__name

    @property
    def daily_log(self):
        return self.__daily_log

    @property
    def facilities(self):
        return self.__facilities

    @property
    def resources(self):
        return self.__resources

    @property
    def homeless_citizens(self):
        return self.__homeless_citizens

    @property
    def capacity(self):
        return sum(housing.capacity for housing in self.__facilities[Housing])

    @property
    def weekday(self):
        return self.__day % 7

    @property
    def citizens(self):
        citizens = [inhabitant for inhabitant in housing.inhabitants for housing in self.__facilities[Housing]]
        citizens.extend(self.__homeless_citizens)
        return citizens

    @property
    def happiness(self):
        return sum(citizen.satisfaction for citizen in self.__citizens) // len(self.__citizens)

    def add_facility(self, facility):
        if not issubclass(type(facility), Facility):
            raise TypeError("Not a subclass of Facility")
        self.__facilities[type(facility)].append(facility)

    def add_citizen(self, citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Not an instance of citizen")
        housing_available = [housing for housing in self.__facilities[Housing] if housing.capacity > len(housing.inhabitants)]
        if housing_available:
            random.choice(housing_available).add_inhabitant(citizen)
        else:
            self.__homeless_citizens.append(citizen)

    def add_resource(self, resource):
        if not issubclass(type(resource), Resource):
            raise TypeError("Not a subclass of Resource")
        self.__resources[type(resource)] += self.__resources.get(type(resource), 0) + resource.amount

    def live_day(self):
        production_facilities = [facility for facility in self.__facilities if issubclass(type(facility), Production)]
        for production_facility in production_facilities:
            resource = production_facility.produce()
            self.add_resource(resource)
