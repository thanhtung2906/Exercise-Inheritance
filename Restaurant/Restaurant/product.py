class Product:
    def __init__(self,name:int,price:float) -> None:
        self.__name = name 
        self.__price = price
    def get_name(self):
        return self.__name
    def set_name(self):
        return self.__price
    