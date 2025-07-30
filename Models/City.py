import random

class City:
    def __init__(self, name="Springfield", facilities=None, resources=None):
        self.__day = 0
        self.__daily_log = []
        self.__name = name
        self.__facilities = facilities or {}
        self.__resources = resources or {}
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
        return sum(housing.capacity for housing in self.__facilities.get(Housing, []))

    @property
    def weekday(self):
        return self.__day % 7

    @property
    def citizens(self):
        return [inhabitant for housing in self.__facilities.get(Housing, []) for inhabitant in housing.inhabitants] + self.__homeless_citizens

    @property
    def happiness(self):
        citizens = self.citizens
        if citizens:
            return sum(citizen.satisfaction for citizen in citizens) // len(citizens)
        return 0

    def add_facility(self, facility):
        if not isinstance(facility, Facility):
            raise TypeError("Not a Facility instance")
        self.__facilities.setdefault(type(facility), []).append(facility)

    def add_citizen(self, citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Not a Citizen instance")
        housing_available = [housing for housing in self.__facilities.get(Housing, []) if housing.capacity > len(housing.inhabitants)]
        if housing_available:
            random.choice(housing_available).add_inhabitant(citizen)
        else:
            self.__homeless_citizens.append(citizen)

    def add_resource(self, resource):
        if not isinstance(resource, Resource):
            raise TypeError("Not a Resource instance")
        self.__resources[type(resource)] = self.__resources.get(type(resource), 0) + resource.amount

    def live_day(self):
        for facility_type, facilities in self.__facilities.items():
            if issubclass(facility_type, Production):
                for facility in facilities:
                    self.add_resource(facility.produce())
        self.__day += 1
