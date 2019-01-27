#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 4 March, 2018
 
Program description: runs a sieve of Eratosthenes up to an upper limit using
numpy slicing, timing the results.
 
@author: matta_idlecoder@protonmail.com
 
"""
import timeit
import numpy as np
 
timing_it = True
 
def iprimes_upto(limit):
    """Improvements to Eratosthenes Sieve using numpy masking
    """
 
    is_prime = np.array(([False, False, True, True] + [False, True] *
                         int((limit - 2)/2)), dtype=bool)
    is_prime = is_prime[:limit+1]
 
    root_limit = int(limit ** 0.5) + 1
    for n in range(3, root_limit, 2):
        if is_prime[n]:
            is_prime[n*n : limit+1 : 2*n] = False
 
    lower_limit = limit - 201 if limit % 2 == 0 else limit - 200
    for i in range(lower_limit, limit + 1, 2):
        if is_prime[i]:
            yield i
 
    return
 
#==============================  MAIN   ===================================
 
upper_limit = int(input('\nEnter the number you want to find all the primes up to: '))
print("\nSearching for primes up to {:,d}...".format(upper_limit))
 
if timing_it:
    start_time = timeit.default_timer()
 
prime_set = list(iprimes_upto(upper_limit))
 
print ("Number of primes is {:,d}".format(len(prime_set)))
print ("Last prime is {:,d}".format(prime_set[-1]))
 
if timing_it:
    prime_time = timeit.default_timer() - start_time
    hours, mins = divmod(prime_time, 3600)
    mins, secs = divmod(mins, 60)
    print('\nCompleted the search in {:,} hours {:,} mins {:0,.1f} seconds.'.
            format(int(hours), int(mins), secs))

