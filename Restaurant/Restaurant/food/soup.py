from food.starter import Starter
class Soup(Starter):
    def __init__(self, name: str, price: float, gram: float) -> None:
        super().__init__(name, price, gram)