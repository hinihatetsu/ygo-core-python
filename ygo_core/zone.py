import enum
from typing import Optional

from ygo_core.card.card import Card

class ZoneID(enum.IntEnum):
    NONE    = 0x0
    MZONE_0 = 0x1
    MZONE_1 = 0x2
    MZONE_2 = 0x4
    MZONE_3 = 0x8
    MZONE_4 = 0x10
    EXZONE_0 = 0x20
    EXZONE_1 = 0x40
    MAINMONSTER_ZONE = MZONE_0 | MZONE_1 | MZONE_2 | MZONE_3 | MZONE_4
    EXMONSTER_ZONE = EXZONE_0 | EXZONE_1
    MONSTER_ZONE = MAINMONSTER_ZONE | EXMONSTER_ZONE

    SZONE_0 = 0x100
    SZONE_1 = 0x200
    SZONE_2 = 0x400
    SZONE_3 = 0x800
    SZONE_4 = 0x1000
    PZONE = 0xc000
    SPELL_ZONE = SZONE_0 | SZONE_1 | SZONE_2 | SZONE_3 | SZONE_4

    OPPONENT = 16


class Zone:
    card: Optional[Card]
    id: ZoneID
    
    def __init__(self) -> None:
        self.card = None
        self.id = ZoneID.NONE # used to select place

    
    def __repr__(self) -> str:
        return f'<card:{self.card}>'

