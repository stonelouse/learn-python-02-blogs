#!/usr/bin/env python3

import sys


def classify_number(value: int) -> str:
    if value == 0:
        return "zero"
    elif value % 4 == 0:
        return "multiple of 4"
    elif value % 2 == 1:
        return "odd"
    else:
        return "no idea"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: py_03_number_check.py <non-negative integer>", file=sys.stderr)
        return 1

    raw_value = sys.argv[1]

    try:
        number = int(raw_value)
    except ValueError:
        print("Error: the argument must be an integer.", file=sys.stderr)
        return 1

    if number < 0:
        print("Error: the argument must be a non-negative integer.", file=sys.stderr)
        return 1

    print(classify_number(number))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
