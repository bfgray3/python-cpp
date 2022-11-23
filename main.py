#!/usr/bin/env python
import argparse
import ctypes
import time
from collections.abc import Sequence

from python import functions


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", nargs="?", default=20, type=int, choices=range(1, 32))
    args = parser.parse_args()

    n = (1 << args.n) - 1

    python_function = functions.f
    c_function = ctypes.CDLL("./sharedlibrary.so").f

    python_start = time.perf_counter()
    p = python_function(n)
    python_end = time.perf_counter()
    print("python:", python_end - python_start)

    c_start = time.perf_counter()
    # TODO: try https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL
    c = c_function(n)  # no GIL

    c_end = time.perf_counter()
    print("c:", c_end - c_start)

    assert p == c

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
