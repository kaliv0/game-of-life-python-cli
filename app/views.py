import curses
from time import sleep

from app.grid import Grid

__all__ = ["CursesView"]


class CursesView:
    def __init__(self, pattern, generation_count=10, frame_rate=7, bbox=(0, 0, 20, 20)):
        self.pattern = pattern
        self.generation_count = generation_count
        self.frame_rate = frame_rate
        self.bbox = bbox

    def render(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        current_grid = Grid(self.pattern)

        # set cursor as invisible
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(f"Terminal too small for pattern {self.pattern.name}")

        # add infinite loop for endless evolution of cells
        for _ in range(self.generation_count):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            screen.refresh()
            # control frames per second
            sleep(1 / self.frame_rate)
