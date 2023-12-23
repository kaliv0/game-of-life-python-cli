import pathlib
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import List

PATTERNS_FILE = Path(__file__).parent.joinpath("resources", "patterns.toml")
DATA_ENCODING = "utf-8"


@dataclass
class Pattern:
    name: str
    living_cells: set[tuple[int, ...]]

    @classmethod
    def init_from_toml(cls, name: str, data: dict):
        return cls(name=name, living_cells={tuple(cell) for cell in data["living_cells"]})


def get_pattern(name: str, filename: pathlib.Path = PATTERNS_FILE) -> Pattern:
    data = tomllib.loads(filename.read_text(encoding=DATA_ENCODING))
    return Pattern.init_from_toml(name, data[name])


def get_all_patterns(filename: pathlib.Path = PATTERNS_FILE) -> List[Pattern]:
    data = tomllib.loads(filename.read_text(encoding=DATA_ENCODING))
    return [Pattern.init_from_toml(name, data) for name, data in data.items()]
