import sys
sys.path.append('.')
from typing import TextIO
from ygo_core.enums.race import RaceEnum

races = {
    str(r).replace('__', 'none').replace('.', '_').lower().replace('enum', ''):
    str(r).replace('RaceEnum.', '')
    for r in RaceEnum
}


def setup(file: TextIO) -> None:
    file.write('\tdef setUp(self) -> None:\n')
    for key, val in races.items():
        file.write(f'\t\tself.{key} = Race(RaceEnum.{val})\n')
    file.write('\n\n')


def isa(file: TextIO) -> None:
    for key, val in races.items():
        for r in races.values():
            if r == '__': continue
            file.write(f'\tdef test_isa_when_{key}_with_{r}(self) -> None:\n')
            file.write(f'\t\tself.assert{val == r}(self.{key}.isa(RaceEnum.{r}))\n')
            file.write('\n\n')



with open('tests/card/test_race.py', 'w') as f:
    f.write('from unittest import TestCase\n\n')
    f.write('from ygo_core.card.race import Race\n')
    f.write('from ygo_core.enums.race import RaceEnum\n\n')

    f.write('class TestRace(TestCase):\n')
    setup(f)
    isa(f)