from food.dessert import Dessert
class Cake(Dessert):
    def __init__(self, name: str, price: float, grams: float, calories: float) -> None:
        super().__init__(name, price, grams, calories)
        self.grams= 250
        self.calories = 1000
        self.price = 5
        