from ..product import Product
class Food(Product):
    def __init__(self,name:str,price:float,gram:float) -> None:
         self.name =name 
         self.price = price 
         self.gram = gram 
         