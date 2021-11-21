import enum

class LocationEnum(enum.IntEnum):
    __            = 0x0
    DECK          = 0x1
    HAND          = 0x2
    MONSTER_ZONE  = 0x4
    SPELL_ZONE    = 0x8
    GRAVE         = 0x10
    BANISHED      = 0x20
    EXTRADECK     = 0x40
    OVERLAY       = 0x80
    ONFIELD = MONSTER_ZONE | SPELL_ZONE
    FSPELL_ZONE   = 0x100
    PENDULUM_ZONE = 0x200
    