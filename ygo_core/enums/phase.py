import enum

class Phase(enum.IntEnum):
    DRAW         = 0x1
    STANBY       = 0x2
    MAIN1        = 0x4
    BATTLE_START = 0x8
    BATTLE_STEP  = 0x10
    DAMAGE_STEP  = 0x20
    DAMAGE_CALC  = 0x40
    BATTLE       = 0x80
    MAIN2        = 0x100
    END          = 0x200