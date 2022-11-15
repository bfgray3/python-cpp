#!/usr/bin/env python
import ctypes
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    print(ctypes.CDLL("./sharedlibrary.so").f(2**31 - 1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
