from typing import Union
from ygo_core.enums.race import RaceEnum


class Race:
    enum = RaceEnum
    
    def __init__(self, value: Union[int, RaceEnum]) -> None:
        self._value: int = int(value)


    def isa(self, race: RaceEnum) -> bool:
        """ Return True if it has enums.Race `race`."""
        return bool(self._value & int(race))


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Race):
            return NotImplemented
        return self._value == other._value


    def __repr__(self) -> str:
        return ''.join(repr(race) for race in RaceEnum if self.isa(race))