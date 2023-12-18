import curses
from time import sleep

from app.grid import Grid
from app.patterns import Pattern


class CursesView:
    def __init__(
        self,
        pattern: Pattern,
        generation_count: int = 8,
        frame_rate: int = 4,
        bbox: tuple[int] = (0, 0, 20, 20),
    ):
        self.pattern = pattern
        self.generation_count = generation_count
        self.frame_rate = frame_rate
        self.bbox = bbox

    def render(self) -> None:
        curses.wrapper(self._draw)

    def _draw(self, screen: curses.window) -> None:
        current_grid = Grid(self.pattern)
        # set cursor as invisible
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.prepare_grid_view(self.bbox))
        except curses.error:
            raise ValueError(f"Terminal too small for pattern {self.pattern.name}")

        for _ in range(self.generation_count):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.prepare_grid_view(self.bbox))
            screen.refresh()
            # control frames per second
            sleep(1 / self.frame_rate)
