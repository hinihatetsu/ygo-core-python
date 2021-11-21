from typing import Optional

from ygo_core.field import HalfField, DuelField
from ygo_core.card.card import Card
from ygo_core.card.location import Location
from ygo_core.zone import Zone
from ygo_core.enums.player import Player
from ygo_core.enums.phase import Phase



class Duel:
    _field: DuelField
    _players: tuple[Player, Player]
    _turn_player: Player
    _turn: int
    _phase: Phase
    _life: list[int]

    _mainphase_end: bool
    _summoning: list[Card]
    _last_summoned: list[Card]
    _last_summon_player: Player

    _current_chain: list[Card]
    _last_chain_player: Player
    _chain_targets: list[Card]
    _current_chain_target: list[Card]


    def __init__(self) -> None:
        self.init()
        self._field.set_zone_id()


    def init(self) -> None:
        """ Initialize duel state. """
        self._field = DuelField(HalfField(), HalfField())
        self._players = (Player.NONE, Player.NONE)
        self._turn_player = Player.NONE
        self._turn = 0
        self._phase = Phase.DRAW
        self._life = [8000, 8000]

        self._mainphase_end = False
        self._summoning = []
        self._last_summoned = []
        self._last_summon_player = Player.NONE

        self._current_chain = []
        self._last_chain_player = Player.NONE
        self._chain_targets = []
        self._current_chain_target = []


    @property
    def players(self) -> tuple[Player, Player]:
        """ Two players in duel. """
        return self._players

    @property
    def turn_player(self) -> Player:
        """ Current turn player. """
        return self._turn_player

    @property
    def turn(self) -> int:
        """ Current turn. """
        return self._turn

    @property
    def phase(self) -> Phase:
        """ Current phase. """
        return self._phase

    @property
    def life(self) -> list[int]:
        """ Current lifes of two players. """
        return self._life
    
    @property 
    def field(self) -> DuelField:
        """ Current field. """
        return self._field

    @property
    def current_chain(self) -> list[Card]:
        """ List of chain blocks. """
        return self._current_chain

    @property
    def last_chain_player(self) -> Player:
        """ Last chain palyer. """
        return self._last_chain_player

    @property
    def chain_targets(self) -> list[Card]:
        """ List of chain targets. """
        return self._chain_targets


    def set_deck(self, player: Player, num_of_main: int, num_of_extra: int) -> None:
        """ Set deck of either player.

        Parameters
        ----------
        player : Player
            Either Player.ME or Player.OPPONENT.
        num_of_main : int
            Number of cards in main deck.
        num_of_extra : int
            Number of cards in extra deck.
        
        """
        self._field[player].set_deck(num_of_main, num_of_extra)


    def get_card(self, controller: Player, location: Location, index: int) -> Card:
        """ Return the card determined by `controller`, `location` and `index`. 
        
        Parameters
        ----------
        controller : Player
            Either Player.ME or Player.OPPONENT.
        locaiton : Location
            Location of card.
        index : int
            Index in the `location`.

        Returns
        -------
        Card
            Card determined by `controller`, `location` and `index`.
        
        """
        return self._field[controller].get_card(location, index)


    def add_card(self, card: Card, controller: Player, location: Location, index: int) -> None:
        card.controller = controller
        card.location = location
        self._field[controller].add_card(card, location, index)

    
    def remove_card(self, card: Card, controller: Player, location: Location, index: int) -> None:
        self._field[controller].remove_card(card, location, index)

    
    def get_cards(self, controller: Player, location: Location) -> list[Optional[Card]]:
        if location.is_zone():
            zones: list[Zone] = self._field[controller].where_zones(location)
            cards: list[Optional[Card]] = [zone.card for zone in zones]

        else:
            cards = [card for card in self._field[controller].where_cards(location)]

        return cards 
    

    def at_mainphase_end(self) -> None:
        self._mainphase_end = True


    def on_start(self, first_player: Player) -> None:
        self.init()
        self._players = (first_player, (Player.OPPONENT if first_player == Player.ME else Player.ME))


    def on_new_turn(self, turn_player: Player) -> None:
        self._turn_player = turn_player
        self._turn += 1


    def on_new_phase(self, phase: Phase) -> None:
        self._phase = phase
        for player in self.players:
            self._field[player].battling_monster = None
            self._field[player].under_attack = False

        for monster in self._field[0].get_monsters():
            monster.attacked = False

        self._mainphase_end = False
    

    def on_summoning(self, player: Player, card: Card) -> None:
        self._last_summoned.clear()
        self._summoning.append(card)
        self._last_summon_player = player

    
    def on_summoned(self) -> None:
        self._last_summoned = [card for card in self._summoning]
        self._summoning.clear()

    
    def on_spsummoned(self) -> None:
        self.on_summoned()
        for card in self._last_summoned:
            card.is_special_summoned = True

    
    def on_chaining(self, last_chain_player: Player, card: Card) -> None:
        self._last_chain_player = last_chain_player
        self._last_summon_player = Player.NONE
        self._current_chain.append(card)
        self._current_chain_target.clear()


    def on_chain_end(self) -> None:
        self._mainphase_end = False
        self._last_chain_player = Player.NONE
        self._current_chain.clear()
        self._chain_targets.clear()
        self._current_chain_target.clear()


    def on_become_target(self, card: Card) -> None:
        self._chain_targets.append(card)
        self._current_chain_target.append(card)


    def on_draw(self, player: Player) -> None:
        self._field[player].deck.pop()
        self._field[player].hand.append(Card(location=Location(Location.enum.HAND)))


    def on_damage(self, player: Player, damage: int) -> None:
        self._life[player] = max(self._life[player] - damage, 0)


    def on_recover(self, player: Player, recover: int) -> None:
        self._life[player] += recover

    
    def on_lp_update(self, player: Player, lp: int) -> None:
        self._life[player] = lp

    
    def on_attack(self, attacking: Card, attacked: Card) -> None:
        self._field[attacking.controller].battling_monster = attacking
        self._field[attacking.controller ^ 1].battling_monster = attacked
        self._field[attacking.controller ^ 1].under_attack = True


    def on_battle(self) -> None:
        self._field[Player.ME].under_attack = False
        self._field[Player.OPPONENT].under_attack = False
