import threading


def f(n: int) -> int:
    i = 0
    for _ in range(n):
        i += 1
    return i


def f_threads(n: int) -> int:
    t1 = threading.Thread(target=f, args=(n,))
    t2 = threading.Thread(target=f, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return 0
