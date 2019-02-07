# -*- coding: utf-8 -*-
 
import numpy as np
 
def primes_in_window_below(long limit, int window_size=1000):
    cdef long window_start, root_limit, n, n2, rem_2n, start_index
    cdef Py_ssize_t m
 
    is_prime = np.ones(window_size, dtype=np.uint16)
    is_prime[0::2] = False
 
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

