from unittest import TestCase

from ygo_core.card.location import Location
from ygo_core.enums.location import LocationEnum

class TestLocation(TestCase):
	def setUp(self) -> None:
		self.location_none = Location(LocationEnum.__)
		self.location_deck = Location(LocationEnum.DECK)
		self.location_hand = Location(LocationEnum.HAND)
		self.location_monster_zone = Location(LocationEnum.MONSTER_ZONE)
		self.location_spell_zone = Location(LocationEnum.SPELL_ZONE)
		self.location_grave = Location(LocationEnum.GRAVE)
		self.location_banished = Location(LocationEnum.BANISHED)
		self.location_extradeck = Location(LocationEnum.EXTRADECK)
		self.location_overlay = Location(LocationEnum.OVERLAY)
		self.location_onfield = Location(LocationEnum.ONFIELD)
		self.location_fspell_zone = Location(LocationEnum.FSPELL_ZONE)
		self.location_pendulum_zone = Location(LocationEnum.PENDULUM_ZONE)


	def test_is_zone_when_location_none(self) -> None:
		self.assertFalse(self.location_none.is_zone())


	def test_is_zone_when_location_deck(self) -> None:
		self.assertFalse(self.location_deck.is_zone())


	def test_is_zone_when_location_hand(self) -> None:
		self.assertFalse(self.location_hand.is_zone())


	def test_is_zone_when_location_monster_zone(self) -> None:
		self.assertTrue(self.location_monster_zone.is_zone())


	def test_is_zone_when_location_spell_zone(self) -> None:
		self.assertTrue(self.location_spell_zone.is_zone())


	def test_is_zone_when_location_grave(self) -> None:
		self.assertFalse(self.location_grave.is_zone())


	def test_is_zone_when_location_banished(self) -> None:
		self.assertFalse(self.location_banished.is_zone())


	def test_is_zone_when_location_extradeck(self) -> None:
		self.assertFalse(self.location_extradeck.is_zone())


	def test_is_zone_when_location_overlay(self) -> None:
		self.assertFalse(self.location_overlay.is_zone())


	def test_is_zone_when_location_onfield(self) -> None:
		self.assertTrue(self.location_onfield.is_zone())


	def test_is_zone_when_location_fspell_zone(self) -> None:
		self.assertFalse(self.location_fspell_zone.is_zone())


	def test_is_zone_when_location_pendulum_zone(self) -> None:
		self.assertFalse(self.location_pendulum_zone.is_zone())


	def test_isa_when_location_none_with_DECK(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.DECK))


	def test_isa_when_location_none_with_HAND(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.HAND))


	def test_isa_when_location_none_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_none_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_none_with_GRAVE(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.GRAVE))


	def test_isa_when_location_none_with_BANISHED(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.BANISHED))


	def test_isa_when_location_none_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_none_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_none_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_none_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_none_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_none.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_deck_with_DECK(self) -> None:
		self.assertTrue(self.location_deck.isa(LocationEnum.DECK))


	def test_isa_when_location_deck_with_HAND(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.HAND))


	def test_isa_when_location_deck_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_deck_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_deck_with_GRAVE(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.GRAVE))


	def test_isa_when_location_deck_with_BANISHED(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.BANISHED))


	def test_isa_when_location_deck_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_deck_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_deck_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_deck_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_deck_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_deck.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_hand_with_DECK(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.DECK))


	def test_isa_when_location_hand_with_HAND(self) -> None:
		self.assertTrue(self.location_hand.isa(LocationEnum.HAND))


	def test_isa_when_location_hand_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_hand_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_hand_with_GRAVE(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.GRAVE))


	def test_isa_when_location_hand_with_BANISHED(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.BANISHED))


	def test_isa_when_location_hand_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_hand_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_hand_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_hand_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_hand_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_hand.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_monster_zone_with_DECK(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.DECK))


	def test_isa_when_location_monster_zone_with_HAND(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.HAND))


	def test_isa_when_location_monster_zone_with_MONSTER_ZONE(self) -> None:
		self.assertTrue(self.location_monster_zone.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_monster_zone_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_monster_zone_with_GRAVE(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.GRAVE))


	def test_isa_when_location_monster_zone_with_BANISHED(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.BANISHED))


	def test_isa_when_location_monster_zone_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_monster_zone_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_monster_zone_with_ONFIELD(self) -> None:
		self.assertTrue(self.location_monster_zone.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_monster_zone_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_monster_zone_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_monster_zone.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_spell_zone_with_DECK(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.DECK))


	def test_isa_when_location_spell_zone_with_HAND(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.HAND))


	def test_isa_when_location_spell_zone_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_spell_zone_with_SPELL_ZONE(self) -> None:
		self.assertTrue(self.location_spell_zone.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_spell_zone_with_GRAVE(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.GRAVE))


	def test_isa_when_location_spell_zone_with_BANISHED(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.BANISHED))


	def test_isa_when_location_spell_zone_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_spell_zone_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_spell_zone_with_ONFIELD(self) -> None:
		self.assertTrue(self.location_spell_zone.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_spell_zone_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_spell_zone_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_spell_zone.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_grave_with_DECK(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.DECK))


	def test_isa_when_location_grave_with_HAND(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.HAND))


	def test_isa_when_location_grave_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_grave_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_grave_with_GRAVE(self) -> None:
		self.assertTrue(self.location_grave.isa(LocationEnum.GRAVE))


	def test_isa_when_location_grave_with_BANISHED(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.BANISHED))


	def test_isa_when_location_grave_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_grave_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_grave_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_grave_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_grave_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_grave.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_banished_with_DECK(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.DECK))


	def test_isa_when_location_banished_with_HAND(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.HAND))


	def test_isa_when_location_banished_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_banished_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_banished_with_GRAVE(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.GRAVE))


	def test_isa_when_location_banished_with_BANISHED(self) -> None:
		self.assertTrue(self.location_banished.isa(LocationEnum.BANISHED))


	def test_isa_when_location_banished_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_banished_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_banished_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_banished_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_banished_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_banished.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_extradeck_with_DECK(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.DECK))


	def test_isa_when_location_extradeck_with_HAND(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.HAND))


	def test_isa_when_location_extradeck_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_extradeck_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_extradeck_with_GRAVE(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.GRAVE))


	def test_isa_when_location_extradeck_with_BANISHED(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.BANISHED))


	def test_isa_when_location_extradeck_with_EXTRADECK(self) -> None:
		self.assertTrue(self.location_extradeck.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_extradeck_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_extradeck_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_extradeck_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_extradeck_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_extradeck.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_overlay_with_DECK(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.DECK))


	def test_isa_when_location_overlay_with_HAND(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.HAND))


	def test_isa_when_location_overlay_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_overlay_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_overlay_with_GRAVE(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.GRAVE))


	def test_isa_when_location_overlay_with_BANISHED(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.BANISHED))


	def test_isa_when_location_overlay_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_overlay_with_OVERLAY(self) -> None:
		self.assertTrue(self.location_overlay.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_overlay_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_overlay_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_overlay_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_overlay.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_onfield_with_DECK(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.DECK))


	def test_isa_when_location_onfield_with_HAND(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.HAND))


	def test_isa_when_location_onfield_with_MONSTER_ZONE(self) -> None:
		self.assertTrue(self.location_onfield.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_onfield_with_SPELL_ZONE(self) -> None:
		self.assertTrue(self.location_onfield.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_onfield_with_GRAVE(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.GRAVE))


	def test_isa_when_location_onfield_with_BANISHED(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.BANISHED))


	def test_isa_when_location_onfield_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_onfield_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_onfield_with_ONFIELD(self) -> None:
		self.assertTrue(self.location_onfield.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_onfield_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_onfield_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_onfield.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_fspell_zone_with_DECK(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.DECK))


	def test_isa_when_location_fspell_zone_with_HAND(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.HAND))


	def test_isa_when_location_fspell_zone_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_fspell_zone_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_fspell_zone_with_GRAVE(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.GRAVE))


	def test_isa_when_location_fspell_zone_with_BANISHED(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.BANISHED))


	def test_isa_when_location_fspell_zone_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_fspell_zone_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_fspell_zone_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_fspell_zone_with_FSPELL_ZONE(self) -> None:
		self.assertTrue(self.location_fspell_zone.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_fspell_zone_with_PENDULUM_ZONE(self) -> None:
		self.assertFalse(self.location_fspell_zone.isa(LocationEnum.PENDULUM_ZONE))


	def test_isa_when_location_pendulum_zone_with_DECK(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.DECK))


	def test_isa_when_location_pendulum_zone_with_HAND(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.HAND))


	def test_isa_when_location_pendulum_zone_with_MONSTER_ZONE(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.MONSTER_ZONE))


	def test_isa_when_location_pendulum_zone_with_SPELL_ZONE(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.SPELL_ZONE))


	def test_isa_when_location_pendulum_zone_with_GRAVE(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.GRAVE))


	def test_isa_when_location_pendulum_zone_with_BANISHED(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.BANISHED))


	def test_isa_when_location_pendulum_zone_with_EXTRADECK(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.EXTRADECK))


	def test_isa_when_location_pendulum_zone_with_OVERLAY(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.OVERLAY))


	def test_isa_when_location_pendulum_zone_with_ONFIELD(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.ONFIELD))


	def test_isa_when_location_pendulum_zone_with_FSPELL_ZONE(self) -> None:
		self.assertFalse(self.location_pendulum_zone.isa(LocationEnum.FSPELL_ZONE))


	def test_isa_when_location_pendulum_zone_with_PENDULUM_ZONE(self) -> None:
		self.assertTrue(self.location_pendulum_zone.isa(LocationEnum.PENDULUM_ZONE))


	def test_is_overlay_when_location_none(self) -> None:
		self.assertFalse(self.location_none.is_overlay())


	def test_is_overlay_when_location_deck(self) -> None:
		self.assertFalse(self.location_deck.is_overlay())


	def test_is_overlay_when_location_hand(self) -> None:
		self.assertFalse(self.location_hand.is_overlay())


	def test_is_overlay_when_location_monster_zone(self) -> None:
		self.assertFalse(self.location_monster_zone.is_overlay())


	def test_is_overlay_when_location_spell_zone(self) -> None:
		self.assertFalse(self.location_spell_zone.is_overlay())


	def test_is_overlay_when_location_grave(self) -> None:
		self.assertFalse(self.location_grave.is_overlay())


	def test_is_overlay_when_location_banished(self) -> None:
		self.assertFalse(self.location_banished.is_overlay())


	def test_is_overlay_when_location_extradeck(self) -> None:
		self.assertFalse(self.location_extradeck.is_overlay())


	def test_is_overlay_when_location_overlay(self) -> None:
		self.assertTrue(self.location_overlay.is_overlay())


	def test_is_overlay_when_location_onfield(self) -> None:
		self.assertFalse(self.location_onfield.is_overlay())


	def test_is_overlay_when_location_fspell_zone(self) -> None:
		self.assertFalse(self.location_fspell_zone.is_overlay())


	def test_is_overlay_when_location_pendulum_zone(self) -> None:
		self.assertFalse(self.location_pendulum_zone.is_overlay())


