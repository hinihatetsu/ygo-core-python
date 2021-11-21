# YGO core package for Python

## What is this?

This is a core python package for YGO.

This contains basic class for YGO such as `Card`, `DuelField` and `Duel`.

## Requirements

Python 3.9 or later

## Installation

```shell
pip install git+https://github.com/hinihatetsu/ygo_core-python
```

## Example

```python
from ygo_core import Duel
from ygo_core.enums import Player

# create Duel instance
duel = Duel()

# get field
field = duel.field
myfield, oppofield = field

# set decks
duel.set_deck(Player.ME, num_of_main=40, num_of_extra=15)
duel.set_deck(Player.OPPONENT, num_of_main=60, num_of_extra=0)

```

## ToDo

- More docstring
- Improve test coverage
