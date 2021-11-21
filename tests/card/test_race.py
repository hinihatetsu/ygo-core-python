from unittest import TestCase

from ygo_core.card.race import Race
from ygo_core.enums.race import RaceEnum

class TestRace(TestCase):
	def setUp(self) -> None:
		self.race_none = Race(RaceEnum.__)
		self.race_warrior = Race(RaceEnum.WARRIOR)
		self.race_spellcaster = Race(RaceEnum.SPELLCASTER)
		self.race_fairy = Race(RaceEnum.FAIRY)
		self.race_fiend = Race(RaceEnum.FIEND)
		self.race_zombie = Race(RaceEnum.ZOMBIE)
		self.race_machine = Race(RaceEnum.MACHINE)
		self.race_aqua = Race(RaceEnum.AQUA)
		self.race_pyro = Race(RaceEnum.PYRO)
		self.race_rock = Race(RaceEnum.ROCK)
		self.race_wingedbeast = Race(RaceEnum.WINGEDBEAST)
		self.race_plant = Race(RaceEnum.PLANT)
		self.race_insect = Race(RaceEnum.INSECT)
		self.race_thunder = Race(RaceEnum.THUNDER)
		self.race_dragon = Race(RaceEnum.DRAGON)
		self.race_beast = Race(RaceEnum.BEAST)
		self.race_beastwarrior = Race(RaceEnum.BEASTWARRIOR)
		self.race_dinosaur = Race(RaceEnum.DINOSAUR)
		self.race_fish = Race(RaceEnum.FISH)
		self.race_seaserpent = Race(RaceEnum.SEASERPENT)
		self.race_reptile = Race(RaceEnum.REPTILE)
		self.race_psychic = Race(RaceEnum.PSYCHIC)
		self.race_divine = Race(RaceEnum.DIVINE)
		self.race_creatorgod = Race(RaceEnum.CREATORGOD)
		self.race_wyrm = Race(RaceEnum.WYRM)
		self.race_cyberse = Race(RaceEnum.CYBERSE)


	def test_isa_when_race_none_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_none_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_none_with_FAIRY(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.FAIRY))


	def test_isa_when_race_none_with_FIEND(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.FIEND))


	def test_isa_when_race_none_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_none_with_MACHINE(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.MACHINE))


	def test_isa_when_race_none_with_AQUA(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.AQUA))


	def test_isa_when_race_none_with_PYRO(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.PYRO))


	def test_isa_when_race_none_with_ROCK(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.ROCK))


	def test_isa_when_race_none_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_none_with_PLANT(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.PLANT))


	def test_isa_when_race_none_with_INSECT(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.INSECT))


	def test_isa_when_race_none_with_THUNDER(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.THUNDER))


	def test_isa_when_race_none_with_DRAGON(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.DRAGON))


	def test_isa_when_race_none_with_BEAST(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.BEAST))


	def test_isa_when_race_none_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_none_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_none_with_FISH(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.FISH))


	def test_isa_when_race_none_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_none_with_REPTILE(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.REPTILE))


	def test_isa_when_race_none_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_none_with_DIVINE(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.DIVINE))


	def test_isa_when_race_none_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_none_with_WYRM(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.WYRM))


	def test_isa_when_race_none_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_none.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_warrior_with_WARRIOR(self) -> None:
		self.assertTrue(self.race_warrior.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_warrior_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_warrior_with_FAIRY(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.FAIRY))


	def test_isa_when_race_warrior_with_FIEND(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.FIEND))


	def test_isa_when_race_warrior_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_warrior_with_MACHINE(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.MACHINE))


	def test_isa_when_race_warrior_with_AQUA(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.AQUA))


	def test_isa_when_race_warrior_with_PYRO(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.PYRO))


	def test_isa_when_race_warrior_with_ROCK(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.ROCK))


	def test_isa_when_race_warrior_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_warrior_with_PLANT(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.PLANT))


	def test_isa_when_race_warrior_with_INSECT(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.INSECT))


	def test_isa_when_race_warrior_with_THUNDER(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.THUNDER))


	def test_isa_when_race_warrior_with_DRAGON(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.DRAGON))


	def test_isa_when_race_warrior_with_BEAST(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.BEAST))


	def test_isa_when_race_warrior_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_warrior_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_warrior_with_FISH(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.FISH))


	def test_isa_when_race_warrior_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_warrior_with_REPTILE(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.REPTILE))


	def test_isa_when_race_warrior_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_warrior_with_DIVINE(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.DIVINE))


	def test_isa_when_race_warrior_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_warrior_with_WYRM(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.WYRM))


	def test_isa_when_race_warrior_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_warrior.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_spellcaster_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_spellcaster_with_SPELLCASTER(self) -> None:
		self.assertTrue(self.race_spellcaster.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_spellcaster_with_FAIRY(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.FAIRY))


	def test_isa_when_race_spellcaster_with_FIEND(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.FIEND))


	def test_isa_when_race_spellcaster_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_spellcaster_with_MACHINE(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.MACHINE))


	def test_isa_when_race_spellcaster_with_AQUA(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.AQUA))


	def test_isa_when_race_spellcaster_with_PYRO(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.PYRO))


	def test_isa_when_race_spellcaster_with_ROCK(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.ROCK))


	def test_isa_when_race_spellcaster_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_spellcaster_with_PLANT(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.PLANT))


	def test_isa_when_race_spellcaster_with_INSECT(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.INSECT))


	def test_isa_when_race_spellcaster_with_THUNDER(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.THUNDER))


	def test_isa_when_race_spellcaster_with_DRAGON(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.DRAGON))


	def test_isa_when_race_spellcaster_with_BEAST(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.BEAST))


	def test_isa_when_race_spellcaster_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_spellcaster_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_spellcaster_with_FISH(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.FISH))


	def test_isa_when_race_spellcaster_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_spellcaster_with_REPTILE(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.REPTILE))


	def test_isa_when_race_spellcaster_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_spellcaster_with_DIVINE(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.DIVINE))


	def test_isa_when_race_spellcaster_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_spellcaster_with_WYRM(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.WYRM))


	def test_isa_when_race_spellcaster_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_spellcaster.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_fairy_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_fairy_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_fairy_with_FAIRY(self) -> None:
		self.assertTrue(self.race_fairy.isa(RaceEnum.FAIRY))


	def test_isa_when_race_fairy_with_FIEND(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.FIEND))


	def test_isa_when_race_fairy_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_fairy_with_MACHINE(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.MACHINE))


	def test_isa_when_race_fairy_with_AQUA(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.AQUA))


	def test_isa_when_race_fairy_with_PYRO(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.PYRO))


	def test_isa_when_race_fairy_with_ROCK(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.ROCK))


	def test_isa_when_race_fairy_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_fairy_with_PLANT(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.PLANT))


	def test_isa_when_race_fairy_with_INSECT(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.INSECT))


	def test_isa_when_race_fairy_with_THUNDER(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.THUNDER))


	def test_isa_when_race_fairy_with_DRAGON(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.DRAGON))


	def test_isa_when_race_fairy_with_BEAST(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.BEAST))


	def test_isa_when_race_fairy_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_fairy_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_fairy_with_FISH(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.FISH))


	def test_isa_when_race_fairy_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_fairy_with_REPTILE(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.REPTILE))


	def test_isa_when_race_fairy_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_fairy_with_DIVINE(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.DIVINE))


	def test_isa_when_race_fairy_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_fairy_with_WYRM(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.WYRM))


	def test_isa_when_race_fairy_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_fairy.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_fiend_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_fiend_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_fiend_with_FAIRY(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.FAIRY))


	def test_isa_when_race_fiend_with_FIEND(self) -> None:
		self.assertTrue(self.race_fiend.isa(RaceEnum.FIEND))


	def test_isa_when_race_fiend_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_fiend_with_MACHINE(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.MACHINE))


	def test_isa_when_race_fiend_with_AQUA(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.AQUA))


	def test_isa_when_race_fiend_with_PYRO(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.PYRO))


	def test_isa_when_race_fiend_with_ROCK(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.ROCK))


	def test_isa_when_race_fiend_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_fiend_with_PLANT(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.PLANT))


	def test_isa_when_race_fiend_with_INSECT(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.INSECT))


	def test_isa_when_race_fiend_with_THUNDER(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.THUNDER))


	def test_isa_when_race_fiend_with_DRAGON(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.DRAGON))


	def test_isa_when_race_fiend_with_BEAST(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.BEAST))


	def test_isa_when_race_fiend_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_fiend_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_fiend_with_FISH(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.FISH))


	def test_isa_when_race_fiend_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_fiend_with_REPTILE(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.REPTILE))


	def test_isa_when_race_fiend_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_fiend_with_DIVINE(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.DIVINE))


	def test_isa_when_race_fiend_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_fiend_with_WYRM(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.WYRM))


	def test_isa_when_race_fiend_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_fiend.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_zombie_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_zombie_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_zombie_with_FAIRY(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.FAIRY))


	def test_isa_when_race_zombie_with_FIEND(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.FIEND))


	def test_isa_when_race_zombie_with_ZOMBIE(self) -> None:
		self.assertTrue(self.race_zombie.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_zombie_with_MACHINE(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.MACHINE))


	def test_isa_when_race_zombie_with_AQUA(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.AQUA))


	def test_isa_when_race_zombie_with_PYRO(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.PYRO))


	def test_isa_when_race_zombie_with_ROCK(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.ROCK))


	def test_isa_when_race_zombie_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_zombie_with_PLANT(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.PLANT))


	def test_isa_when_race_zombie_with_INSECT(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.INSECT))


	def test_isa_when_race_zombie_with_THUNDER(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.THUNDER))


	def test_isa_when_race_zombie_with_DRAGON(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.DRAGON))


	def test_isa_when_race_zombie_with_BEAST(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.BEAST))


	def test_isa_when_race_zombie_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_zombie_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_zombie_with_FISH(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.FISH))


	def test_isa_when_race_zombie_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_zombie_with_REPTILE(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.REPTILE))


	def test_isa_when_race_zombie_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_zombie_with_DIVINE(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.DIVINE))


	def test_isa_when_race_zombie_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_zombie_with_WYRM(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.WYRM))


	def test_isa_when_race_zombie_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_zombie.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_machine_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_machine_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_machine_with_FAIRY(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.FAIRY))


	def test_isa_when_race_machine_with_FIEND(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.FIEND))


	def test_isa_when_race_machine_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_machine_with_MACHINE(self) -> None:
		self.assertTrue(self.race_machine.isa(RaceEnum.MACHINE))


	def test_isa_when_race_machine_with_AQUA(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.AQUA))


	def test_isa_when_race_machine_with_PYRO(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.PYRO))


	def test_isa_when_race_machine_with_ROCK(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.ROCK))


	def test_isa_when_race_machine_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_machine_with_PLANT(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.PLANT))


	def test_isa_when_race_machine_with_INSECT(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.INSECT))


	def test_isa_when_race_machine_with_THUNDER(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.THUNDER))


	def test_isa_when_race_machine_with_DRAGON(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.DRAGON))


	def test_isa_when_race_machine_with_BEAST(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.BEAST))


	def test_isa_when_race_machine_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_machine_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_machine_with_FISH(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.FISH))


	def test_isa_when_race_machine_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_machine_with_REPTILE(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.REPTILE))


	def test_isa_when_race_machine_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_machine_with_DIVINE(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.DIVINE))


	def test_isa_when_race_machine_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_machine_with_WYRM(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.WYRM))


	def test_isa_when_race_machine_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_machine.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_aqua_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_aqua_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_aqua_with_FAIRY(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.FAIRY))


	def test_isa_when_race_aqua_with_FIEND(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.FIEND))


	def test_isa_when_race_aqua_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_aqua_with_MACHINE(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.MACHINE))


	def test_isa_when_race_aqua_with_AQUA(self) -> None:
		self.assertTrue(self.race_aqua.isa(RaceEnum.AQUA))


	def test_isa_when_race_aqua_with_PYRO(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.PYRO))


	def test_isa_when_race_aqua_with_ROCK(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.ROCK))


	def test_isa_when_race_aqua_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_aqua_with_PLANT(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.PLANT))


	def test_isa_when_race_aqua_with_INSECT(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.INSECT))


	def test_isa_when_race_aqua_with_THUNDER(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.THUNDER))


	def test_isa_when_race_aqua_with_DRAGON(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.DRAGON))


	def test_isa_when_race_aqua_with_BEAST(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.BEAST))


	def test_isa_when_race_aqua_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_aqua_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_aqua_with_FISH(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.FISH))


	def test_isa_when_race_aqua_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_aqua_with_REPTILE(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.REPTILE))


	def test_isa_when_race_aqua_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_aqua_with_DIVINE(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.DIVINE))


	def test_isa_when_race_aqua_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_aqua_with_WYRM(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.WYRM))


	def test_isa_when_race_aqua_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_aqua.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_pyro_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_pyro_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_pyro_with_FAIRY(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.FAIRY))


	def test_isa_when_race_pyro_with_FIEND(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.FIEND))


	def test_isa_when_race_pyro_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_pyro_with_MACHINE(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.MACHINE))


	def test_isa_when_race_pyro_with_AQUA(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.AQUA))


	def test_isa_when_race_pyro_with_PYRO(self) -> None:
		self.assertTrue(self.race_pyro.isa(RaceEnum.PYRO))


	def test_isa_when_race_pyro_with_ROCK(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.ROCK))


	def test_isa_when_race_pyro_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_pyro_with_PLANT(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.PLANT))


	def test_isa_when_race_pyro_with_INSECT(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.INSECT))


	def test_isa_when_race_pyro_with_THUNDER(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.THUNDER))


	def test_isa_when_race_pyro_with_DRAGON(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.DRAGON))


	def test_isa_when_race_pyro_with_BEAST(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.BEAST))


	def test_isa_when_race_pyro_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_pyro_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_pyro_with_FISH(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.FISH))


	def test_isa_when_race_pyro_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_pyro_with_REPTILE(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.REPTILE))


	def test_isa_when_race_pyro_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_pyro_with_DIVINE(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.DIVINE))


	def test_isa_when_race_pyro_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_pyro_with_WYRM(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.WYRM))


	def test_isa_when_race_pyro_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_pyro.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_rock_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_rock_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_rock_with_FAIRY(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.FAIRY))


	def test_isa_when_race_rock_with_FIEND(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.FIEND))


	def test_isa_when_race_rock_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_rock_with_MACHINE(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.MACHINE))


	def test_isa_when_race_rock_with_AQUA(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.AQUA))


	def test_isa_when_race_rock_with_PYRO(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.PYRO))


	def test_isa_when_race_rock_with_ROCK(self) -> None:
		self.assertTrue(self.race_rock.isa(RaceEnum.ROCK))


	def test_isa_when_race_rock_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_rock_with_PLANT(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.PLANT))


	def test_isa_when_race_rock_with_INSECT(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.INSECT))


	def test_isa_when_race_rock_with_THUNDER(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.THUNDER))


	def test_isa_when_race_rock_with_DRAGON(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.DRAGON))


	def test_isa_when_race_rock_with_BEAST(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.BEAST))


	def test_isa_when_race_rock_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_rock_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_rock_with_FISH(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.FISH))


	def test_isa_when_race_rock_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_rock_with_REPTILE(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.REPTILE))


	def test_isa_when_race_rock_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_rock_with_DIVINE(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.DIVINE))


	def test_isa_when_race_rock_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_rock_with_WYRM(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.WYRM))


	def test_isa_when_race_rock_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_rock.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_wingedbeast_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_wingedbeast_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_wingedbeast_with_FAIRY(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.FAIRY))


	def test_isa_when_race_wingedbeast_with_FIEND(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.FIEND))


	def test_isa_when_race_wingedbeast_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_wingedbeast_with_MACHINE(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.MACHINE))


	def test_isa_when_race_wingedbeast_with_AQUA(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.AQUA))


	def test_isa_when_race_wingedbeast_with_PYRO(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.PYRO))


	def test_isa_when_race_wingedbeast_with_ROCK(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.ROCK))


	def test_isa_when_race_wingedbeast_with_WINGEDBEAST(self) -> None:
		self.assertTrue(self.race_wingedbeast.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_wingedbeast_with_PLANT(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.PLANT))


	def test_isa_when_race_wingedbeast_with_INSECT(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.INSECT))


	def test_isa_when_race_wingedbeast_with_THUNDER(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.THUNDER))


	def test_isa_when_race_wingedbeast_with_DRAGON(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.DRAGON))


	def test_isa_when_race_wingedbeast_with_BEAST(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.BEAST))


	def test_isa_when_race_wingedbeast_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_wingedbeast_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_wingedbeast_with_FISH(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.FISH))


	def test_isa_when_race_wingedbeast_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_wingedbeast_with_REPTILE(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.REPTILE))


	def test_isa_when_race_wingedbeast_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_wingedbeast_with_DIVINE(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.DIVINE))


	def test_isa_when_race_wingedbeast_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_wingedbeast_with_WYRM(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.WYRM))


	def test_isa_when_race_wingedbeast_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_wingedbeast.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_plant_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_plant_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_plant_with_FAIRY(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.FAIRY))


	def test_isa_when_race_plant_with_FIEND(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.FIEND))


	def test_isa_when_race_plant_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_plant_with_MACHINE(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.MACHINE))


	def test_isa_when_race_plant_with_AQUA(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.AQUA))


	def test_isa_when_race_plant_with_PYRO(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.PYRO))


	def test_isa_when_race_plant_with_ROCK(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.ROCK))


	def test_isa_when_race_plant_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_plant_with_PLANT(self) -> None:
		self.assertTrue(self.race_plant.isa(RaceEnum.PLANT))


	def test_isa_when_race_plant_with_INSECT(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.INSECT))


	def test_isa_when_race_plant_with_THUNDER(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.THUNDER))


	def test_isa_when_race_plant_with_DRAGON(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.DRAGON))


	def test_isa_when_race_plant_with_BEAST(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.BEAST))


	def test_isa_when_race_plant_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_plant_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_plant_with_FISH(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.FISH))


	def test_isa_when_race_plant_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_plant_with_REPTILE(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.REPTILE))


	def test_isa_when_race_plant_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_plant_with_DIVINE(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.DIVINE))


	def test_isa_when_race_plant_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_plant_with_WYRM(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.WYRM))


	def test_isa_when_race_plant_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_plant.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_insect_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_insect_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_insect_with_FAIRY(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.FAIRY))


	def test_isa_when_race_insect_with_FIEND(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.FIEND))


	def test_isa_when_race_insect_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_insect_with_MACHINE(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.MACHINE))


	def test_isa_when_race_insect_with_AQUA(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.AQUA))


	def test_isa_when_race_insect_with_PYRO(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.PYRO))


	def test_isa_when_race_insect_with_ROCK(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.ROCK))


	def test_isa_when_race_insect_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_insect_with_PLANT(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.PLANT))


	def test_isa_when_race_insect_with_INSECT(self) -> None:
		self.assertTrue(self.race_insect.isa(RaceEnum.INSECT))


	def test_isa_when_race_insect_with_THUNDER(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.THUNDER))


	def test_isa_when_race_insect_with_DRAGON(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.DRAGON))


	def test_isa_when_race_insect_with_BEAST(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.BEAST))


	def test_isa_when_race_insect_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_insect_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_insect_with_FISH(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.FISH))


	def test_isa_when_race_insect_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_insect_with_REPTILE(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.REPTILE))


	def test_isa_when_race_insect_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_insect_with_DIVINE(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.DIVINE))


	def test_isa_when_race_insect_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_insect_with_WYRM(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.WYRM))


	def test_isa_when_race_insect_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_insect.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_thunder_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_thunder_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_thunder_with_FAIRY(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.FAIRY))


	def test_isa_when_race_thunder_with_FIEND(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.FIEND))


	def test_isa_when_race_thunder_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_thunder_with_MACHINE(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.MACHINE))


	def test_isa_when_race_thunder_with_AQUA(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.AQUA))


	def test_isa_when_race_thunder_with_PYRO(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.PYRO))


	def test_isa_when_race_thunder_with_ROCK(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.ROCK))


	def test_isa_when_race_thunder_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_thunder_with_PLANT(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.PLANT))


	def test_isa_when_race_thunder_with_INSECT(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.INSECT))


	def test_isa_when_race_thunder_with_THUNDER(self) -> None:
		self.assertTrue(self.race_thunder.isa(RaceEnum.THUNDER))


	def test_isa_when_race_thunder_with_DRAGON(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.DRAGON))


	def test_isa_when_race_thunder_with_BEAST(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.BEAST))


	def test_isa_when_race_thunder_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_thunder_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_thunder_with_FISH(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.FISH))


	def test_isa_when_race_thunder_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_thunder_with_REPTILE(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.REPTILE))


	def test_isa_when_race_thunder_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_thunder_with_DIVINE(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.DIVINE))


	def test_isa_when_race_thunder_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_thunder_with_WYRM(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.WYRM))


	def test_isa_when_race_thunder_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_thunder.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_dragon_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_dragon_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_dragon_with_FAIRY(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.FAIRY))


	def test_isa_when_race_dragon_with_FIEND(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.FIEND))


	def test_isa_when_race_dragon_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_dragon_with_MACHINE(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.MACHINE))


	def test_isa_when_race_dragon_with_AQUA(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.AQUA))


	def test_isa_when_race_dragon_with_PYRO(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.PYRO))


	def test_isa_when_race_dragon_with_ROCK(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.ROCK))


	def test_isa_when_race_dragon_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_dragon_with_PLANT(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.PLANT))


	def test_isa_when_race_dragon_with_INSECT(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.INSECT))


	def test_isa_when_race_dragon_with_THUNDER(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.THUNDER))


	def test_isa_when_race_dragon_with_DRAGON(self) -> None:
		self.assertTrue(self.race_dragon.isa(RaceEnum.DRAGON))


	def test_isa_when_race_dragon_with_BEAST(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.BEAST))


	def test_isa_when_race_dragon_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_dragon_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_dragon_with_FISH(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.FISH))


	def test_isa_when_race_dragon_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_dragon_with_REPTILE(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.REPTILE))


	def test_isa_when_race_dragon_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_dragon_with_DIVINE(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.DIVINE))


	def test_isa_when_race_dragon_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_dragon_with_WYRM(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.WYRM))


	def test_isa_when_race_dragon_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_dragon.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_beast_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_beast_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_beast_with_FAIRY(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.FAIRY))


	def test_isa_when_race_beast_with_FIEND(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.FIEND))


	def test_isa_when_race_beast_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_beast_with_MACHINE(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.MACHINE))


	def test_isa_when_race_beast_with_AQUA(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.AQUA))


	def test_isa_when_race_beast_with_PYRO(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.PYRO))


	def test_isa_when_race_beast_with_ROCK(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.ROCK))


	def test_isa_when_race_beast_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_beast_with_PLANT(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.PLANT))


	def test_isa_when_race_beast_with_INSECT(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.INSECT))


	def test_isa_when_race_beast_with_THUNDER(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.THUNDER))


	def test_isa_when_race_beast_with_DRAGON(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.DRAGON))


	def test_isa_when_race_beast_with_BEAST(self) -> None:
		self.assertTrue(self.race_beast.isa(RaceEnum.BEAST))


	def test_isa_when_race_beast_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_beast_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_beast_with_FISH(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.FISH))


	def test_isa_when_race_beast_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_beast_with_REPTILE(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.REPTILE))


	def test_isa_when_race_beast_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_beast_with_DIVINE(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.DIVINE))


	def test_isa_when_race_beast_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_beast_with_WYRM(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.WYRM))


	def test_isa_when_race_beast_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_beast.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_beastwarrior_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_beastwarrior_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_beastwarrior_with_FAIRY(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.FAIRY))


	def test_isa_when_race_beastwarrior_with_FIEND(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.FIEND))


	def test_isa_when_race_beastwarrior_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_beastwarrior_with_MACHINE(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.MACHINE))


	def test_isa_when_race_beastwarrior_with_AQUA(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.AQUA))


	def test_isa_when_race_beastwarrior_with_PYRO(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.PYRO))


	def test_isa_when_race_beastwarrior_with_ROCK(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.ROCK))


	def test_isa_when_race_beastwarrior_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_beastwarrior_with_PLANT(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.PLANT))


	def test_isa_when_race_beastwarrior_with_INSECT(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.INSECT))


	def test_isa_when_race_beastwarrior_with_THUNDER(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.THUNDER))


	def test_isa_when_race_beastwarrior_with_DRAGON(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.DRAGON))


	def test_isa_when_race_beastwarrior_with_BEAST(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.BEAST))


	def test_isa_when_race_beastwarrior_with_BEASTWARRIOR(self) -> None:
		self.assertTrue(self.race_beastwarrior.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_beastwarrior_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_beastwarrior_with_FISH(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.FISH))


	def test_isa_when_race_beastwarrior_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_beastwarrior_with_REPTILE(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.REPTILE))


	def test_isa_when_race_beastwarrior_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_beastwarrior_with_DIVINE(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.DIVINE))


	def test_isa_when_race_beastwarrior_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_beastwarrior_with_WYRM(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.WYRM))


	def test_isa_when_race_beastwarrior_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_beastwarrior.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_dinosaur_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_dinosaur_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_dinosaur_with_FAIRY(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.FAIRY))


	def test_isa_when_race_dinosaur_with_FIEND(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.FIEND))


	def test_isa_when_race_dinosaur_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_dinosaur_with_MACHINE(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.MACHINE))


	def test_isa_when_race_dinosaur_with_AQUA(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.AQUA))


	def test_isa_when_race_dinosaur_with_PYRO(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.PYRO))


	def test_isa_when_race_dinosaur_with_ROCK(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.ROCK))


	def test_isa_when_race_dinosaur_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_dinosaur_with_PLANT(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.PLANT))


	def test_isa_when_race_dinosaur_with_INSECT(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.INSECT))


	def test_isa_when_race_dinosaur_with_THUNDER(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.THUNDER))


	def test_isa_when_race_dinosaur_with_DRAGON(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.DRAGON))


	def test_isa_when_race_dinosaur_with_BEAST(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.BEAST))


	def test_isa_when_race_dinosaur_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_dinosaur_with_DINOSAUR(self) -> None:
		self.assertTrue(self.race_dinosaur.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_dinosaur_with_FISH(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.FISH))


	def test_isa_when_race_dinosaur_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_dinosaur_with_REPTILE(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.REPTILE))


	def test_isa_when_race_dinosaur_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_dinosaur_with_DIVINE(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.DIVINE))


	def test_isa_when_race_dinosaur_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_dinosaur_with_WYRM(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.WYRM))


	def test_isa_when_race_dinosaur_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_dinosaur.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_fish_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_fish_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_fish_with_FAIRY(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.FAIRY))


	def test_isa_when_race_fish_with_FIEND(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.FIEND))


	def test_isa_when_race_fish_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_fish_with_MACHINE(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.MACHINE))


	def test_isa_when_race_fish_with_AQUA(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.AQUA))


	def test_isa_when_race_fish_with_PYRO(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.PYRO))


	def test_isa_when_race_fish_with_ROCK(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.ROCK))


	def test_isa_when_race_fish_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_fish_with_PLANT(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.PLANT))


	def test_isa_when_race_fish_with_INSECT(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.INSECT))


	def test_isa_when_race_fish_with_THUNDER(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.THUNDER))


	def test_isa_when_race_fish_with_DRAGON(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.DRAGON))


	def test_isa_when_race_fish_with_BEAST(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.BEAST))


	def test_isa_when_race_fish_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_fish_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_fish_with_FISH(self) -> None:
		self.assertTrue(self.race_fish.isa(RaceEnum.FISH))


	def test_isa_when_race_fish_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_fish_with_REPTILE(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.REPTILE))


	def test_isa_when_race_fish_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_fish_with_DIVINE(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.DIVINE))


	def test_isa_when_race_fish_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_fish_with_WYRM(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.WYRM))


	def test_isa_when_race_fish_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_fish.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_seaserpent_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_seaserpent_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_seaserpent_with_FAIRY(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.FAIRY))


	def test_isa_when_race_seaserpent_with_FIEND(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.FIEND))


	def test_isa_when_race_seaserpent_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_seaserpent_with_MACHINE(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.MACHINE))


	def test_isa_when_race_seaserpent_with_AQUA(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.AQUA))


	def test_isa_when_race_seaserpent_with_PYRO(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.PYRO))


	def test_isa_when_race_seaserpent_with_ROCK(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.ROCK))


	def test_isa_when_race_seaserpent_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_seaserpent_with_PLANT(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.PLANT))


	def test_isa_when_race_seaserpent_with_INSECT(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.INSECT))


	def test_isa_when_race_seaserpent_with_THUNDER(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.THUNDER))


	def test_isa_when_race_seaserpent_with_DRAGON(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.DRAGON))


	def test_isa_when_race_seaserpent_with_BEAST(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.BEAST))


	def test_isa_when_race_seaserpent_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_seaserpent_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_seaserpent_with_FISH(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.FISH))


	def test_isa_when_race_seaserpent_with_SEASERPENT(self) -> None:
		self.assertTrue(self.race_seaserpent.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_seaserpent_with_REPTILE(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.REPTILE))


	def test_isa_when_race_seaserpent_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_seaserpent_with_DIVINE(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.DIVINE))


	def test_isa_when_race_seaserpent_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_seaserpent_with_WYRM(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.WYRM))


	def test_isa_when_race_seaserpent_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_seaserpent.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_reptile_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_reptile_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_reptile_with_FAIRY(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.FAIRY))


	def test_isa_when_race_reptile_with_FIEND(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.FIEND))


	def test_isa_when_race_reptile_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_reptile_with_MACHINE(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.MACHINE))


	def test_isa_when_race_reptile_with_AQUA(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.AQUA))


	def test_isa_when_race_reptile_with_PYRO(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.PYRO))


	def test_isa_when_race_reptile_with_ROCK(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.ROCK))


	def test_isa_when_race_reptile_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_reptile_with_PLANT(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.PLANT))


	def test_isa_when_race_reptile_with_INSECT(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.INSECT))


	def test_isa_when_race_reptile_with_THUNDER(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.THUNDER))


	def test_isa_when_race_reptile_with_DRAGON(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.DRAGON))


	def test_isa_when_race_reptile_with_BEAST(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.BEAST))


	def test_isa_when_race_reptile_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_reptile_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_reptile_with_FISH(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.FISH))


	def test_isa_when_race_reptile_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_reptile_with_REPTILE(self) -> None:
		self.assertTrue(self.race_reptile.isa(RaceEnum.REPTILE))


	def test_isa_when_race_reptile_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_reptile_with_DIVINE(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.DIVINE))


	def test_isa_when_race_reptile_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_reptile_with_WYRM(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.WYRM))


	def test_isa_when_race_reptile_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_reptile.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_psychic_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_psychic_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_psychic_with_FAIRY(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.FAIRY))


	def test_isa_when_race_psychic_with_FIEND(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.FIEND))


	def test_isa_when_race_psychic_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_psychic_with_MACHINE(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.MACHINE))


	def test_isa_when_race_psychic_with_AQUA(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.AQUA))


	def test_isa_when_race_psychic_with_PYRO(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.PYRO))


	def test_isa_when_race_psychic_with_ROCK(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.ROCK))


	def test_isa_when_race_psychic_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_psychic_with_PLANT(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.PLANT))


	def test_isa_when_race_psychic_with_INSECT(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.INSECT))


	def test_isa_when_race_psychic_with_THUNDER(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.THUNDER))


	def test_isa_when_race_psychic_with_DRAGON(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.DRAGON))


	def test_isa_when_race_psychic_with_BEAST(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.BEAST))


	def test_isa_when_race_psychic_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_psychic_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_psychic_with_FISH(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.FISH))


	def test_isa_when_race_psychic_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_psychic_with_REPTILE(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.REPTILE))


	def test_isa_when_race_psychic_with_PSYCHIC(self) -> None:
		self.assertTrue(self.race_psychic.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_psychic_with_DIVINE(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.DIVINE))


	def test_isa_when_race_psychic_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_psychic_with_WYRM(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.WYRM))


	def test_isa_when_race_psychic_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_psychic.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_divine_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_divine_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_divine_with_FAIRY(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.FAIRY))


	def test_isa_when_race_divine_with_FIEND(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.FIEND))


	def test_isa_when_race_divine_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_divine_with_MACHINE(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.MACHINE))


	def test_isa_when_race_divine_with_AQUA(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.AQUA))


	def test_isa_when_race_divine_with_PYRO(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.PYRO))


	def test_isa_when_race_divine_with_ROCK(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.ROCK))


	def test_isa_when_race_divine_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_divine_with_PLANT(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.PLANT))


	def test_isa_when_race_divine_with_INSECT(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.INSECT))


	def test_isa_when_race_divine_with_THUNDER(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.THUNDER))


	def test_isa_when_race_divine_with_DRAGON(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.DRAGON))


	def test_isa_when_race_divine_with_BEAST(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.BEAST))


	def test_isa_when_race_divine_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_divine_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_divine_with_FISH(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.FISH))


	def test_isa_when_race_divine_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_divine_with_REPTILE(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.REPTILE))


	def test_isa_when_race_divine_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_divine_with_DIVINE(self) -> None:
		self.assertTrue(self.race_divine.isa(RaceEnum.DIVINE))


	def test_isa_when_race_divine_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_divine_with_WYRM(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.WYRM))


	def test_isa_when_race_divine_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_divine.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_creatorgod_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_creatorgod_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_creatorgod_with_FAIRY(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.FAIRY))


	def test_isa_when_race_creatorgod_with_FIEND(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.FIEND))


	def test_isa_when_race_creatorgod_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_creatorgod_with_MACHINE(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.MACHINE))


	def test_isa_when_race_creatorgod_with_AQUA(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.AQUA))


	def test_isa_when_race_creatorgod_with_PYRO(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.PYRO))


	def test_isa_when_race_creatorgod_with_ROCK(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.ROCK))


	def test_isa_when_race_creatorgod_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_creatorgod_with_PLANT(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.PLANT))


	def test_isa_when_race_creatorgod_with_INSECT(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.INSECT))


	def test_isa_when_race_creatorgod_with_THUNDER(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.THUNDER))


	def test_isa_when_race_creatorgod_with_DRAGON(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.DRAGON))


	def test_isa_when_race_creatorgod_with_BEAST(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.BEAST))


	def test_isa_when_race_creatorgod_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_creatorgod_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_creatorgod_with_FISH(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.FISH))


	def test_isa_when_race_creatorgod_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_creatorgod_with_REPTILE(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.REPTILE))


	def test_isa_when_race_creatorgod_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_creatorgod_with_DIVINE(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.DIVINE))


	def test_isa_when_race_creatorgod_with_CREATORGOD(self) -> None:
		self.assertTrue(self.race_creatorgod.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_creatorgod_with_WYRM(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.WYRM))


	def test_isa_when_race_creatorgod_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_creatorgod.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_wyrm_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_wyrm_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_wyrm_with_FAIRY(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.FAIRY))


	def test_isa_when_race_wyrm_with_FIEND(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.FIEND))


	def test_isa_when_race_wyrm_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_wyrm_with_MACHINE(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.MACHINE))


	def test_isa_when_race_wyrm_with_AQUA(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.AQUA))


	def test_isa_when_race_wyrm_with_PYRO(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.PYRO))


	def test_isa_when_race_wyrm_with_ROCK(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.ROCK))


	def test_isa_when_race_wyrm_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_wyrm_with_PLANT(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.PLANT))


	def test_isa_when_race_wyrm_with_INSECT(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.INSECT))


	def test_isa_when_race_wyrm_with_THUNDER(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.THUNDER))


	def test_isa_when_race_wyrm_with_DRAGON(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.DRAGON))


	def test_isa_when_race_wyrm_with_BEAST(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.BEAST))


	def test_isa_when_race_wyrm_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_wyrm_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_wyrm_with_FISH(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.FISH))


	def test_isa_when_race_wyrm_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_wyrm_with_REPTILE(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.REPTILE))


	def test_isa_when_race_wyrm_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_wyrm_with_DIVINE(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.DIVINE))


	def test_isa_when_race_wyrm_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_wyrm_with_WYRM(self) -> None:
		self.assertTrue(self.race_wyrm.isa(RaceEnum.WYRM))


	def test_isa_when_race_wyrm_with_CYBERSE(self) -> None:
		self.assertFalse(self.race_wyrm.isa(RaceEnum.CYBERSE))


	def test_isa_when_race_cyberse_with_WARRIOR(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.WARRIOR))


	def test_isa_when_race_cyberse_with_SPELLCASTER(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.SPELLCASTER))


	def test_isa_when_race_cyberse_with_FAIRY(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.FAIRY))


	def test_isa_when_race_cyberse_with_FIEND(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.FIEND))


	def test_isa_when_race_cyberse_with_ZOMBIE(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.ZOMBIE))


	def test_isa_when_race_cyberse_with_MACHINE(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.MACHINE))


	def test_isa_when_race_cyberse_with_AQUA(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.AQUA))


	def test_isa_when_race_cyberse_with_PYRO(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.PYRO))


	def test_isa_when_race_cyberse_with_ROCK(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.ROCK))


	def test_isa_when_race_cyberse_with_WINGEDBEAST(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.WINGEDBEAST))


	def test_isa_when_race_cyberse_with_PLANT(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.PLANT))


	def test_isa_when_race_cyberse_with_INSECT(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.INSECT))


	def test_isa_when_race_cyberse_with_THUNDER(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.THUNDER))


	def test_isa_when_race_cyberse_with_DRAGON(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.DRAGON))


	def test_isa_when_race_cyberse_with_BEAST(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.BEAST))


	def test_isa_when_race_cyberse_with_BEASTWARRIOR(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.BEASTWARRIOR))


	def test_isa_when_race_cyberse_with_DINOSAUR(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.DINOSAUR))


	def test_isa_when_race_cyberse_with_FISH(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.FISH))


	def test_isa_when_race_cyberse_with_SEASERPENT(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.SEASERPENT))


	def test_isa_when_race_cyberse_with_REPTILE(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.REPTILE))


	def test_isa_when_race_cyberse_with_PSYCHIC(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.PSYCHIC))


	def test_isa_when_race_cyberse_with_DIVINE(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.DIVINE))


	def test_isa_when_race_cyberse_with_CREATORGOD(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.CREATORGOD))


	def test_isa_when_race_cyberse_with_WYRM(self) -> None:
		self.assertFalse(self.race_cyberse.isa(RaceEnum.WYRM))


	def test_isa_when_race_cyberse_with_CYBERSE(self) -> None:
		self.assertTrue(self.race_cyberse.isa(RaceEnum.CYBERSE))


