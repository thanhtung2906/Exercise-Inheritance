import sys
sys.path.append("c:\\Users\\tobug\\Documents\\GitHub\\Exercise-Inheritance\\Restaurant\\Restaurant")
from product import Product
class Food(Product):
    def __init__(self, name: int, price: float,grams:float) -> None:
        super().__init__(name, price)
        self.grams = grams