#!/usr/bin/env python
import argparse
import ctypes
import time
from collections.abc import Sequence

from python import functions


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", nargs="?", default=20, type=int, choices=range(1, 32))
    parser.add_argument("--language", choices=("c", "cpp"), required=True)
    args = parser.parse_args()

    n = (1 << args.n) - 1

    dll = ctypes.CDLL(f"./{args.language}.so")

    if args.language == "c":
        # use single-threaded functions
        python_function = functions.f
        dll_function = dll.f
    else:
        # use two threads
        python_function = functions.f_threads
        dll_function = dll.f_threads

    python_start = time.perf_counter()
    p_result = python_function(n)
    python_end = time.perf_counter()
    print("python:", python_end - python_start)

    dll_start = time.perf_counter()
    # TODO: try https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL
    dll_result = dll_function(n)  # no GIL
    dll_end = time.perf_counter()
    print("dll:", dll_end - dll_start)

    assert p_result == dll_result

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
