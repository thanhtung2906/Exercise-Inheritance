import sys
sys.path.append("C:/Users/tobug/Documents/GitHub/Exercise-Inheritance/Restaurant/Restaurant")
from product import Product
class Beverage(Product):
    def __init__(self, name: int, price: float,milliliters:float) -> None:
        super().__init__(name, price)
        self.milliliters = milliliters 



