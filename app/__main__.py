import argparse

from app import patterns
from app.cli import get_command_line_args
from app.patterns import Pattern
from app.views import CursesView


def main():
    args = get_command_line_args()
    if args.gen <= 0 or args.fps <= 0:
        raise argparse.ArgumentTypeError(
            "Generation count and frame rate must be greater than zero"
        )

    if args.all:
        while True:
            for pattern in patterns.get_all_patterns():
                _show_pattern(pattern, args)
    else:
        while True:
            _show_pattern(patterns.get_pattern(name=args.pattern), args)


def _show_pattern(pattern: Pattern, args: argparse.Namespace) -> None:
    CursesView(pattern=pattern, generation_count=args.gen, frame_rate=args.fps).render()


if __name__ == "__main__":
    main()
