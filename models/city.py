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

    def add_citizen_housing(self, citizen):
        if not isinstance(citizen, Citizen):
            raise TypeError("Not a Citizen instance")
        housing_available = [housing for housing in self.__facilities.get(Housing, []) if housing.capacity > len(housing.inhabitants)]
        if housing_available:
            random.choice(housing_available).add_inhabitant(citizen)
            return True
        else:
            self.__homeless_citizens.append(citizen)
            return False

    def add_resource(self, resource):
        if not isinstance(resource, Resource):
            raise TypeError("Not a Resource instance")
        self.__resources[type(resource)] = self.__resources.get(type(resource), 0) + resource.amount

    def factory_produce(self):
        for facility_type, facilities in self.__facilities.items():
            if issubclass(facility_type, Production):
                for facility in facilities:
                    self.add_resource(facility.produce(self.weekday))

    def event_happen(self):
        pass

    def update_citizens_facilities(self):
        for facility_type, facilities in self.facilities.items():
            for facility in facilities:
                if facility.integrity <= 0:
                    if isinstance(facility, Housing):
                        self.__homeless_citizens.append(facility.inhabitants)
                    self.__facilities[facility_type].remove(facility)
        for homeless_citizen in self.__homeless_citizens:
            if not homeless_citizen.is_alive:
                self.__homeless_citizens.remove(homeless_citizen)

    def attribute_factory(self, citizen):
        for factories in self.__facilities[citizen.profession].values():
            for factory in factories:
                if factory.add_worker(citizen): # True if there is place in factory
                    return True
        return False

    def municipality(self):
        # repair facilities
        for facilities in self.__facilities.values():
            for facility in facilities:
                if facility.integrity <= 70:
                    facility.repair(25)
        # reattribute homeless
        for homeless_citizen in self.__homeless_citizens:
            if not self.add_citizen_housing(homeless_citizen):
                break
        # reattribute work
        for citizen in self.citizens:
            if not citizen.work.employed:
                self.attribute_factory(citizen)

    def citizens_leisure(self):
        for citizen in self.citizens:
            if self.weekday in citizen.work.off_days:
                citizen.leisure(self.__facilities[Leisure])

    def grow_city(self):
        for facilities in self.__facilities.values():
            for facility in facilities:
                facility.degrade()
        for citizen in self.citizens:
            citizen.grow(food=self.__resources[Food], water=self.__resources[Water])

    def live_day(self):
        self.event_happen()
        self.update_citizens_facilities()
        self.municipality()
        self.factory_produce()
        self.citizens_leisure()
        self.grow_city()
        self.update_citizens_facilities()
        self.__day += 1
