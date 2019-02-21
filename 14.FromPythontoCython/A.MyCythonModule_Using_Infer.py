# -*- coding: utf-8 -*-
# cython: infer_types=True

import numpy as np


def init_prime_array(prime_window_size):
    LastArray = np.ones(prime_window_size, dtype=np.uint16)
    LastArray[0::2] = False
    return LastArray


def primes_in_window_below(limit, window_size=1000):
    is_prime = init_prime_array(window_size)
    window_start = limit - window_size
    root_limit = int(limit ** 0.5 + 1.5)

    for n in range(3, root_limit, 2):
        n2 = n * 2
        rem_2n = window_start % n2
        rem_2n += n if (rem_2n <= n) else -n
        start_index = n2 - rem_2n
        is_prime[start_index : : n2] = False

# Generator:
    for m in range(1, window_size, 2):
        try:
            if is_prime[m]:
                n = window_start + m
                yield (n)
        except IndexError:
            break
    return
