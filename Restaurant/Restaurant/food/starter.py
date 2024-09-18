import sys
sys.path.append(r"c:\Users\tobug\Documents\GitHub\Exercise-Inheritance\Restaurant")
from Restaurant.food.food import Food
class Starter(Food):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)
