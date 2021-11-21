import enum


class Query(enum.IntEnum):
    ID           = 0x1
    POSITION     = 0x2
    ALIAS        = 0x4
    TYPE         = 0x8
    LEVEL        = 0x10
    RANK         = 0x20
    ATTRIBUTE    = 0x40
    RACE         = 0x80
    ATTACK       = 0x100
    DEFENCE      = 0x200
    BASE_ATTACK  = 0x400
    BASE_DEFENCE = 0x800
    REASON       = 0x1000
    REASON_CARD  = 0x2000
    EQUIP_CARD   = 0x4000
    TARGET_CARD  = 0x8000
    OVERLAY_CARD = 0x10000
    COUNTERS     = 0x20000
    CONTROLLER   = 0x40000
    STATUS       = 0x80000
    IS_PUBLIC    = 0x100000
    LSCALE       = 0x200000
    RSCALE       = 0x400000
    LINK         = 0x800000
    IS_HIDDEN    = 0x1000000
    COVER        = 0x2000000
    END          = 0x80000000