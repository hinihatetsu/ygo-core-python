from unittest import TestCase

from ygo_core.card.position import Position
from ygo_core.enums.position import PositionEnum

class TestPosition(TestCase):
	def setUp(self) -> None:
		self.position_none = Position(PositionEnum.__)
		self.position_faseup_attack = Position(PositionEnum.FASEUP_ATTACK)
		self.position_fasedown_attack = Position(PositionEnum.FASEDOWN_ATTACK)
		self.position_faseup_defence = Position(PositionEnum.FASEUP_DEFENCE)
		self.position_fasedown_defence = Position(PositionEnum.FASEDOWN_DEFENCE)
		self.position_faceup = Position(PositionEnum.FACEUP)
		self.position_facedown = Position(PositionEnum.FACEDOWN)
		self.position_attack = Position(PositionEnum.ATTACK)
		self.position_defence = Position(PositionEnum.DEFENCE)


	def test_isa_when_position_none_with_FASEUP_ATTACK(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_none_with_FASEDOWN_ATTACK(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_none_with_FASEUP_DEFENCE(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_none_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_none_with_FACEUP(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.FACEUP))


	def test_isa_when_position_none_with_FACEDOWN(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_none_with_ATTACK(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.ATTACK))


	def test_isa_when_position_none_with_DEFENCE(self) -> None:
		self.assertFalse(self.position_none.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_faseup_attack_with_FASEUP_ATTACK(self) -> None:
		self.assertTrue(self.position_faseup_attack.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_faseup_attack_with_FASEDOWN_ATTACK(self) -> None:
		self.assertFalse(self.position_faseup_attack.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_faseup_attack_with_FASEUP_DEFENCE(self) -> None:
		self.assertFalse(self.position_faseup_attack.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_faseup_attack_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertFalse(self.position_faseup_attack.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_faseup_attack_with_FACEUP(self) -> None:
		self.assertTrue(self.position_faseup_attack.isa(PositionEnum.FACEUP))


	def test_isa_when_position_faseup_attack_with_FACEDOWN(self) -> None:
		self.assertFalse(self.position_faseup_attack.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_faseup_attack_with_ATTACK(self) -> None:
		self.assertTrue(self.position_faseup_attack.isa(PositionEnum.ATTACK))


	def test_isa_when_position_faseup_attack_with_DEFENCE(self) -> None:
		self.assertFalse(self.position_faseup_attack.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_fasedown_attack_with_FASEUP_ATTACK(self) -> None:
		self.assertFalse(self.position_fasedown_attack.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_fasedown_attack_with_FASEDOWN_ATTACK(self) -> None:
		self.assertTrue(self.position_fasedown_attack.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_fasedown_attack_with_FASEUP_DEFENCE(self) -> None:
		self.assertFalse(self.position_fasedown_attack.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_fasedown_attack_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertFalse(self.position_fasedown_attack.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_fasedown_attack_with_FACEUP(self) -> None:
		self.assertFalse(self.position_fasedown_attack.isa(PositionEnum.FACEUP))


	def test_isa_when_position_fasedown_attack_with_FACEDOWN(self) -> None:
		self.assertTrue(self.position_fasedown_attack.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_fasedown_attack_with_ATTACK(self) -> None:
		self.assertTrue(self.position_fasedown_attack.isa(PositionEnum.ATTACK))


	def test_isa_when_position_fasedown_attack_with_DEFENCE(self) -> None:
		self.assertFalse(self.position_fasedown_attack.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_faseup_defence_with_FASEUP_ATTACK(self) -> None:
		self.assertFalse(self.position_faseup_defence.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_faseup_defence_with_FASEDOWN_ATTACK(self) -> None:
		self.assertFalse(self.position_faseup_defence.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_faseup_defence_with_FASEUP_DEFENCE(self) -> None:
		self.assertTrue(self.position_faseup_defence.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_faseup_defence_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertFalse(self.position_faseup_defence.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_faseup_defence_with_FACEUP(self) -> None:
		self.assertTrue(self.position_faseup_defence.isa(PositionEnum.FACEUP))


	def test_isa_when_position_faseup_defence_with_FACEDOWN(self) -> None:
		self.assertFalse(self.position_faseup_defence.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_faseup_defence_with_ATTACK(self) -> None:
		self.assertFalse(self.position_faseup_defence.isa(PositionEnum.ATTACK))


	def test_isa_when_position_faseup_defence_with_DEFENCE(self) -> None:
		self.assertTrue(self.position_faseup_defence.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_fasedown_defence_with_FASEUP_ATTACK(self) -> None:
		self.assertFalse(self.position_fasedown_defence.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_fasedown_defence_with_FASEDOWN_ATTACK(self) -> None:
		self.assertFalse(self.position_fasedown_defence.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_fasedown_defence_with_FASEUP_DEFENCE(self) -> None:
		self.assertFalse(self.position_fasedown_defence.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_fasedown_defence_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertTrue(self.position_fasedown_defence.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_fasedown_defence_with_FACEUP(self) -> None:
		self.assertFalse(self.position_fasedown_defence.isa(PositionEnum.FACEUP))


	def test_isa_when_position_fasedown_defence_with_FACEDOWN(self) -> None:
		self.assertTrue(self.position_fasedown_defence.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_fasedown_defence_with_ATTACK(self) -> None:
		self.assertFalse(self.position_fasedown_defence.isa(PositionEnum.ATTACK))


	def test_isa_when_position_fasedown_defence_with_DEFENCE(self) -> None:
		self.assertTrue(self.position_fasedown_defence.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_faceup_with_FASEUP_ATTACK(self) -> None:
		self.assertTrue(self.position_faceup.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_faceup_with_FASEDOWN_ATTACK(self) -> None:
		self.assertFalse(self.position_faceup.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_faceup_with_FASEUP_DEFENCE(self) -> None:
		self.assertTrue(self.position_faceup.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_faceup_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertFalse(self.position_faceup.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_faceup_with_FACEUP(self) -> None:
		self.assertTrue(self.position_faceup.isa(PositionEnum.FACEUP))


	def test_isa_when_position_faceup_with_FACEDOWN(self) -> None:
		self.assertFalse(self.position_faceup.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_faceup_with_ATTACK(self) -> None:
		self.assertTrue(self.position_faceup.isa(PositionEnum.ATTACK))


	def test_isa_when_position_faceup_with_DEFENCE(self) -> None:
		self.assertTrue(self.position_faceup.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_facedown_with_FASEUP_ATTACK(self) -> None:
		self.assertFalse(self.position_facedown.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_facedown_with_FASEDOWN_ATTACK(self) -> None:
		self.assertTrue(self.position_facedown.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_facedown_with_FASEUP_DEFENCE(self) -> None:
		self.assertFalse(self.position_facedown.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_facedown_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertTrue(self.position_facedown.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_facedown_with_FACEUP(self) -> None:
		self.assertFalse(self.position_facedown.isa(PositionEnum.FACEUP))


	def test_isa_when_position_facedown_with_FACEDOWN(self) -> None:
		self.assertTrue(self.position_facedown.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_facedown_with_ATTACK(self) -> None:
		self.assertTrue(self.position_facedown.isa(PositionEnum.ATTACK))


	def test_isa_when_position_facedown_with_DEFENCE(self) -> None:
		self.assertTrue(self.position_facedown.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_attack_with_FASEUP_ATTACK(self) -> None:
		self.assertTrue(self.position_attack.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_attack_with_FASEDOWN_ATTACK(self) -> None:
		self.assertTrue(self.position_attack.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_attack_with_FASEUP_DEFENCE(self) -> None:
		self.assertFalse(self.position_attack.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_attack_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertFalse(self.position_attack.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_attack_with_FACEUP(self) -> None:
		self.assertTrue(self.position_attack.isa(PositionEnum.FACEUP))


	def test_isa_when_position_attack_with_FACEDOWN(self) -> None:
		self.assertTrue(self.position_attack.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_attack_with_ATTACK(self) -> None:
		self.assertTrue(self.position_attack.isa(PositionEnum.ATTACK))


	def test_isa_when_position_attack_with_DEFENCE(self) -> None:
		self.assertFalse(self.position_attack.isa(PositionEnum.DEFENCE))


	def test_isa_when_position_defence_with_FASEUP_ATTACK(self) -> None:
		self.assertFalse(self.position_defence.isa(PositionEnum.FASEUP_ATTACK))


	def test_isa_when_position_defence_with_FASEDOWN_ATTACK(self) -> None:
		self.assertFalse(self.position_defence.isa(PositionEnum.FASEDOWN_ATTACK))


	def test_isa_when_position_defence_with_FASEUP_DEFENCE(self) -> None:
		self.assertTrue(self.position_defence.isa(PositionEnum.FASEUP_DEFENCE))


	def test_isa_when_position_defence_with_FASEDOWN_DEFENCE(self) -> None:
		self.assertTrue(self.position_defence.isa(PositionEnum.FASEDOWN_DEFENCE))


	def test_isa_when_position_defence_with_FACEUP(self) -> None:
		self.assertTrue(self.position_defence.isa(PositionEnum.FACEUP))


	def test_isa_when_position_defence_with_FACEDOWN(self) -> None:
		self.assertTrue(self.position_defence.isa(PositionEnum.FACEDOWN))


	def test_isa_when_position_defence_with_ATTACK(self) -> None:
		self.assertFalse(self.position_defence.isa(PositionEnum.ATTACK))


	def test_isa_when_position_defence_with_DEFENCE(self) -> None:
		self.assertTrue(self.position_defence.isa(PositionEnum.DEFENCE))


	def test_is_attack_when_position_none(self) -> None:
		self.assertFalse(self.position_none.is_attack())


	def test_is_attack_when_position_faseup_attack(self) -> None:
		self.assertTrue(self.position_faseup_attack.is_attack())


	def test_is_attack_when_position_fasedown_attack(self) -> None:
		self.assertTrue(self.position_fasedown_attack.is_attack())


	def test_is_attack_when_position_faseup_defence(self) -> None:
		self.assertFalse(self.position_faseup_defence.is_attack())


	def test_is_attack_when_position_fasedown_defence(self) -> None:
		self.assertFalse(self.position_fasedown_defence.is_attack())


	def test_is_attack_when_position_faceup(self) -> None:
		self.assertTrue(self.position_faceup.is_attack())


	def test_is_attack_when_position_facedown(self) -> None:
		self.assertTrue(self.position_facedown.is_attack())


	def test_is_attack_when_position_attack(self) -> None:
		self.assertTrue(self.position_attack.is_attack())


	def test_is_attack_when_position_defence(self) -> None:
		self.assertFalse(self.position_defence.is_attack())


	def test_is_defence_when_position_none(self) -> None:
		self.assertFalse(self.position_none.is_defence())


	def test_is_defence_when_position_faseup_attack(self) -> None:
		self.assertFalse(self.position_faseup_attack.is_defence())


	def test_is_defence_when_position_fasedown_attack(self) -> None:
		self.assertFalse(self.position_fasedown_attack.is_defence())


	def test_is_defence_when_position_faseup_defence(self) -> None:
		self.assertTrue(self.position_faseup_defence.is_defence())


	def test_is_defence_when_position_fasedown_defence(self) -> None:
		self.assertTrue(self.position_fasedown_defence.is_defence())


	def test_is_defence_when_position_faceup(self) -> None:
		self.assertTrue(self.position_faceup.is_defence())


	def test_is_defence_when_position_facedown(self) -> None:
		self.assertTrue(self.position_facedown.is_defence())


	def test_is_defence_when_position_attack(self) -> None:
		self.assertFalse(self.position_attack.is_defence())


	def test_is_defence_when_position_defence(self) -> None:
		self.assertTrue(self.position_defence.is_defence())


