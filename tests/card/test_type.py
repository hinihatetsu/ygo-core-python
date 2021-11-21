from unittest import TestCase

from ygo_core.card.type import Type
from ygo_core.enums.type import TypeEnum

class TestType(TestCase):
	def setUp(self) -> None:
		self.type_none = Type(TypeEnum.__)
		self.type_monster = Type(TypeEnum.MONSTER)
		self.type_spell = Type(TypeEnum.SPELL)
		self.type_trap = Type(TypeEnum.TRAP)
		self.type_normal = Type(TypeEnum.NORMAL)
		self.type_effect = Type(TypeEnum.EFFECT)
		self.type_fusion = Type(TypeEnum.FUSION)
		self.type_ritual = Type(TypeEnum.RITUAL)
		self.type_trapmonster = Type(TypeEnum.TRAPMONSTER)
		self.type_spirit = Type(TypeEnum.SPIRIT)
		self.type_union = Type(TypeEnum.UNION)
		self.type_gemini = Type(TypeEnum.GEMINI)
		self.type_tuner = Type(TypeEnum.TUNER)
		self.type_synchro = Type(TypeEnum.SYNCHRO)
		self.type_token = Type(TypeEnum.TOKEN)
		self.type_quickplay = Type(TypeEnum.QUICKPLAY)
		self.type_continuous = Type(TypeEnum.CONTINUOUS)
		self.type_equip = Type(TypeEnum.EQUIP)
		self.type_field = Type(TypeEnum.FIELD)
		self.type_counter = Type(TypeEnum.COUNTER)
		self.type_flip = Type(TypeEnum.FLIP)
		self.type_toon = Type(TypeEnum.TOON)
		self.type_xyz = Type(TypeEnum.XYZ)
		self.type_pendulum = Type(TypeEnum.PENDULUM)
		self.type_spsummon = Type(TypeEnum.SPSUMMON)
		self.type_link = Type(TypeEnum.LINK)


	def test_isa_when_type_none_with_MONSTER(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.MONSTER))


	def test_isa_when_type_none_with_SPELL(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.SPELL))


	def test_isa_when_type_none_with_TRAP(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.TRAP))


	def test_isa_when_type_none_with_NORMAL(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.NORMAL))


	def test_isa_when_type_none_with_EFFECT(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.EFFECT))


	def test_isa_when_type_none_with_FUSION(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.FUSION))


	def test_isa_when_type_none_with_RITUAL(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.RITUAL))


	def test_isa_when_type_none_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_none_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_none_with_UNION(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.UNION))


	def test_isa_when_type_none_with_GEMINI(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.GEMINI))


	def test_isa_when_type_none_with_TUNER(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.TUNER))


	def test_isa_when_type_none_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_none_with_TOKEN(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.TOKEN))


	def test_isa_when_type_none_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_none_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_none_with_EQUIP(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.EQUIP))


	def test_isa_when_type_none_with_FIELD(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.FIELD))


	def test_isa_when_type_none_with_COUNTER(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.COUNTER))


	def test_isa_when_type_none_with_FLIP(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.FLIP))


	def test_isa_when_type_none_with_TOON(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.TOON))


	def test_isa_when_type_none_with_XYZ(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.XYZ))


	def test_isa_when_type_none_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_none_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_none_with_LINK(self) -> None:
		self.assertFalse(self.type_none.isa(TypeEnum.LINK))


	def test_isa_when_type_monster_with_MONSTER(self) -> None:
		self.assertTrue(self.type_monster.isa(TypeEnum.MONSTER))


	def test_isa_when_type_monster_with_SPELL(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.SPELL))


	def test_isa_when_type_monster_with_TRAP(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.TRAP))


	def test_isa_when_type_monster_with_NORMAL(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.NORMAL))


	def test_isa_when_type_monster_with_EFFECT(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.EFFECT))


	def test_isa_when_type_monster_with_FUSION(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.FUSION))


	def test_isa_when_type_monster_with_RITUAL(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.RITUAL))


	def test_isa_when_type_monster_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_monster_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_monster_with_UNION(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.UNION))


	def test_isa_when_type_monster_with_GEMINI(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.GEMINI))


	def test_isa_when_type_monster_with_TUNER(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.TUNER))


	def test_isa_when_type_monster_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_monster_with_TOKEN(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.TOKEN))


	def test_isa_when_type_monster_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_monster_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_monster_with_EQUIP(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.EQUIP))


	def test_isa_when_type_monster_with_FIELD(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.FIELD))


	def test_isa_when_type_monster_with_COUNTER(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.COUNTER))


	def test_isa_when_type_monster_with_FLIP(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.FLIP))


	def test_isa_when_type_monster_with_TOON(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.TOON))


	def test_isa_when_type_monster_with_XYZ(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.XYZ))


	def test_isa_when_type_monster_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_monster_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_monster_with_LINK(self) -> None:
		self.assertFalse(self.type_monster.isa(TypeEnum.LINK))


	def test_isa_when_type_spell_with_MONSTER(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.MONSTER))


	def test_isa_when_type_spell_with_SPELL(self) -> None:
		self.assertTrue(self.type_spell.isa(TypeEnum.SPELL))


	def test_isa_when_type_spell_with_TRAP(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.TRAP))


	def test_isa_when_type_spell_with_NORMAL(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.NORMAL))


	def test_isa_when_type_spell_with_EFFECT(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.EFFECT))


	def test_isa_when_type_spell_with_FUSION(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.FUSION))


	def test_isa_when_type_spell_with_RITUAL(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.RITUAL))


	def test_isa_when_type_spell_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_spell_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_spell_with_UNION(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.UNION))


	def test_isa_when_type_spell_with_GEMINI(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.GEMINI))


	def test_isa_when_type_spell_with_TUNER(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.TUNER))


	def test_isa_when_type_spell_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_spell_with_TOKEN(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.TOKEN))


	def test_isa_when_type_spell_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_spell_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_spell_with_EQUIP(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.EQUIP))


	def test_isa_when_type_spell_with_FIELD(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.FIELD))


	def test_isa_when_type_spell_with_COUNTER(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.COUNTER))


	def test_isa_when_type_spell_with_FLIP(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.FLIP))


	def test_isa_when_type_spell_with_TOON(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.TOON))


	def test_isa_when_type_spell_with_XYZ(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.XYZ))


	def test_isa_when_type_spell_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_spell_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_spell_with_LINK(self) -> None:
		self.assertFalse(self.type_spell.isa(TypeEnum.LINK))


	def test_isa_when_type_trap_with_MONSTER(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.MONSTER))


	def test_isa_when_type_trap_with_SPELL(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.SPELL))


	def test_isa_when_type_trap_with_TRAP(self) -> None:
		self.assertTrue(self.type_trap.isa(TypeEnum.TRAP))


	def test_isa_when_type_trap_with_NORMAL(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.NORMAL))


	def test_isa_when_type_trap_with_EFFECT(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.EFFECT))


	def test_isa_when_type_trap_with_FUSION(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.FUSION))


	def test_isa_when_type_trap_with_RITUAL(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.RITUAL))


	def test_isa_when_type_trap_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_trap_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_trap_with_UNION(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.UNION))


	def test_isa_when_type_trap_with_GEMINI(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.GEMINI))


	def test_isa_when_type_trap_with_TUNER(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.TUNER))


	def test_isa_when_type_trap_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_trap_with_TOKEN(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.TOKEN))


	def test_isa_when_type_trap_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_trap_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_trap_with_EQUIP(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.EQUIP))


	def test_isa_when_type_trap_with_FIELD(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.FIELD))


	def test_isa_when_type_trap_with_COUNTER(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.COUNTER))


	def test_isa_when_type_trap_with_FLIP(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.FLIP))


	def test_isa_when_type_trap_with_TOON(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.TOON))


	def test_isa_when_type_trap_with_XYZ(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.XYZ))


	def test_isa_when_type_trap_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_trap_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_trap_with_LINK(self) -> None:
		self.assertFalse(self.type_trap.isa(TypeEnum.LINK))


	def test_isa_when_type_normal_with_MONSTER(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.MONSTER))


	def test_isa_when_type_normal_with_SPELL(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.SPELL))


	def test_isa_when_type_normal_with_TRAP(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.TRAP))


	def test_isa_when_type_normal_with_NORMAL(self) -> None:
		self.assertTrue(self.type_normal.isa(TypeEnum.NORMAL))


	def test_isa_when_type_normal_with_EFFECT(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.EFFECT))


	def test_isa_when_type_normal_with_FUSION(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.FUSION))


	def test_isa_when_type_normal_with_RITUAL(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.RITUAL))


	def test_isa_when_type_normal_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_normal_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_normal_with_UNION(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.UNION))


	def test_isa_when_type_normal_with_GEMINI(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.GEMINI))


	def test_isa_when_type_normal_with_TUNER(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.TUNER))


	def test_isa_when_type_normal_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_normal_with_TOKEN(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.TOKEN))


	def test_isa_when_type_normal_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_normal_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_normal_with_EQUIP(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.EQUIP))


	def test_isa_when_type_normal_with_FIELD(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.FIELD))


	def test_isa_when_type_normal_with_COUNTER(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.COUNTER))


	def test_isa_when_type_normal_with_FLIP(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.FLIP))


	def test_isa_when_type_normal_with_TOON(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.TOON))


	def test_isa_when_type_normal_with_XYZ(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.XYZ))


	def test_isa_when_type_normal_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_normal_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_normal_with_LINK(self) -> None:
		self.assertFalse(self.type_normal.isa(TypeEnum.LINK))


	def test_isa_when_type_effect_with_MONSTER(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.MONSTER))


	def test_isa_when_type_effect_with_SPELL(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.SPELL))


	def test_isa_when_type_effect_with_TRAP(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.TRAP))


	def test_isa_when_type_effect_with_NORMAL(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.NORMAL))


	def test_isa_when_type_effect_with_EFFECT(self) -> None:
		self.assertTrue(self.type_effect.isa(TypeEnum.EFFECT))


	def test_isa_when_type_effect_with_FUSION(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.FUSION))


	def test_isa_when_type_effect_with_RITUAL(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.RITUAL))


	def test_isa_when_type_effect_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_effect_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_effect_with_UNION(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.UNION))


	def test_isa_when_type_effect_with_GEMINI(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.GEMINI))


	def test_isa_when_type_effect_with_TUNER(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.TUNER))


	def test_isa_when_type_effect_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_effect_with_TOKEN(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.TOKEN))


	def test_isa_when_type_effect_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_effect_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_effect_with_EQUIP(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.EQUIP))


	def test_isa_when_type_effect_with_FIELD(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.FIELD))


	def test_isa_when_type_effect_with_COUNTER(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.COUNTER))


	def test_isa_when_type_effect_with_FLIP(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.FLIP))


	def test_isa_when_type_effect_with_TOON(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.TOON))


	def test_isa_when_type_effect_with_XYZ(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.XYZ))


	def test_isa_when_type_effect_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_effect_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_effect_with_LINK(self) -> None:
		self.assertFalse(self.type_effect.isa(TypeEnum.LINK))


	def test_isa_when_type_fusion_with_MONSTER(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.MONSTER))


	def test_isa_when_type_fusion_with_SPELL(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.SPELL))


	def test_isa_when_type_fusion_with_TRAP(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.TRAP))


	def test_isa_when_type_fusion_with_NORMAL(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.NORMAL))


	def test_isa_when_type_fusion_with_EFFECT(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.EFFECT))


	def test_isa_when_type_fusion_with_FUSION(self) -> None:
		self.assertTrue(self.type_fusion.isa(TypeEnum.FUSION))


	def test_isa_when_type_fusion_with_RITUAL(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.RITUAL))


	def test_isa_when_type_fusion_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_fusion_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_fusion_with_UNION(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.UNION))


	def test_isa_when_type_fusion_with_GEMINI(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.GEMINI))


	def test_isa_when_type_fusion_with_TUNER(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.TUNER))


	def test_isa_when_type_fusion_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_fusion_with_TOKEN(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.TOKEN))


	def test_isa_when_type_fusion_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_fusion_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_fusion_with_EQUIP(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.EQUIP))


	def test_isa_when_type_fusion_with_FIELD(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.FIELD))


	def test_isa_when_type_fusion_with_COUNTER(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.COUNTER))


	def test_isa_when_type_fusion_with_FLIP(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.FLIP))


	def test_isa_when_type_fusion_with_TOON(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.TOON))


	def test_isa_when_type_fusion_with_XYZ(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.XYZ))


	def test_isa_when_type_fusion_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_fusion_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_fusion_with_LINK(self) -> None:
		self.assertFalse(self.type_fusion.isa(TypeEnum.LINK))


	def test_isa_when_type_ritual_with_MONSTER(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.MONSTER))


	def test_isa_when_type_ritual_with_SPELL(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.SPELL))


	def test_isa_when_type_ritual_with_TRAP(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.TRAP))


	def test_isa_when_type_ritual_with_NORMAL(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.NORMAL))


	def test_isa_when_type_ritual_with_EFFECT(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.EFFECT))


	def test_isa_when_type_ritual_with_FUSION(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.FUSION))


	def test_isa_when_type_ritual_with_RITUAL(self) -> None:
		self.assertTrue(self.type_ritual.isa(TypeEnum.RITUAL))


	def test_isa_when_type_ritual_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_ritual_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_ritual_with_UNION(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.UNION))


	def test_isa_when_type_ritual_with_GEMINI(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.GEMINI))


	def test_isa_when_type_ritual_with_TUNER(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.TUNER))


	def test_isa_when_type_ritual_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_ritual_with_TOKEN(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.TOKEN))


	def test_isa_when_type_ritual_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_ritual_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_ritual_with_EQUIP(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.EQUIP))


	def test_isa_when_type_ritual_with_FIELD(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.FIELD))


	def test_isa_when_type_ritual_with_COUNTER(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.COUNTER))


	def test_isa_when_type_ritual_with_FLIP(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.FLIP))


	def test_isa_when_type_ritual_with_TOON(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.TOON))


	def test_isa_when_type_ritual_with_XYZ(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.XYZ))


	def test_isa_when_type_ritual_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_ritual_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_ritual_with_LINK(self) -> None:
		self.assertFalse(self.type_ritual.isa(TypeEnum.LINK))


	def test_isa_when_type_trapmonster_with_MONSTER(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.MONSTER))


	def test_isa_when_type_trapmonster_with_SPELL(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.SPELL))


	def test_isa_when_type_trapmonster_with_TRAP(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.TRAP))


	def test_isa_when_type_trapmonster_with_NORMAL(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.NORMAL))


	def test_isa_when_type_trapmonster_with_EFFECT(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.EFFECT))


	def test_isa_when_type_trapmonster_with_FUSION(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.FUSION))


	def test_isa_when_type_trapmonster_with_RITUAL(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.RITUAL))


	def test_isa_when_type_trapmonster_with_TRAPMONSTER(self) -> None:
		self.assertTrue(self.type_trapmonster.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_trapmonster_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_trapmonster_with_UNION(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.UNION))


	def test_isa_when_type_trapmonster_with_GEMINI(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.GEMINI))


	def test_isa_when_type_trapmonster_with_TUNER(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.TUNER))


	def test_isa_when_type_trapmonster_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_trapmonster_with_TOKEN(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.TOKEN))


	def test_isa_when_type_trapmonster_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_trapmonster_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_trapmonster_with_EQUIP(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.EQUIP))


	def test_isa_when_type_trapmonster_with_FIELD(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.FIELD))


	def test_isa_when_type_trapmonster_with_COUNTER(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.COUNTER))


	def test_isa_when_type_trapmonster_with_FLIP(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.FLIP))


	def test_isa_when_type_trapmonster_with_TOON(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.TOON))


	def test_isa_when_type_trapmonster_with_XYZ(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.XYZ))


	def test_isa_when_type_trapmonster_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_trapmonster_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_trapmonster_with_LINK(self) -> None:
		self.assertFalse(self.type_trapmonster.isa(TypeEnum.LINK))


	def test_isa_when_type_spirit_with_MONSTER(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.MONSTER))


	def test_isa_when_type_spirit_with_SPELL(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.SPELL))


	def test_isa_when_type_spirit_with_TRAP(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.TRAP))


	def test_isa_when_type_spirit_with_NORMAL(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.NORMAL))


	def test_isa_when_type_spirit_with_EFFECT(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.EFFECT))


	def test_isa_when_type_spirit_with_FUSION(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.FUSION))


	def test_isa_when_type_spirit_with_RITUAL(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.RITUAL))


	def test_isa_when_type_spirit_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_spirit_with_SPIRIT(self) -> None:
		self.assertTrue(self.type_spirit.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_spirit_with_UNION(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.UNION))


	def test_isa_when_type_spirit_with_GEMINI(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.GEMINI))


	def test_isa_when_type_spirit_with_TUNER(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.TUNER))


	def test_isa_when_type_spirit_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_spirit_with_TOKEN(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.TOKEN))


	def test_isa_when_type_spirit_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_spirit_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_spirit_with_EQUIP(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.EQUIP))


	def test_isa_when_type_spirit_with_FIELD(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.FIELD))


	def test_isa_when_type_spirit_with_COUNTER(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.COUNTER))


	def test_isa_when_type_spirit_with_FLIP(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.FLIP))


	def test_isa_when_type_spirit_with_TOON(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.TOON))


	def test_isa_when_type_spirit_with_XYZ(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.XYZ))


	def test_isa_when_type_spirit_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_spirit_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_spirit_with_LINK(self) -> None:
		self.assertFalse(self.type_spirit.isa(TypeEnum.LINK))


	def test_isa_when_type_union_with_MONSTER(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.MONSTER))


	def test_isa_when_type_union_with_SPELL(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.SPELL))


	def test_isa_when_type_union_with_TRAP(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.TRAP))


	def test_isa_when_type_union_with_NORMAL(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.NORMAL))


	def test_isa_when_type_union_with_EFFECT(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.EFFECT))


	def test_isa_when_type_union_with_FUSION(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.FUSION))


	def test_isa_when_type_union_with_RITUAL(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.RITUAL))


	def test_isa_when_type_union_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_union_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_union_with_UNION(self) -> None:
		self.assertTrue(self.type_union.isa(TypeEnum.UNION))


	def test_isa_when_type_union_with_GEMINI(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.GEMINI))


	def test_isa_when_type_union_with_TUNER(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.TUNER))


	def test_isa_when_type_union_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_union_with_TOKEN(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.TOKEN))


	def test_isa_when_type_union_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_union_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_union_with_EQUIP(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.EQUIP))


	def test_isa_when_type_union_with_FIELD(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.FIELD))


	def test_isa_when_type_union_with_COUNTER(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.COUNTER))


	def test_isa_when_type_union_with_FLIP(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.FLIP))


	def test_isa_when_type_union_with_TOON(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.TOON))


	def test_isa_when_type_union_with_XYZ(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.XYZ))


	def test_isa_when_type_union_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_union_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_union_with_LINK(self) -> None:
		self.assertFalse(self.type_union.isa(TypeEnum.LINK))


	def test_isa_when_type_gemini_with_MONSTER(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.MONSTER))


	def test_isa_when_type_gemini_with_SPELL(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.SPELL))


	def test_isa_when_type_gemini_with_TRAP(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.TRAP))


	def test_isa_when_type_gemini_with_NORMAL(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.NORMAL))


	def test_isa_when_type_gemini_with_EFFECT(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.EFFECT))


	def test_isa_when_type_gemini_with_FUSION(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.FUSION))


	def test_isa_when_type_gemini_with_RITUAL(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.RITUAL))


	def test_isa_when_type_gemini_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_gemini_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_gemini_with_UNION(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.UNION))


	def test_isa_when_type_gemini_with_GEMINI(self) -> None:
		self.assertTrue(self.type_gemini.isa(TypeEnum.GEMINI))


	def test_isa_when_type_gemini_with_TUNER(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.TUNER))


	def test_isa_when_type_gemini_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_gemini_with_TOKEN(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.TOKEN))


	def test_isa_when_type_gemini_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_gemini_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_gemini_with_EQUIP(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.EQUIP))


	def test_isa_when_type_gemini_with_FIELD(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.FIELD))


	def test_isa_when_type_gemini_with_COUNTER(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.COUNTER))


	def test_isa_when_type_gemini_with_FLIP(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.FLIP))


	def test_isa_when_type_gemini_with_TOON(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.TOON))


	def test_isa_when_type_gemini_with_XYZ(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.XYZ))


	def test_isa_when_type_gemini_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_gemini_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_gemini_with_LINK(self) -> None:
		self.assertFalse(self.type_gemini.isa(TypeEnum.LINK))


	def test_isa_when_type_tuner_with_MONSTER(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.MONSTER))


	def test_isa_when_type_tuner_with_SPELL(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.SPELL))


	def test_isa_when_type_tuner_with_TRAP(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.TRAP))


	def test_isa_when_type_tuner_with_NORMAL(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.NORMAL))


	def test_isa_when_type_tuner_with_EFFECT(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.EFFECT))


	def test_isa_when_type_tuner_with_FUSION(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.FUSION))


	def test_isa_when_type_tuner_with_RITUAL(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.RITUAL))


	def test_isa_when_type_tuner_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_tuner_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_tuner_with_UNION(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.UNION))


	def test_isa_when_type_tuner_with_GEMINI(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.GEMINI))


	def test_isa_when_type_tuner_with_TUNER(self) -> None:
		self.assertTrue(self.type_tuner.isa(TypeEnum.TUNER))


	def test_isa_when_type_tuner_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_tuner_with_TOKEN(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.TOKEN))


	def test_isa_when_type_tuner_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_tuner_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_tuner_with_EQUIP(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.EQUIP))


	def test_isa_when_type_tuner_with_FIELD(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.FIELD))


	def test_isa_when_type_tuner_with_COUNTER(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.COUNTER))


	def test_isa_when_type_tuner_with_FLIP(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.FLIP))


	def test_isa_when_type_tuner_with_TOON(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.TOON))


	def test_isa_when_type_tuner_with_XYZ(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.XYZ))


	def test_isa_when_type_tuner_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_tuner_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_tuner_with_LINK(self) -> None:
		self.assertFalse(self.type_tuner.isa(TypeEnum.LINK))


	def test_isa_when_type_synchro_with_MONSTER(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.MONSTER))


	def test_isa_when_type_synchro_with_SPELL(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.SPELL))


	def test_isa_when_type_synchro_with_TRAP(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.TRAP))


	def test_isa_when_type_synchro_with_NORMAL(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.NORMAL))


	def test_isa_when_type_synchro_with_EFFECT(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.EFFECT))


	def test_isa_when_type_synchro_with_FUSION(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.FUSION))


	def test_isa_when_type_synchro_with_RITUAL(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.RITUAL))


	def test_isa_when_type_synchro_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_synchro_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_synchro_with_UNION(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.UNION))


	def test_isa_when_type_synchro_with_GEMINI(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.GEMINI))


	def test_isa_when_type_synchro_with_TUNER(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.TUNER))


	def test_isa_when_type_synchro_with_SYNCHRO(self) -> None:
		self.assertTrue(self.type_synchro.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_synchro_with_TOKEN(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.TOKEN))


	def test_isa_when_type_synchro_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_synchro_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_synchro_with_EQUIP(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.EQUIP))


	def test_isa_when_type_synchro_with_FIELD(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.FIELD))


	def test_isa_when_type_synchro_with_COUNTER(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.COUNTER))


	def test_isa_when_type_synchro_with_FLIP(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.FLIP))


	def test_isa_when_type_synchro_with_TOON(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.TOON))


	def test_isa_when_type_synchro_with_XYZ(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.XYZ))


	def test_isa_when_type_synchro_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_synchro_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_synchro_with_LINK(self) -> None:
		self.assertFalse(self.type_synchro.isa(TypeEnum.LINK))


	def test_isa_when_type_token_with_MONSTER(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.MONSTER))


	def test_isa_when_type_token_with_SPELL(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.SPELL))


	def test_isa_when_type_token_with_TRAP(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.TRAP))


	def test_isa_when_type_token_with_NORMAL(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.NORMAL))


	def test_isa_when_type_token_with_EFFECT(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.EFFECT))


	def test_isa_when_type_token_with_FUSION(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.FUSION))


	def test_isa_when_type_token_with_RITUAL(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.RITUAL))


	def test_isa_when_type_token_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_token_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_token_with_UNION(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.UNION))


	def test_isa_when_type_token_with_GEMINI(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.GEMINI))


	def test_isa_when_type_token_with_TUNER(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.TUNER))


	def test_isa_when_type_token_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_token_with_TOKEN(self) -> None:
		self.assertTrue(self.type_token.isa(TypeEnum.TOKEN))


	def test_isa_when_type_token_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_token_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_token_with_EQUIP(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.EQUIP))


	def test_isa_when_type_token_with_FIELD(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.FIELD))


	def test_isa_when_type_token_with_COUNTER(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.COUNTER))


	def test_isa_when_type_token_with_FLIP(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.FLIP))


	def test_isa_when_type_token_with_TOON(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.TOON))


	def test_isa_when_type_token_with_XYZ(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.XYZ))


	def test_isa_when_type_token_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_token_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_token_with_LINK(self) -> None:
		self.assertFalse(self.type_token.isa(TypeEnum.LINK))


	def test_isa_when_type_quickplay_with_MONSTER(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.MONSTER))


	def test_isa_when_type_quickplay_with_SPELL(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.SPELL))


	def test_isa_when_type_quickplay_with_TRAP(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.TRAP))


	def test_isa_when_type_quickplay_with_NORMAL(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.NORMAL))


	def test_isa_when_type_quickplay_with_EFFECT(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.EFFECT))


	def test_isa_when_type_quickplay_with_FUSION(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.FUSION))


	def test_isa_when_type_quickplay_with_RITUAL(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.RITUAL))


	def test_isa_when_type_quickplay_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_quickplay_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_quickplay_with_UNION(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.UNION))


	def test_isa_when_type_quickplay_with_GEMINI(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.GEMINI))


	def test_isa_when_type_quickplay_with_TUNER(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.TUNER))


	def test_isa_when_type_quickplay_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_quickplay_with_TOKEN(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.TOKEN))


	def test_isa_when_type_quickplay_with_QUICKPLAY(self) -> None:
		self.assertTrue(self.type_quickplay.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_quickplay_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_quickplay_with_EQUIP(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.EQUIP))


	def test_isa_when_type_quickplay_with_FIELD(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.FIELD))


	def test_isa_when_type_quickplay_with_COUNTER(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.COUNTER))


	def test_isa_when_type_quickplay_with_FLIP(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.FLIP))


	def test_isa_when_type_quickplay_with_TOON(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.TOON))


	def test_isa_when_type_quickplay_with_XYZ(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.XYZ))


	def test_isa_when_type_quickplay_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_quickplay_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_quickplay_with_LINK(self) -> None:
		self.assertFalse(self.type_quickplay.isa(TypeEnum.LINK))


	def test_isa_when_type_continuous_with_MONSTER(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.MONSTER))


	def test_isa_when_type_continuous_with_SPELL(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.SPELL))


	def test_isa_when_type_continuous_with_TRAP(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.TRAP))


	def test_isa_when_type_continuous_with_NORMAL(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.NORMAL))


	def test_isa_when_type_continuous_with_EFFECT(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.EFFECT))


	def test_isa_when_type_continuous_with_FUSION(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.FUSION))


	def test_isa_when_type_continuous_with_RITUAL(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.RITUAL))


	def test_isa_when_type_continuous_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_continuous_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_continuous_with_UNION(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.UNION))


	def test_isa_when_type_continuous_with_GEMINI(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.GEMINI))


	def test_isa_when_type_continuous_with_TUNER(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.TUNER))


	def test_isa_when_type_continuous_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_continuous_with_TOKEN(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.TOKEN))


	def test_isa_when_type_continuous_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_continuous_with_CONTINUOUS(self) -> None:
		self.assertTrue(self.type_continuous.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_continuous_with_EQUIP(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.EQUIP))


	def test_isa_when_type_continuous_with_FIELD(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.FIELD))


	def test_isa_when_type_continuous_with_COUNTER(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.COUNTER))


	def test_isa_when_type_continuous_with_FLIP(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.FLIP))


	def test_isa_when_type_continuous_with_TOON(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.TOON))


	def test_isa_when_type_continuous_with_XYZ(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.XYZ))


	def test_isa_when_type_continuous_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_continuous_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_continuous_with_LINK(self) -> None:
		self.assertFalse(self.type_continuous.isa(TypeEnum.LINK))


	def test_isa_when_type_equip_with_MONSTER(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.MONSTER))


	def test_isa_when_type_equip_with_SPELL(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.SPELL))


	def test_isa_when_type_equip_with_TRAP(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.TRAP))


	def test_isa_when_type_equip_with_NORMAL(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.NORMAL))


	def test_isa_when_type_equip_with_EFFECT(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.EFFECT))


	def test_isa_when_type_equip_with_FUSION(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.FUSION))


	def test_isa_when_type_equip_with_RITUAL(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.RITUAL))


	def test_isa_when_type_equip_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_equip_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_equip_with_UNION(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.UNION))


	def test_isa_when_type_equip_with_GEMINI(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.GEMINI))


	def test_isa_when_type_equip_with_TUNER(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.TUNER))


	def test_isa_when_type_equip_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_equip_with_TOKEN(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.TOKEN))


	def test_isa_when_type_equip_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_equip_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_equip_with_EQUIP(self) -> None:
		self.assertTrue(self.type_equip.isa(TypeEnum.EQUIP))


	def test_isa_when_type_equip_with_FIELD(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.FIELD))


	def test_isa_when_type_equip_with_COUNTER(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.COUNTER))


	def test_isa_when_type_equip_with_FLIP(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.FLIP))


	def test_isa_when_type_equip_with_TOON(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.TOON))


	def test_isa_when_type_equip_with_XYZ(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.XYZ))


	def test_isa_when_type_equip_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_equip_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_equip_with_LINK(self) -> None:
		self.assertFalse(self.type_equip.isa(TypeEnum.LINK))


	def test_isa_when_type_field_with_MONSTER(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.MONSTER))


	def test_isa_when_type_field_with_SPELL(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.SPELL))


	def test_isa_when_type_field_with_TRAP(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.TRAP))


	def test_isa_when_type_field_with_NORMAL(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.NORMAL))


	def test_isa_when_type_field_with_EFFECT(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.EFFECT))


	def test_isa_when_type_field_with_FUSION(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.FUSION))


	def test_isa_when_type_field_with_RITUAL(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.RITUAL))


	def test_isa_when_type_field_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_field_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_field_with_UNION(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.UNION))


	def test_isa_when_type_field_with_GEMINI(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.GEMINI))


	def test_isa_when_type_field_with_TUNER(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.TUNER))


	def test_isa_when_type_field_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_field_with_TOKEN(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.TOKEN))


	def test_isa_when_type_field_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_field_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_field_with_EQUIP(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.EQUIP))


	def test_isa_when_type_field_with_FIELD(self) -> None:
		self.assertTrue(self.type_field.isa(TypeEnum.FIELD))


	def test_isa_when_type_field_with_COUNTER(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.COUNTER))


	def test_isa_when_type_field_with_FLIP(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.FLIP))


	def test_isa_when_type_field_with_TOON(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.TOON))


	def test_isa_when_type_field_with_XYZ(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.XYZ))


	def test_isa_when_type_field_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_field_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_field_with_LINK(self) -> None:
		self.assertFalse(self.type_field.isa(TypeEnum.LINK))


	def test_isa_when_type_counter_with_MONSTER(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.MONSTER))


	def test_isa_when_type_counter_with_SPELL(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.SPELL))


	def test_isa_when_type_counter_with_TRAP(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.TRAP))


	def test_isa_when_type_counter_with_NORMAL(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.NORMAL))


	def test_isa_when_type_counter_with_EFFECT(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.EFFECT))


	def test_isa_when_type_counter_with_FUSION(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.FUSION))


	def test_isa_when_type_counter_with_RITUAL(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.RITUAL))


	def test_isa_when_type_counter_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_counter_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_counter_with_UNION(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.UNION))


	def test_isa_when_type_counter_with_GEMINI(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.GEMINI))


	def test_isa_when_type_counter_with_TUNER(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.TUNER))


	def test_isa_when_type_counter_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_counter_with_TOKEN(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.TOKEN))


	def test_isa_when_type_counter_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_counter_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_counter_with_EQUIP(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.EQUIP))


	def test_isa_when_type_counter_with_FIELD(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.FIELD))


	def test_isa_when_type_counter_with_COUNTER(self) -> None:
		self.assertTrue(self.type_counter.isa(TypeEnum.COUNTER))


	def test_isa_when_type_counter_with_FLIP(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.FLIP))


	def test_isa_when_type_counter_with_TOON(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.TOON))


	def test_isa_when_type_counter_with_XYZ(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.XYZ))


	def test_isa_when_type_counter_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_counter_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_counter_with_LINK(self) -> None:
		self.assertFalse(self.type_counter.isa(TypeEnum.LINK))


	def test_isa_when_type_flip_with_MONSTER(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.MONSTER))


	def test_isa_when_type_flip_with_SPELL(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.SPELL))


	def test_isa_when_type_flip_with_TRAP(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.TRAP))


	def test_isa_when_type_flip_with_NORMAL(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.NORMAL))


	def test_isa_when_type_flip_with_EFFECT(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.EFFECT))


	def test_isa_when_type_flip_with_FUSION(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.FUSION))


	def test_isa_when_type_flip_with_RITUAL(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.RITUAL))


	def test_isa_when_type_flip_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_flip_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_flip_with_UNION(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.UNION))


	def test_isa_when_type_flip_with_GEMINI(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.GEMINI))


	def test_isa_when_type_flip_with_TUNER(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.TUNER))


	def test_isa_when_type_flip_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_flip_with_TOKEN(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.TOKEN))


	def test_isa_when_type_flip_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_flip_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_flip_with_EQUIP(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.EQUIP))


	def test_isa_when_type_flip_with_FIELD(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.FIELD))


	def test_isa_when_type_flip_with_COUNTER(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.COUNTER))


	def test_isa_when_type_flip_with_FLIP(self) -> None:
		self.assertTrue(self.type_flip.isa(TypeEnum.FLIP))


	def test_isa_when_type_flip_with_TOON(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.TOON))


	def test_isa_when_type_flip_with_XYZ(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.XYZ))


	def test_isa_when_type_flip_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_flip_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_flip_with_LINK(self) -> None:
		self.assertFalse(self.type_flip.isa(TypeEnum.LINK))


	def test_isa_when_type_toon_with_MONSTER(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.MONSTER))


	def test_isa_when_type_toon_with_SPELL(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.SPELL))


	def test_isa_when_type_toon_with_TRAP(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.TRAP))


	def test_isa_when_type_toon_with_NORMAL(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.NORMAL))


	def test_isa_when_type_toon_with_EFFECT(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.EFFECT))


	def test_isa_when_type_toon_with_FUSION(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.FUSION))


	def test_isa_when_type_toon_with_RITUAL(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.RITUAL))


	def test_isa_when_type_toon_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_toon_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_toon_with_UNION(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.UNION))


	def test_isa_when_type_toon_with_GEMINI(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.GEMINI))


	def test_isa_when_type_toon_with_TUNER(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.TUNER))


	def test_isa_when_type_toon_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_toon_with_TOKEN(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.TOKEN))


	def test_isa_when_type_toon_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_toon_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_toon_with_EQUIP(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.EQUIP))


	def test_isa_when_type_toon_with_FIELD(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.FIELD))


	def test_isa_when_type_toon_with_COUNTER(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.COUNTER))


	def test_isa_when_type_toon_with_FLIP(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.FLIP))


	def test_isa_when_type_toon_with_TOON(self) -> None:
		self.assertTrue(self.type_toon.isa(TypeEnum.TOON))


	def test_isa_when_type_toon_with_XYZ(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.XYZ))


	def test_isa_when_type_toon_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_toon_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_toon_with_LINK(self) -> None:
		self.assertFalse(self.type_toon.isa(TypeEnum.LINK))


	def test_isa_when_type_xyz_with_MONSTER(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.MONSTER))


	def test_isa_when_type_xyz_with_SPELL(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.SPELL))


	def test_isa_when_type_xyz_with_TRAP(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.TRAP))


	def test_isa_when_type_xyz_with_NORMAL(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.NORMAL))


	def test_isa_when_type_xyz_with_EFFECT(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.EFFECT))


	def test_isa_when_type_xyz_with_FUSION(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.FUSION))


	def test_isa_when_type_xyz_with_RITUAL(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.RITUAL))


	def test_isa_when_type_xyz_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_xyz_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_xyz_with_UNION(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.UNION))


	def test_isa_when_type_xyz_with_GEMINI(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.GEMINI))


	def test_isa_when_type_xyz_with_TUNER(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.TUNER))


	def test_isa_when_type_xyz_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_xyz_with_TOKEN(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.TOKEN))


	def test_isa_when_type_xyz_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_xyz_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_xyz_with_EQUIP(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.EQUIP))


	def test_isa_when_type_xyz_with_FIELD(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.FIELD))


	def test_isa_when_type_xyz_with_COUNTER(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.COUNTER))


	def test_isa_when_type_xyz_with_FLIP(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.FLIP))


	def test_isa_when_type_xyz_with_TOON(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.TOON))


	def test_isa_when_type_xyz_with_XYZ(self) -> None:
		self.assertTrue(self.type_xyz.isa(TypeEnum.XYZ))


	def test_isa_when_type_xyz_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_xyz_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_xyz_with_LINK(self) -> None:
		self.assertFalse(self.type_xyz.isa(TypeEnum.LINK))


	def test_isa_when_type_pendulum_with_MONSTER(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.MONSTER))


	def test_isa_when_type_pendulum_with_SPELL(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.SPELL))


	def test_isa_when_type_pendulum_with_TRAP(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.TRAP))


	def test_isa_when_type_pendulum_with_NORMAL(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.NORMAL))


	def test_isa_when_type_pendulum_with_EFFECT(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.EFFECT))


	def test_isa_when_type_pendulum_with_FUSION(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.FUSION))


	def test_isa_when_type_pendulum_with_RITUAL(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.RITUAL))


	def test_isa_when_type_pendulum_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_pendulum_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_pendulum_with_UNION(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.UNION))


	def test_isa_when_type_pendulum_with_GEMINI(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.GEMINI))


	def test_isa_when_type_pendulum_with_TUNER(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.TUNER))


	def test_isa_when_type_pendulum_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_pendulum_with_TOKEN(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.TOKEN))


	def test_isa_when_type_pendulum_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_pendulum_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_pendulum_with_EQUIP(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.EQUIP))


	def test_isa_when_type_pendulum_with_FIELD(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.FIELD))


	def test_isa_when_type_pendulum_with_COUNTER(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.COUNTER))


	def test_isa_when_type_pendulum_with_FLIP(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.FLIP))


	def test_isa_when_type_pendulum_with_TOON(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.TOON))


	def test_isa_when_type_pendulum_with_XYZ(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.XYZ))


	def test_isa_when_type_pendulum_with_PENDULUM(self) -> None:
		self.assertTrue(self.type_pendulum.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_pendulum_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_pendulum_with_LINK(self) -> None:
		self.assertFalse(self.type_pendulum.isa(TypeEnum.LINK))


	def test_isa_when_type_spsummon_with_MONSTER(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.MONSTER))


	def test_isa_when_type_spsummon_with_SPELL(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.SPELL))


	def test_isa_when_type_spsummon_with_TRAP(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.TRAP))


	def test_isa_when_type_spsummon_with_NORMAL(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.NORMAL))


	def test_isa_when_type_spsummon_with_EFFECT(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.EFFECT))


	def test_isa_when_type_spsummon_with_FUSION(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.FUSION))


	def test_isa_when_type_spsummon_with_RITUAL(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.RITUAL))


	def test_isa_when_type_spsummon_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_spsummon_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_spsummon_with_UNION(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.UNION))


	def test_isa_when_type_spsummon_with_GEMINI(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.GEMINI))


	def test_isa_when_type_spsummon_with_TUNER(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.TUNER))


	def test_isa_when_type_spsummon_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_spsummon_with_TOKEN(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.TOKEN))


	def test_isa_when_type_spsummon_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_spsummon_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_spsummon_with_EQUIP(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.EQUIP))


	def test_isa_when_type_spsummon_with_FIELD(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.FIELD))


	def test_isa_when_type_spsummon_with_COUNTER(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.COUNTER))


	def test_isa_when_type_spsummon_with_FLIP(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.FLIP))


	def test_isa_when_type_spsummon_with_TOON(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.TOON))


	def test_isa_when_type_spsummon_with_XYZ(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.XYZ))


	def test_isa_when_type_spsummon_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_spsummon_with_SPSUMMON(self) -> None:
		self.assertTrue(self.type_spsummon.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_spsummon_with_LINK(self) -> None:
		self.assertFalse(self.type_spsummon.isa(TypeEnum.LINK))


	def test_isa_when_type_link_with_MONSTER(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.MONSTER))


	def test_isa_when_type_link_with_SPELL(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.SPELL))


	def test_isa_when_type_link_with_TRAP(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.TRAP))


	def test_isa_when_type_link_with_NORMAL(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.NORMAL))


	def test_isa_when_type_link_with_EFFECT(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.EFFECT))


	def test_isa_when_type_link_with_FUSION(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.FUSION))


	def test_isa_when_type_link_with_RITUAL(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.RITUAL))


	def test_isa_when_type_link_with_TRAPMONSTER(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.TRAPMONSTER))


	def test_isa_when_type_link_with_SPIRIT(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.SPIRIT))


	def test_isa_when_type_link_with_UNION(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.UNION))


	def test_isa_when_type_link_with_GEMINI(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.GEMINI))


	def test_isa_when_type_link_with_TUNER(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.TUNER))


	def test_isa_when_type_link_with_SYNCHRO(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.SYNCHRO))


	def test_isa_when_type_link_with_TOKEN(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.TOKEN))


	def test_isa_when_type_link_with_QUICKPLAY(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.QUICKPLAY))


	def test_isa_when_type_link_with_CONTINUOUS(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.CONTINUOUS))


	def test_isa_when_type_link_with_EQUIP(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.EQUIP))


	def test_isa_when_type_link_with_FIELD(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.FIELD))


	def test_isa_when_type_link_with_COUNTER(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.COUNTER))


	def test_isa_when_type_link_with_FLIP(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.FLIP))


	def test_isa_when_type_link_with_TOON(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.TOON))


	def test_isa_when_type_link_with_XYZ(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.XYZ))


	def test_isa_when_type_link_with_PENDULUM(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.PENDULUM))


	def test_isa_when_type_link_with_SPSUMMON(self) -> None:
		self.assertFalse(self.type_link.isa(TypeEnum.SPSUMMON))


	def test_isa_when_type_link_with_LINK(self) -> None:
		self.assertTrue(self.type_link.isa(TypeEnum.LINK))


