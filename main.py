#!/usr/bin/env python
import argparse
import ctypes
import time
from collections.abc import Sequence

from python import functions


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", nargs="?", default=1 << 20 - 1, type=int)
    args = parser.parse_args()

    python_start = time.perf_counter()
    p = functions.f(args.n)
    python_end = time.perf_counter()
    print("python:", python_end - python_start)

    c_start = time.perf_counter()
    # TODO: try https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL
    c = ctypes.CDLL("./sharedlibrary.so").f(args.n)  # no GIL
    c_end = time.perf_counter()
    print("c:", c_end - c_start)

    assert p == c

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
