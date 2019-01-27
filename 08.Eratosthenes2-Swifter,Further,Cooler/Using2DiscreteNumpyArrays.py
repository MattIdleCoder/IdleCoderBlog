#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 10 March, 2018

Program description: uses a generator to create a pseudo-sieve of Eratosthenes
up to an upper limit, bypassing the memory limit on the maximum list size by
splitting the upper limit into manageable arrays, and timing the results.

@author: matta_idlecoder@protonmail.com

This version:
- uses 2 unrelated numpy arrays to extend size of max primes that can be found.
-
"""

import timeit
import datetime
import sys
import numpy as np

timing_it = True
listing_primes = True

def init_prime_arrays(maximum):
    """Returns 1 or 2 discrete Boolean numpy arrays, initialised for odd primes

    If it creates 2 massive numpy arrays, they are unconnected. 
    """
    init_max_array_length = 10**10
    maximum += 1 if (maximum % 2 == 1) else 0  # make maximum even

    num_arrays = 1
    if init_max_array_length * num_arrays < maximum:
        num_arrays *= 2
    each_array_length = int(maximum / num_arrays)

    if each_array_length > 10**10:
        print("\nYour number is too large for this version of the program.")
        print("Enter a number <= {:,}\n".format(10**9))
        sys.exit(2)

    array_0 = np.ones(each_array_length, dtype=bool)
    array_0[::2] = False
    array_0[1:3]  = False, True
    last_value = array_0[-1]

    if num_arrays == 2:
        array_1 = np.ones(each_array_length, dtype=bool)
        first_false = 0 if last_value else 1
        array_1[first_false::2] = False
    else:
        array_1 = []

    print("Initial array length tried was {:,d}".format(init_max_array_length))
    print("Actual array length used was {:,d}".format(each_array_length))
    print("The number of arrays used to make the limit manageable was "
          "{:,d}".format(num_arrays))

    return (array_0, array_1, num_arrays)


def iprimes_upto(limit):
    """Pseudo sieve of Eratosthenes, using a Generator

    Attempts to use two unrelated numpy arrays to reach bigger primes faster.
    """
    is_prime_0, is_prime_1, number_arrays = init_prime_arrays(limit)
    array_length = len(is_prime_0)
    root_limit = int(limit ** 0.5 + 1.5)
    n = 3

# Sieve of Eratosthenes, using binary masking across TWO numpy arrays.
# Avoids use of for-loops:
    array_index = 0
    while array_index < number_arrays:
        while n < root_limit:
            n2 = n * 2
            if array_index == 0:        # first loop of array and this n
                if not is_prime_0[n]:  # skip to next odd n if already False
                    n += 2
                    continue  
                # trick here is to make the array size large enough so that
                # √limit always lies within the first array. This is checked in
                # init_prime_arrays() above:
                is_prime_0[n :: n2] = False
                is_prime_0[n] = True

            elif array_index == 1:
                # Finds the indices in the second array:
                rem_2n = (array_index * array_length) % n2
                rem_2n += n if (rem_2n <= n) else -n
                start_index = n2 - rem_2n
                is_prime_1[start_index:: n2] = False
            n += 2
        array_index += 1
        n = 3 # reset for second array

# Generator:
    first_index = array_length - 1000
    last_array = is_prime_0 if number_arrays == 1 else is_prime_1

    for m in range(first_index, array_length):
        if last_array[m]:
            n = ((number_arrays - 1) * array_length) + m
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
    print ("There were no primes found in the last 1,000 numbers below {:,}".format(upper_limit))

elif listing_primes:
    print ("\nThe last 20 primes are:\n")
    for prime1, prime2 in zip(prime_set[-20::][::2], prime_set[-20::][1::2]):
        print ("{:<40,}{:<,}".format(prime1, prime2))
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