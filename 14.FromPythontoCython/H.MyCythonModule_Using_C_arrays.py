# -*- coding: utf-8 -*-
 
DEF WIN_SIZE = 1000
 
def primes_in_window_below(long limit):
 
    cdef long window_start, root_limit, n, n2, start_index, rem_2n
    cdef Py_ssize_t counter1, counter2, m
    cdef bint is_prime[WIN_SIZE]
 
    counter1 = 0
    while counter1 < WIN_SIZE:
        is_prime[counter1] = 0
        is_prime[counter1 + 1] = 1
        counter1 += 2
 
    window_start = limit - WIN_SIZE    
    root_limit = int(limit ** 0.5 + 1.5)
 
    for n in range(3, root_limit, 2):
        n2 = n * 2
        rem_2n = window_start % n2
        rem_2n += n if (rem_2n <= n) else -n
        start_index = n2 - rem_2n
 
        counter2 = start_index
        while counter2 < WIN_SIZE:
            is_prime[counter2] = 0
            counter2 += n2
 
# Generator:
    for m in range(1, WIN_SIZE, 2):
        if is_prime[m]:
            n = window_start + m
            yield (n)
 
    return

