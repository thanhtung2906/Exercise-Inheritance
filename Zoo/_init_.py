from gorilla import Gorilla
from snake import Snake
from lizard import Lizard
from bear import Bear
from mammal import Mammal
from reptile import Reptile
from beringel import Beringel

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
beringel = Beringel("Kong")
print(beringel.__class__.__bases__[0].__name__)
print(beringel.name)
print(beringel._Animal__name)