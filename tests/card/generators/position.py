import sys
sys.path.append('.')
from typing import TextIO
from ygo_core.enums.position import PositionEnum

poss = {
    str(pos).replace('__', 'none').replace('.', '_').lower().replace('enum', ''):
    str(pos).replace('PositionEnum.', '')
    for pos in PositionEnum
}


def setup(file: TextIO) -> None:
    file.write('\tdef setUp(self) -> None:\n')
    for key, val in poss.items():
        file.write(f'\t\tself.{key} = Position(PositionEnum.{val})\n')
    file.write('\n\n')


def isa(file: TextIO) -> None:
    for key, val in poss.items():
        for pos in poss.values():
            if pos == '__': continue
            file.write(f'\tdef test_isa_when_{key}_with_{pos}(self) -> None:\n')
            boolean = bool(eval(f'PositionEnum.{val}') & eval(f'PositionEnum.{pos}'))
            file.write(f'\t\tself.assert{boolean}(self.{key}.isa(PositionEnum.{pos}))\n')
            file.write('\n\n')


def is_attack(file: TextIO) -> None:
    for key, val in poss.items():
        file.write(f'\tdef test_is_attack_when_{key}(self) -> None:\n')
        boolean = bool(eval(f'PositionEnum.{val}') & PositionEnum.ATTACK)
        file.write(f'\t\tself.assert{boolean}(self.{key}.is_attack())\n')
        file.write('\n\n')


def is_defence(file: TextIO) -> None:
    for key, val in poss.items():
        file.write(f'\tdef test_is_defence_when_{key}(self) -> None:\n')
        boolean = bool(eval(f'PositionEnum.{val}') & PositionEnum.DEFENCE)
        file.write(f'\t\tself.assert{boolean}(self.{key}.is_defence())\n')
        file.write('\n\n')


with open('tests/card/test_position.py', 'w') as f:
    f.write('from unittest import TestCase\n\n')
    f.write('from ygo_core.card.position import Position\n')
    f.write('from ygo_core.enums.position import PositionEnum\n\n')

    f.write('class TestPosition(TestCase):\n')
    setup(f)
    isa(f)
    is_attack(f)
    is_defence(f)