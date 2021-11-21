from pathlib import Path
from typing import Union


class Deck:
    main: list[int]
    extra: list[int]
    side: list[int]

    def __init__(self) -> None:
        self.main = []
        self.extra = []
        self.side = []

    
    def load(self, path: Union[str, Path]) -> None:
        """ Load deck from a ydk file. 

        Parameters
        ----------
        path : str | PathLike
            Deck will be loaded from this `path`.


        Raises
        ------
        FileNotFoundError
            raises when `path` does not exist

        ValueError
            raise when suffix of `path` is not ydk

        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f'File `{str(path)}` does not exist')

        if path.suffix != '.ydk':
            raise ValueError(f'The file extension is invalid. valid: ydk, got {path.suffix}')
        

        box: list[int] = self.main
        with path.open() as f:
            for line in f.readlines():
                line = line.strip()
                if line == '#extra':
                    box = self.extra
                elif line == '!side':
                    box = self.side

                try:
                    id = int(line)
                    box.append(id)
                except ValueError as err:
                    pass

        

    @property
    def count_main(self) -> int:
        """ Count of cards in main. """
        return len(self.main)
    
    @property
    def count_extra(self) -> int:
        """ Count of cards in extra. """
        return len(self.extra)

    @property
    def count_side(self) -> int:
        """ Count of cards in side. """
        return len(self.side)

    @property
    def count(self) -> int:
        """ Count of total cards in deck (including side). """
        return self.count_main + self.count_extra + self.count_side
                
