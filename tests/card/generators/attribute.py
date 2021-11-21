import sys
sys.path.append('.')
from typing import TextIO
from ygo_core.enums.attribute import AttributeEnum

attributes = {
    str(attr).replace('__', 'none').replace('.', '_').lower().replace('enum', ''):
    str(attr).replace('AttributeEnum.', '')
    for attr in AttributeEnum
}


def setup(file: TextIO) -> None:
    file.write('\tdef setUp(self) -> None:\n')
    for key, val in attributes.items():
        file.write(f'\t\tself.{key} = Attribute(AttributeEnum.{val})\n')
    file.write('\n\n')


def isa(file: TextIO) -> None:
    for key, val in attributes.items():
        for attr in attributes.values():
            if attr == '__': continue
            file.write(f'\tdef test_isa_when_{key}_with_{attr}(self) -> None:\n')
            file.write(f'\t\tself.assert{val == attr}(self.{key}.isa(AttributeEnum.{attr}))\n')
            file.write('\n\n')



with open('tests/card/test_attribute.py', 'w') as f:
    f.write('from unittest import TestCase\n\n')
    f.write('from ygo_core.card.attribute import Attribute\n')
    f.write('from ygo_core.enums.attribute import AttributeEnum\n\n')

    f.write('class TestAttribute(TestCase):\n')
    setup(f)
    isa(f)