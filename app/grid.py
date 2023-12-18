import collections
from dataclasses import dataclass

# deltas used to determine neighbours' coordinates for each cell
NEIGHBOUR_DELTAS = (
    (-1, -1),  # above left
    (-1, 0),  # above
    (-1, 1),  # above right
    (0, -1),  # left
    (0, 1),  # right
    (1, -1),  # below left
    (1, 0),  # below
    (1, 1),  # below right
)


@dataclass
class CellState:
    DEAD = " "
    ALIVE = "#"


class Grid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self) -> None:
        living_neighbours = collections.defaultdict(int)
        # determine number of living neighbours for every cell
        for row, col in self.pattern.living_cells:
            for dlt_row, dlt_col in NEIGHBOUR_DELTAS:
                neighbour_coordinate = (row + dlt_row, col + dlt_col)
                living_neighbours[neighbour_coordinate] += 1

        surviving_neighbours = {
            cell_coordinates
            for cell_coordinates, count in living_neighbours.items()
            if count in {2, 3}
        }
        total_survivors = surviving_neighbours & self.pattern.living_cells  # intersection

        reproducing_neighbours = {
            cell_coordinates for cell_coordinates, count in living_neighbours.items() if count == 3
        }
        new_offspring = reproducing_neighbours - self.pattern.living_cells  # difference

        self.pattern.living_cells = total_survivors | new_offspring  # union of both sets

    def prepare_grid_view(self, bbox: tuple[int]) -> str:
        start_row, start_col, end_row, end_col = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]

        for row in range(start_row, end_row):
            display_row = []
            for col in range(start_col, end_col):
                if (row, col) in self.pattern.living_cells:
                    curr_state = CellState.ALIVE
                else:
                    curr_state = CellState.DEAD
                display_row.append(curr_state)
            display.append(" ".join(display_row))

        return "\n ".join(display)
