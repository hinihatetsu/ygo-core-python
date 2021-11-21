import enum


class AttributeEnum(enum.IntEnum):
    __     = 0x0
    EARTH  = 0x1
    WATER  = 0x2
    FIRE   = 0x4
    WIND   = 0x08
    LIGHT  = 0x10
    DARK   = 0x20
    DIVINE = 0x40