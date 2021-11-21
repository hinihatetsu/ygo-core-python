from typing import NamedTuple, Optional

from ygo_core.card.card import Card
from ygo_core.card.location import Location
from ygo_core.card.type import Type
from ygo_core.zone import Zone, ZoneID



class HalfField():
    """ A half filed class.
    This also contains hand, deck, and extradeck
    """
    hand: list[Card]
    deck: list[Card]
    extradeck: list[Card]
    graveyard: list[Card]
    banished: list[Card]
    monster_zones: list[Zone]
    spell_zones: list[Zone]

    battling_monster: Optional[Card]
    under_attack: bool

    def __init__(self) -> None:
        self.hand = []
        self.deck = []
        self.extradeck = []
        self.graveyard = []
        self.banished = []
        self.monster_zones = [Zone() for _ in range(7)]
        self.spell_zones = [Zone() for _ in range(8)]
        
        self.battling_monster = None
        self.under_attack = False
    
    @property
    def mainmonster_zones(self) -> list[Zone]:
        return self.monster_zones[0:5]

    @property
    def exmonster_zones(self) -> list[Zone]:
        return self.monster_zones[5:7]

    @property
    def Fspell_zone(self) -> Zone:
        return self.spell_zones[5]

    @property
    def pendulum_zones(self) -> list[Zone]:
        return self.spell_zones[6:8]

    @property
    def column_zones(self) -> list[list[Zone]]:
        return [
            [self.spell_zones[0], self.mainmonster_zones[0]],
            [self.spell_zones[1], self.mainmonster_zones[1], self.exmonster_zones[0]],
            [self.spell_zones[2], self.mainmonster_zones[2]],
            [self.spell_zones[3], self.mainmonster_zones[3], self.exmonster_zones[1]],
            [self.spell_zones[4], self.mainmonster_zones[4]]
        ]

    @property
    def exzonemonster_count(self) -> int:
        return sum(int(bool(zone.card)) for zone in self.exmonster_zones)

    @property
    def monster_count(self) -> int:
        return sum(int(bool(zone.card)) for zone in self.monster_zones)

    @property
    def spell_without_Fspell_count(self) -> int:
        return sum(int(bool(zone.card)) for zone in self.spell_zones[0:5])

    @property
    def spell_count(self) -> int:
        return sum(int(bool(zone.card)) for zone in self.spell_zones)

    @property
    def hand_count(self) -> int:
        return len(self.hand)

    @property
    def deck_count(self) -> int:
        return len(self.deck)


    def columncard_count(self, column: int) -> int:
        return sum(int(bool(zone.card)) for zone in self.column_zones[column])

    @property
    def field_count(self) -> int:
        return self.monster_count + self.spell_count

    @property
    def fieldhand_count(self) -> int:
        return self.field_count + self.hand_count

    @property
    def is_field_empty(self) -> bool:
        return self.field_count == 0

    
    def get_card(self, location: Location, index: int) -> Card:
        """ Return a card on field.

        Parameters
        ----------
        location : card.Location
            Location where you get card from.
        index : int
            Index of cards in `loaction`.
            If location is grave and index is 2, then return the second card from the bottom of grave.

        Returns
        -------
        card.Card
            An card object at `index` of `location`.

        Note
        ----
        If `location` is overlay or `location` is invalid,
        return a new card.Card object.
        """
        if location.is_overlay():
            return Card(location=location)

        card: Card = Card()

        if location.is_zone():
            zone: Zone = self.where_zones(location)[index]
            if zone.card:
                card = zone.card        
        else:
            card = self.where_cards(location)[index]

        return card

    
    def add_card(self, card: Card, location: Location, index: int) -> None:
        """ Add card to field.

        Parameters
        ----------
        card : card.Card
            A card object to add.
        location : card.Location
            Place where the card is added to.
        index : int
            Index of `loaction`.
        """
        
        if location.is_overlay():
            if location.is_zone():
                zones: list[Zone] = self.where_zones(location)
                zone: Zone =zones[index]
                if zone.card:
                    zone.card.overlays.append(card.id)
            else:
                cards: list[Card] = self.where_cards(location)
                pcard: Card = cards[index]
                pcard.overlays.append(card.id)
            return
        
        if location.is_zone():
            zones = self.where_zones(location)
            zone = zones[index]
            zone.card = card
        else:
            cards = self.where_cards(location)
            cards.insert(index, card)

    
    def remove_card(self, card: Card, location: Location, index: int) -> None:
        """ Remove a card from field.

        Parameters
        ----------
        card : card.Card
            A card object to remove.
        location : card.Location
            Place where the card is removed from.
        index : int
            Index of `location`.
        """
        if location.is_overlay():
            if location.is_zone():
                zones: list[Zone] = self.where_zones(location)
                zone: Zone = zones[index]
                if zone.card:
                    zone.card.overlays.remove(card.id)
            else:
                cards: list[Card] = self.where_cards(location)
                pcard: Card = cards[index]
                pcard.overlays.remove(card.id)
            return
        
        if location.is_zone():
            zones = self.where_zones(location)
            zone = zones[index]
            zone.card = None
        else:
            cards = self.where_cards(location)
            cards.remove(card)


    def where_cards(self, location: Location) -> list[Card]:
        """ Return list object of `location`.

        Parameters
        ----------
        location : card.Location
            Place.
        
        Returns
        -------
        list
            List object of card.Card.

        Raises
        ------
        ValueError
            Raise if location.is_zone().
        """
        if location.is_zone():
            raise ValueError('`location` is zone. Use where_zones() instead.')
        if location.isa(Location.enum.DECK):
            return self.deck

        elif location.isa(Location.enum.HAND):
            return self.hand

        elif location.isa(Location.enum.GRAVE):
            return self.graveyard

        elif location.isa(Location.enum.BANISHED):
            return self.banished

        elif location.isa(Location.enum.EXTRADECK):
            return self.extradeck

        else:
            return []


    def where_zones(self, location: Location) -> list[Zone]:
        """ Return list object of `location`.

        Parameters
        ----------
        location : card.Location
            Place.
        
        Returns
        -------
        list
            List object of zone.Zone.

        Raises
        ------
        ValueError
            Raise if location is not zone.
        """
        if not location.is_zone():
            raise ValueError('`location` is not zone. Use where_cards() instead.')
        
        if location.isa(Location.enum.MONSTER_ZONE):
            return self.monster_zones

        elif location.isa(Location.enum.SPELL_ZONE):
            return self.spell_zones
        
        else:
            return []
    

    def set_deck(self, num_of_main: int, num_of_extra: int) -> None:
        """ Set deck on field.

        Parameters
        ----------
        num_of_main : int
            Number of cards in main deck.
        num_of_extra : int
            Number of cards in extra deck.
        """
        self.deck = [Card() for _ in range(num_of_main)]
        self.extradeck = [Card() for _ in range(num_of_extra)]
        

    def get_mainzone_monsters(self) -> list[Card]:
        """ Return all the monsters in main monster zone. 
        
        Returns
        -------
        list[card.Card]
            List of all the cards in monster zone.
        """
        return [zone.card for zone in self.mainmonster_zones if zone.card]


    def get_exzone_monsters(self) -> list[Card]:
        """ Return all monsters in extra monster zone.

        Returns
        -------
        list[card.Card]
            List of all the cards in extra monster zone.
        """
        return [zone.card for zone in self.exmonster_zones if zone.card]
    

    def get_monsters(self) -> list[Card]:
        """ Return all the monsters in monster zone.

        Returns
        -------
        list[card.Card]
            List of all the cards in monster zone (main & extra monster zone).
        """
        return [zone.card for zone in self.monster_zones if zone.card]

    
    def get_graveyard_monsters(self) -> list[Card]:
        """ Return all the monsters in graveyard.

        Returns
        -------
        list[card.Card]
            List of all the monster cards in graveyard.
        """
        return [card for card in self.graveyard if card.type == Type.enum.MONSTER]


    def get_graveyard_spells(self) -> list[Card]:
        """ Return all the spells in graveyard.

        Returns
        -------
        list[card.Card]
            List of all the spell cards in graveyard.
        """
        return [card for card in self.graveyard if card.type == Type.enum.SPELL]
    
    
    def get_graveyard_traps(self) -> list[Card]:
        """ Return all the traps in graveyard.

        Returns
        -------
        list[card.Card]
            List of all the trap cards in graveyard.
        """
        return [card for card in self.graveyard if card.type == Type.enum.TRAP]

    
    def get_spells(self) -> list[Card]:
        """ Return all the spells in spell zone.

        Returns
        -------
        list[card.Card]
            List of all the spell cards in spell zone.
        """
        return [zone.card for zone in self.spell_zones if zone.card]
        

    def get_Fspell(self) -> Optional[Card]:
        """ Return the field spell on filed.

        Returns
        -------
        card.Card
            The field spell card on filed.
        """
        return self.Fspell_zone.card

    
    def contains_in_hand(self, card_id: int) -> bool:
        """ Return true if the card is in hand.

        Parameters
        ----------
        card_id : int
            Card id of card.
        
        Returns
        -------
        bool
            Return true if the card of card_id is in hand.
        """
        return card_id in [card.id for card in self.hand]

    
    def contains_in_graveyard(self, card_id: int) -> bool:
        """ Return true if the card is in graveyard.

        Parameters
        ----------
        card_id : int
            Card id of card.
        
        Returns
        -------
        bool
            Return true if the card of card_id is in graveyard.
        """
        return card_id in [card.id for card in  self.graveyard]


    def contains_in_banished(self, card_id: int) -> bool:
        """ Return true if the card is in banished.

        Parameters
        ----------
        card_id : int
            Card id of card.
        
        Returns
        -------
        bool
            Return true if the card of card_id is in banished.
        """
        return card_id in [card.id for card in self.graveyard]


    def contains_in_extradeck(self, card_id: int) -> bool:
        """ Return true if the card is in extradeck.

        Parameters
        ----------
        card_id : int
            Card id of card.
        
        Returns
        -------
        bool
            Return true if the card of card_id is in extradeck.
        """
        return card_id in [card.id for card in self.extradeck]


    def has_attak_monster(self) -> bool:
        """ Return true if attack position monster is on filed.

        Returns
        -------
        bool
            Return true if attack position monster is on filed.
        """
        return any(zone.card.is_attack() for zone in self.monster_zones if zone.card) 

    
    def has_defence_monster(self) -> bool:
        """ Return true if defence position monster is on filed.

        Returns
        -------
        bool
            Return true if defence position monster is on filed.
        """
        return any(zone.card.is_defence() for zone in self.monster_zones if zone.card)



class DuelField(NamedTuple):
    myside: HalfField
    opside: HalfField

    def set_zone_id(self) -> None:
        """ set id to zones """
        for i, mzone in enumerate(self.myside.monster_zones):
            mzone.id = ZoneID(ZoneID.MZONE_0 << i)
        for i, szone in enumerate(self.myside.spell_zones):
            szone.id = ZoneID(ZoneID.SZONE_0 << i)
        for i, mzone in enumerate(self.opside.monster_zones):
            mzone.id = ZoneID(ZoneID.MZONE_0 << i << ZoneID.OPPONENT)
        for i, szone in enumerate(self.opside.spell_zones):
            szone.id = ZoneID(ZoneID.SZONE_0 << i << ZoneID.OPPONENT)