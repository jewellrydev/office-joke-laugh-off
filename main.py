#!/usr/bin/env python3
"""Out of Order — entry for One-Line Office Joke Laugh-Off on make.fun.

Prints exactly one line: an original one-line joke about office life.
"""

LINE = "Our printer is the only employee who can announce 'I am out of order' and get a technician instead of a warning."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
