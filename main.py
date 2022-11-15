#!/usr/bin/env python
import ctypes
import time
from collections.abc import Sequence

from python import functions

N = 2**32 - 1


def main(argv: Sequence[str] | None = None) -> int:
    python_start = time.perf_counter()
    functions.f(N)
    python_end = time.perf_counter()
    print("python:", python_end - python_start)

    c_start = time.perf_counter()
    # TODO: try https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL
    ctypes.CDLL("./sharedlibrary.so").f(N)  # no GIL
    c_end = time.perf_counter()
    print("c:", c_end - c_start)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
