#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 8 March, 2018
 
Program description: uses a generator to create a sieve of Eratosthenes up to
an upper limit, attempting to bypass the hardware limit on the maximum list
size by splitting the upper limit into manageable lists, and timing the results.
 
@author: matta_idlecoder@protonmail.com
"""
import timeit
import numpy as np
import datetime
 
listing_primes = True
timing_it = True
 
def init_prime_arrays(maximum):
    """Returns list of Boolean numpy arrays, initialised for eliminating primes
 
    Value at each index reflects whether the index is prime or not
    Values 0.. are correct, with all higher evens eliminated
    """
 
    list_of_arrays = []
    init_max_array_length = 5*10**6   
    maximum += 1 if (maximum % 2 == 1) else 0  # make maximum even
 
    num_arrays = 1
    while init_max_array_length * num_arrays < maximum:
        num_arrays *= 2
 
    each_array_length = int(maximum / num_arrays)
 
    first_array = np.ones(each_array_length, dtype=bool)
    first_array[4::2] = False  # set every second item to False, starting from 4
    list_of_arrays.append(first_array)
 
    distance_covered = each_array_length - 1 # value of last index, not the length
    last_value = first_array[-1]
 
    while distance_covered < maximum - 1:
        new_array = np.ones(each_array_length, dtype=bool)
        first_false = 0 if last_value else 1
        new_array[first_false::2] = False
        last_value = new_array[-1]
        list_of_arrays.append(new_array)
        distance_covered += each_array_length
 
    list_of_arrays[0][0], list_of_arrays[0][1]  = False, False
 
    print("Initial array length tried was {:,d}".format(init_max_array_length))
    print("Actual array length used was {:,d}".format(each_array_length))
    print("The number of arrays used to make the limit manageable was "
          "{:,d}".format(len(list_of_arrays)))
    return list_of_arrays
 
 
def iprimes_upto(limit):
    """Sieve of Eratosthenes using a list of arrays and a Generator
    """
    is_prime = init_prime_arrays(limit)
    number_arrays = len(is_prime)
    array_length = len(is_prime[0])
 
    # Sieve of Eratosthenes, nested into a list of np arrays.
    # Even numbers were eliminated when the boolean arrays were set up:
    for n in range(3, int(limit ** 0.5 + 1.5), 2):
        array_num, index = divmod(n, array_length)
        if is_prime[array_num][index]:
            for i in range(n * n, limit + 1, n * 2):
                array_num, index = divmod(i, array_length)
                is_prime[array_num][index] = False

    # Generator:
    last_array_length = len(is_prime[-1])
    prime_check_index = last_array_length - 1000
 
    # New in this version - don't bother to find the primes in the earlier 
    # arrays. Just check all the numbers in the prime check window: 
    for m in range(prime_check_index, last_array_length):
        if is_prime[-1][m]:
            n = (number_arrays - 1) * array_length + m
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

    
