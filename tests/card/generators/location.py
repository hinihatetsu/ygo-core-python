import sys
sys.path.append('.')
from typing import TextIO
from ygo_core.enums.location import LocationEnum


locations = {
    str(loc).replace('__', 'none').replace('.', '_').lower().replace('enum', ''):
    str(loc).replace('LocationEnum.', '')
    for loc in LocationEnum
}


def setup(file: TextIO) -> None:
    file.write('\tdef setUp(self) -> None:\n')
    for key, val in locations.items():
        file.write(f'\t\tself.{key} = Location(LocationEnum.{val})\n')
    file.write('\n\n')


def is_zone(file: TextIO) -> None:
    ZONE = LocationEnum.MONSTER_ZONE | LocationEnum.SPELL_ZONE
    for key, val in locations.items():
        file.write(f'\tdef test_is_zone_when_{key}(self) -> None:\n')
        boolean = bool(eval(f'LocationEnum.{val}') & ZONE)
        file.write(f'\t\tself.assert{boolean}(self.{key}.is_zone())\n')
        file.write('\n\n')


def isa(file: TextIO) -> None:
    for key, val in locations.items():
        for loc in locations.values():
            if loc == '__': continue
            file.write(f'\tdef test_isa_when_{key}_with_{loc}(self) -> None:\n')
            boolean = bool(eval(f'LocationEnum.{val}') & eval(f'LocationEnum.{loc}'))
            file.write(f'\t\tself.assert{boolean}(self.{key}.isa(LocationEnum.{loc}))\n')
            file.write('\n\n')


def is_overlay(file: TextIO) -> None:
    for key, val in locations.items():
        file.write(f'\tdef test_is_overlay_when_{key}(self) -> None:\n')
        boolean = (val == 'OVERLAY')
        file.write(f'\t\tself.assert{boolean}(self.{key}.is_overlay())\n')
        file.write('\n\n')


with open('tests/card/test_location.py', 'w') as f:
    f.writelines('from unittest import TestCase\n\n')
    f.write('from ygo_core.card.location import Location\n')
    f.write('from ygo_core.enums.location import LocationEnum\n\n')
    

    f.write('class TestLocation(TestCase):\n')
    setup(f)
    is_zone(f)
    isa(f)
    is_overlay(f)

    