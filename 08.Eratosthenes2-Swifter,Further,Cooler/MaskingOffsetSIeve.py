#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 12 March, 2018

Program description: uses a generator to perform an offset odd sieve on a small 
range of integers below a user-specified upper limit. 

@author: matta_idlecoder@protonmail.com
"""
import timeit
import datetime
import numpy as np

timing_it = True
listing_primes = True

def init_prime_array(maximum):
    """Returns a small Boolean numpy array, initialised for eliminating primes
    """
    max_array_length = 1000  
    maximum += 1 if (maximum % 2 == 1) else 0  
    num_arrays = int(maximum / max_array_length)

    LastArray = np.ones(max_array_length, dtype=bool)
    LastArray[0::2] = False

    print("The last {:,d} numbers were checked from \n{:,} to {:,}.".
          format(max_array_length, max_array_length*(num_arrays - 1),
                 max_array_length*num_arrays - 1))

    return LastArray, num_arrays


def iprimes_upto(limit):
    """Offset sieve of Eratosthenes, using a Generator.

    Checks all the odds, not only prime multiples, but only in a small window
    below the maximum, usually set to 1000 wide.
    """
    is_prime, number_arrays = init_prime_array(limit)
    array_length = len(is_prime)
    root_limit = int(limit ** 0.5 + 1.5)
    n = 3

    prime_window_index = number_arrays - 1
    window_start = prime_window_index * array_length
    while n < root_limit:
        # This mapping finds the first index to eliminate in an offset array.
        # It doesn't matter if the first 10**15 arrays beneath it have not been
        # masked - or even created:
        n2 = n * 2
        rem_2n = window_start % n2
        rem_2n += n if (rem_2n <= n) else -n
        start_index = n2 - rem_2n
        is_prime[start_index:: n2] = False
        n += 2
    
    # Generator:
    for m in range(array_length):
        if is_prime[m]:
            n = window_start + m
            yield (n)
    
    return

#==============================  MAIN   ===================================

upper_limit = 1001
prime_question = "\nEnter a number >= 10,000 that is divisible by 1,000 that \n"
prime_question += "you want to find the nearest primes to:   "

while upper_limit < 10**4 or upper_limit % 1000 != 0:
    upper_limit = int(input(prime_question))
    if upper_limit % 1000 != 0:
        print("Enter a number divisible by 1,000.")
    if upper_limit < 10**4:
        print("Try using a bigger number.")
            
print("\nSearching for the nearest primes to {:,}...\n".format(upper_limit))

if timing_it:
    print('Starting the search at',
              datetime.datetime.now().strftime("%H:%M:%S"), "\n")
    start_time = timeit.default_timer()

prime_set = list(iprimes_upto(upper_limit))

if not prime_set:
    print ("There were no primes found in the last 1,000 numbers below {:,}".
            format(upper_limit))

elif listing_primes:
    print ("\nThe last 20 primes are:\n")
    for prime1, prime2 in zip(prime_set[-20::][::2], prime_set[-20::][1::2]):
        print ("{:<35,}{:<,}".format(prime1, prime2))
else:
    prime_max = max(prime_set)
    print("The biggest prime found was {:,d}".format(prime_max))

if timing_it:
    prime_time = timeit.default_timer() - start_time
    days, hours = divmod(prime_time, 86400)
    hours, mins = divmod(hours, 3600)
    mins, secs = divmod(mins, 60)
    print(
        '\nCompleted the search in {:,} days {:,} hours {:,} mins {:0,.1f} seconds.'.format(
            int(days), int(hours), int(mins), secs))
            
            
            