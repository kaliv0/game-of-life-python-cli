import sys

from app import views, patterns
from app.cli import get_command_line_args


def main():
    args = get_command_line_args()
    # TODO: unnecessary -> only one view available
    View = getattr(views, args.view)

    if args.all:
        for pattern in patterns.get_all_patterns():
            _show_pattern(View, pattern, args)
    else:
        _show_pattern(View, patterns.get_pattern(name=args.pattern), args)


def _show_pattern(View, pattern, args):
    try:
        View(pattern=pattern, generation_count=args.gen, frame_rate=args.fps).render()
    except Exception as e:
        # TODO: refactor error loging
        print(e, file=sys.stderr)


if __name__ == "__main__":
    main()
