import sys
sys.path.append(" c:/Users/tobug/Documents/GitHub/Exercise-Inheritance/Restaurant/Restaurant/food/food.py")
from food import Food         
                
class Main_dish(Food):
    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name, price, grams)