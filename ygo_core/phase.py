from typing import Generator

from ygo_core.card.card import Card

class MainPhase:
    summonable: list[Card]
    special_summonable: list[Card]
    repositionable: list[Card]
    monster_settable: list[Card] 
    spell_settable: list[Card]
    activatable: list[Card]
    activation_descs: list[int]
    can_battle: bool
    can_end: bool

    def __init__(self) -> None:
        self.summonable = []
        self.special_summonable = []
        self.repositionable = []
        self.monster_settable = []
        self.spell_settable = []
        self.activatable = []
        self.activation_descs = []
        self.can_battle = False
        self.can_end = False


    def __iter__(self) -> Generator[list[Card], None, None]:
        return self.__generator__()


    def __generator__(self) -> Generator[list[Card], None, None]:
        yield self.summonable
        yield self.special_summonable
        yield self.repositionable
        yield self.monster_settable
        yield self.spell_settable
        yield self.activatable


    def __len__(self) -> int:
        return sum(len(lst) for lst in self)


class BattlePhase:
    attackable: list[Card]
    activatable: list[Card]
    activation_descs: list[int]
    can_main2: bool
    can_end: bool

    def __init__(self) -> None:
        self.attackable = []
        self.activatable = []
        self.activation_descs = []
        self.can_main2 = False
        self.can_end = False


        