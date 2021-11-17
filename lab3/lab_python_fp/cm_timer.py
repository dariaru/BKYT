from contextlib import contextmanager
import time

@contextmanager
def cm_timer_1():
    start = time.time()
    yield
    print("Время работы блока кода: {} секунд".format(time.time() - start))


class cm_timer_2:

    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, ecx_type, exc_value, traceback):
        print("Время работы блока кода: {} секунд".format(time.time() - self.start))


with cm_timer_1():
    time.sleep(3)
with cm_timer_2():
    time.sleep(3)