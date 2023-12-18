from dataclasses import dataclass


@dataclass
class Pattern:
    """
    represents evolving 'organism'
    """

    name: str
    living_cells: set[tuple[int, int]]
