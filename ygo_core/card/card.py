from __future__ import annotations
from typing import Optional

from ygo_core.enums.player import Player
from ygo_core.card.location import Location
from ygo_core.card.attribute import Attribute
from ygo_core.card.race import Race
from ygo_core.card.type import Type
from ygo_core.card.position import Position



class Card:
    """ A class representing YGO card """
    def __init__(self, card_id: int=0, location: Location=Location(0)) -> None:
        # card info
        self.id: int = card_id
        self.arias: int = 0
        self.type: Type = Type(0)
        self.level: int = 0
        self.rank: int = 0
        self.attribute: Attribute = Attribute(0)
        self.race: Race = Race(0)
        self.attack: int = 0
        self.defence: int = 0
        self.base_attack: int = 0
        self.base_defence: int = 0
        self.lscale: int = 0
        self.rscale: int = 0
        self.link: int = 0
        self.linkmarker: int = 0

        # status in duel
        self.controller: Player = Player.NONE
        self.location: Location = location
        self.position: Position = Position(0)
        self.target_cards: list[Card] = []
        self.targeted_by: list[Card] = []
        self.equip_target: Optional[Card] = None
        self.equip_cards: list[Card] = []
        self.overlays: list[int] = []
        self.reason: int = 0
        self.reason_card: Optional[Card] = None
        self.counters: dict[int, int] = dict()

        # status flag
        self.status: int = 0
        self.attacked: bool = False
        self.can_direct_attack: bool = False
        self.is_special_summoned: bool = False
        self.is_faceup: bool = False


    def is_attack(self) -> bool:
        """ Return True if the position is attack.

        Returns
        -------
        bool
            True if the position is attack.
        """
        return self.position.is_attack()


    def is_defence(self) -> bool:
        """ Return True if the position is defence.
        
        Returns
        -------
        bool
            True if the position is defence.
        """
        return self.position.is_defence()


    def __repr__(self) -> str:
        return f'<{self.id}>'