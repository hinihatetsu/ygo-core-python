import enum


class LinkMarker(enum.IntEnum):
    BOTTOM_LEFT  = 0x1
    BOTTOM       = 0x2
    BOTTOM_RIGHT = 0x4
    LEFT         = 0x10
    RIGHT        = 0x40
    TOP_LEFT     = 0x100
    TOP          = 0x200
    TOP_RIGHT    = 0x400