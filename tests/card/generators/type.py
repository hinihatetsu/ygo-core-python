import sys
sys.path.append('.')
from typing import TextIO
from ygo_core.enums.type import TypeEnum

types = {
    str(t).replace('__', 'none').replace('.', '_').lower().replace('enum', ''):
    str(t).replace('TypeEnum.', '')
    for t in TypeEnum
}


def setup(file: TextIO) -> None:
    file.write('\tdef setUp(self) -> None:\n')
    for key, val in types.items():
        file.write(f'\t\tself.{key} = Type(TypeEnum.{val})\n')
    file.write('\n\n')


def isa(file: TextIO) -> None:
    for key, val in types.items():
        for t in types.values():
            if t == '__': continue
            file.write(f'\tdef test_isa_when_{key}_with_{t}(self) -> None:\n')
            file.write(f'\t\tself.assert{val == t}(self.{key}.isa(TypeEnum.{t}))\n')
            file.write('\n\n')



with open('tests/card/test_type.py', 'w') as f:
    f.write('from unittest import TestCase\n\n')
    f.write('from ygo_core.card.type import Type\n')
    f.write('from ygo_core.enums.type import TypeEnum\n\n')

    f.write('class TestType(TestCase):\n')
    setup(f)
    isa(f)