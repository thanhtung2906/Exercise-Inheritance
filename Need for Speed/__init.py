from vehicle import Vehicle
from car import Car
from sportcar import SportCar
from familycar import FamilyCar
from motorcycle import MotorCycle
from crossmotorcycle import CrossMotorCycle
vehicle = Vehicle(50, 150)
print(vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)