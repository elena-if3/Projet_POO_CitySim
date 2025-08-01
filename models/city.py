import random
from .facility.facility import Facility
from .facility.housing import Housing
from .facility.leisure import Leisure
from .facility.factory import Factory
from .resource.resource import Resource
from .resource.food import Food
from .resource.water import Water
from .resource.electricity import Electricity
from .citizen.citizen import Citizen

class City:
    def __init__(self, name="Springfield", facilities=None, resources=None):
        self.__day = 0
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
        housing_available = [housing for housing in self.__facilities.get(Housing, []) if not housing.is_full]
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

    def factory_produce(self, is_night):
        for facility_type, facilities in self.__facilities.items():
            if issubclass(facility_type, Factory):
                for facility in facilities:
                    self.add_resource(facility.produce(weekday=self.weekday, is_night=is_night))

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
                if not factory.is_full:
                    factory.add_worker(citizen)
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

    def grow_citizen(self, is_night):
        for citizen in self.citizens:
            citizen.grow(food=self.__resources[Food], water=self.__resources[Water], is_night=is_night)

    def grow_city(self, is_night):
        for facilities in self.__facilities.values():
            for facility in facilities:
                facility.grow(electricity=self.__resources[Electricity], water=self.__resources[Water], is_night=is_night)
        self.grow_citizen(is_night=is_night)

    def live_day(self):
        self.event_happen()
        self.update_citizens_facilities()
        self.municipality()
        self.factory_produce(is_night=False)
        self.citizens_leisure()
        self.grow_city(is_night=False)
        self.update_citizens_facilities()

    def live_night(self):
        self.event_happen()
        self.update_citizens_facilities()
        self.factory_produce(is_night=True)
        self.grow_city(is_night=True)

    def live_complete_day(self):
        self.live_day()
        self.live_night()
        self.__day += 1
