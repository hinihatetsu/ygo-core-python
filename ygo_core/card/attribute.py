from typing import Union
from ygo_core.enums.attribute import AttributeEnum


class Attribute:
    enum = AttributeEnum
    _value: int

    def __init__(self, value: Union[int, AttributeEnum]) -> None:
        self._value = int(value)


    def isa(self, attr: AttributeEnum) -> bool:
        """ Return True if it has enums.Attribute `attr`."""
        return bool(self._value & int(attr))


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Attribute):
            return NotImplemented
        return self._value == other._value


    def __repr__(self) -> str:
        return ''.join(repr(attr) for attr in AttributeEnum if self.isa(attr))
