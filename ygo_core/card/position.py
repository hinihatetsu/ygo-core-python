from typing import Union
from ygo_core.enums.position import PositionEnum


class Position:
    enum = PositionEnum
    _value: int

    def __init__(self, value: Union[int, PositionEnum]) -> None:
        self._value: int = int(value)

    
    @property
    def value(self) -> int:
        return self._value

    
    def isa(self, pos: PositionEnum) -> bool:
        return bool(self._value & int(pos))


    def is_attack(self) -> bool:
        return self.isa(PositionEnum.ATTACK)


    def is_defence(self) -> bool:
        return self.isa(PositionEnum.DEFENCE)


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self._value == other._value


    def __repr__(self) -> str:
        return ''.join(repr(pos) for pos in PositionEnum if self.isa(pos))