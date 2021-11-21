from unittest import TestCase

from ygo_core.card.attribute import Attribute
from ygo_core.enums.attribute import AttributeEnum

class TestAttribute(TestCase):
	def setUp(self) -> None:
		self.attribute_none = Attribute(AttributeEnum.__)
		self.attribute_earth = Attribute(AttributeEnum.EARTH)
		self.attribute_water = Attribute(AttributeEnum.WATER)
		self.attribute_fire = Attribute(AttributeEnum.FIRE)
		self.attribute_wind = Attribute(AttributeEnum.WIND)
		self.attribute_light = Attribute(AttributeEnum.LIGHT)
		self.attribute_dark = Attribute(AttributeEnum.DARK)
		self.attribute_divine = Attribute(AttributeEnum.DIVINE)


	def test_isa_when_attribute_none_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_none_with_WATER(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_none_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_none_with_WIND(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_none_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_none_with_DARK(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_none_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_none.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_earth_with_EARTH(self) -> None:
		self.assertTrue(self.attribute_earth.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_earth_with_WATER(self) -> None:
		self.assertFalse(self.attribute_earth.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_earth_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_earth.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_earth_with_WIND(self) -> None:
		self.assertFalse(self.attribute_earth.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_earth_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_earth.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_earth_with_DARK(self) -> None:
		self.assertFalse(self.attribute_earth.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_earth_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_earth.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_water_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_water.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_water_with_WATER(self) -> None:
		self.assertTrue(self.attribute_water.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_water_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_water.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_water_with_WIND(self) -> None:
		self.assertFalse(self.attribute_water.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_water_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_water.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_water_with_DARK(self) -> None:
		self.assertFalse(self.attribute_water.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_water_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_water.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_fire_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_fire.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_fire_with_WATER(self) -> None:
		self.assertFalse(self.attribute_fire.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_fire_with_FIRE(self) -> None:
		self.assertTrue(self.attribute_fire.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_fire_with_WIND(self) -> None:
		self.assertFalse(self.attribute_fire.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_fire_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_fire.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_fire_with_DARK(self) -> None:
		self.assertFalse(self.attribute_fire.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_fire_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_fire.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_wind_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_wind.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_wind_with_WATER(self) -> None:
		self.assertFalse(self.attribute_wind.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_wind_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_wind.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_wind_with_WIND(self) -> None:
		self.assertTrue(self.attribute_wind.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_wind_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_wind.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_wind_with_DARK(self) -> None:
		self.assertFalse(self.attribute_wind.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_wind_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_wind.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_light_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_light.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_light_with_WATER(self) -> None:
		self.assertFalse(self.attribute_light.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_light_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_light.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_light_with_WIND(self) -> None:
		self.assertFalse(self.attribute_light.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_light_with_LIGHT(self) -> None:
		self.assertTrue(self.attribute_light.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_light_with_DARK(self) -> None:
		self.assertFalse(self.attribute_light.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_light_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_light.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_dark_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_dark.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_dark_with_WATER(self) -> None:
		self.assertFalse(self.attribute_dark.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_dark_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_dark.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_dark_with_WIND(self) -> None:
		self.assertFalse(self.attribute_dark.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_dark_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_dark.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_dark_with_DARK(self) -> None:
		self.assertTrue(self.attribute_dark.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_dark_with_DIVINE(self) -> None:
		self.assertFalse(self.attribute_dark.isa(AttributeEnum.DIVINE))


	def test_isa_when_attribute_divine_with_EARTH(self) -> None:
		self.assertFalse(self.attribute_divine.isa(AttributeEnum.EARTH))


	def test_isa_when_attribute_divine_with_WATER(self) -> None:
		self.assertFalse(self.attribute_divine.isa(AttributeEnum.WATER))


	def test_isa_when_attribute_divine_with_FIRE(self) -> None:
		self.assertFalse(self.attribute_divine.isa(AttributeEnum.FIRE))


	def test_isa_when_attribute_divine_with_WIND(self) -> None:
		self.assertFalse(self.attribute_divine.isa(AttributeEnum.WIND))


	def test_isa_when_attribute_divine_with_LIGHT(self) -> None:
		self.assertFalse(self.attribute_divine.isa(AttributeEnum.LIGHT))


	def test_isa_when_attribute_divine_with_DARK(self) -> None:
		self.assertFalse(self.attribute_divine.isa(AttributeEnum.DARK))


	def test_isa_when_attribute_divine_with_DIVINE(self) -> None:
		self.assertTrue(self.attribute_divine.isa(AttributeEnum.DIVINE))


