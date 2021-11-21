"""
Core package of YGO
"""

__version__ = '0.1.0'

from .duel import Duel
from .deck import Deck
from .card.card import Card


__all__ = [
    'Duel',
    'Deck',
    'Card'
]