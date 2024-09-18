from food import Food
class Dessert(Food):
    def __init__(self, name: str, price: float, grams: float,calories:float) -> None:
        super().__init__(name, price, grams)
        self.calories = calories
    def get_calories(self):
        return self.calories