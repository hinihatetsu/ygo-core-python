from typing import Union
from ygo_core.enums.type import TypeEnum

class Type:
    enum = TypeEnum
    
    def __init__(self, value: Union[int, TypeEnum]) -> None:
        self._value: int = int(value)

    
    def isa(self, t: TypeEnum) -> bool:
        """ Return True if it has enums.Type `t`."""
        return bool(self._value & int(t))


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Type):
            return NotImplemented
        return self._value == other._value


    def __repr__(self) -> str:
        return ''.join(repr(t) for t in TypeEnum if self.isa(t))