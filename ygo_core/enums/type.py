import enum

class TypeEnum(enum.IntEnum):
    __          = 0x0
    MONSTER     = 0x1
    SPELL       = 0x2
    TRAP        = 0x4
    NORMAL      = 0x10
    EFFECT      = 0x20
    FUSION      = 0x40
    RITUAL      = 0x80
    TRAPMONSTER = 0x100
    SPIRIT      = 0x200
    UNION       = 0x400
    GEMINI      = 0x800
    TUNER       = 0x1000
    SYNCHRO     = 0x2000
    TOKEN       = 0x4000
    QUICKPLAY   = 0x10000
    CONTINUOUS  = 0x20000
    EQUIP       = 0x40000
    FIELD       = 0x80000
    COUNTER     = 0x100000
    FLIP        = 0x200000
    TOON        = 0x400000
    XYZ         = 0x800000
    PENDULUM    = 0x1000000
    SPSUMMON    = 0x2000000
    LINK        = 0x4000000