import tomllib
from dataclasses import dataclass
from pathlib import Path

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"
DATA_ENCODING = "utf-8"


@dataclass
class Pattern:
    """
    represents evolving 'organism'
    """

    name: str
    living_cells: set[tuple]
    # living_cells: set[tuple[int, int]]

    @classmethod
    def init_from_toml(cls, name, data):
        return cls(name=name, living_cells={tuple(cell) for cell in data["living_cells"]})


def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding=DATA_ENCODING))
    return Pattern.init_from_toml(name, data[name])


def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding=DATA_ENCODING))
    return [Pattern.init_from_toml(name, data) for name, data in data.items()]
