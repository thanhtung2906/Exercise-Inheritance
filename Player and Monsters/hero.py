class Hero:
    def __init__(self, username , level):
        self.username = username 
        self.level = level 
    def __repr__(self) -> str:
        return f'{self.username} of type {self.__class__} has level {self.level}'