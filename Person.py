class Person:
    def __init__(self,name,age) -> None:    
        self.name = name 
        self.age = age 
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
class Child(Person):
    pass

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)