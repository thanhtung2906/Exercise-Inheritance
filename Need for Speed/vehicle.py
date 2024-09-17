class Vehicle:
    fuel_consumption = 1.25
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption
    
    def __init__(self,fuel,horse_power):
        self.fuel = fuel 
        self.horse_power = horse_power 
        
    def drive(self,kilometers):
        self.fuel = self.fuel - kilometers*self.DEFAULT_FUEL_CONSUMPTION
        if self.fuel <= 0:
            self.fuel = 0 

