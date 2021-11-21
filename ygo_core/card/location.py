from __future__ import annotations
from typing import Union
from ygo_core.enums.location import LocationEnum

class Location:
    """ Location is logical sum of enums.Location. """
    enum = LocationEnum
    ZONE = LocationEnum.MONSTER_ZONE | LocationEnum.SPELL_ZONE
    _value: int

    def __init__(self, value: Union[int, LocationEnum]) -> None:
        self._value = int(value)

    
    @property
    def value(self) -> int:
        return self._value


    def is_zone(self) -> bool:
        return bool(self._value & self.ZONE)


    def isa(self, loc: LocationEnum) -> bool:
        """ Return True if it has enums.Location `loc`"""
        return bool(self._value & int(loc))


    def is_overlay(self) -> bool:
        return self.isa(LocationEnum.OVERLAY)


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):
            return NotImplemented
        return self.value == other.value

    
    def __repr__(self) -> str:
        return ''.join(repr(loc) for loc in LocationEnum if self.isa(loc))