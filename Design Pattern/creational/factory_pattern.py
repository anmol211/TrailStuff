from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class Car(Vehicle):
    def create_vehicle(self):
        print("Car created")


class Bike(Vehicle):
    def create_vehicle(self):
        print("Bike created")


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicleType) -> Vehicle:
        if vehicleType == "Car":
            return Car()
        if vehicleType == "Bike":
            return Bike()


if __name__ == '__main__':
    vehicle_factory = VehicleFactory.get_vehicle("Car")
    vehicle_factory.create_vehicle()
