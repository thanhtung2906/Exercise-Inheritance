from hero import Hero
from darkknight import DarkKnight
from wizard import Wizard
from knight import Knight
from darkwizard import DarKWizard
from elf import Elf
from museelf  import MuseElf
from soulmaster import SoulMaster
from bladeknight import BladeKnight
hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)