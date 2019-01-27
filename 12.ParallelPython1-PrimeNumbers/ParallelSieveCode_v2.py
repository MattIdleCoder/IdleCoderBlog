#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program description: runs an ofset odd sieve inside a small, 1000-wide window of 
numbers just below a large, user-defined limit. Uses a binary Numpy array for 
the integer window and uses parallel processing to mask slices of the array on 
different cores.

Created 20 Nov, 2018
@author: matta_idlecoder@protonmail.com
"""
import timeit
import datetime
import numpy as np
from concurrent import futures

timing_it = True
listing_primes = True


def init_prime_array(prime_window_size):
    """Returns a Boolean numpy array, initialised with evens eliminated
    """
    LastArray = np.ones(prime_window_size, dtype=bool)
    LastArray[0::2] = False
    return LastArray


def del_non_primes(CPU_index, num_cores, window_size, limit):
    """Initialize the prime array slice and mask out non-primes
 
    The array initialization lines have been moved here, so that only variables
    are passed from the futures.ProcessPoolExecutor, rather than refs to
    different sections of the same list
    """
    array_start = limit - window_size + CPU_index * int(window_size / num_cores)
    is_prime = init_prime_array(int(window_size/num_cores))
    root_limit = int(limit ** 0.5 + 1.5)
 
    for n in range(3, root_limit, 2):
        n2 = n * 2
        rem_2n = array_start % n2
        rem_2n += n if (rem_2n <= n) else -n
        start_index = n2 - rem_2n
        is_prime[start_index : : n2] = False
 
    return array_start, is_prime
 
 
def primes_in_window_below(limit, prime_window_size=1000):
    """Pseudo-sieve of Eratosthenes, using a Generator
 
    """
    #AVAIL_CORES = os.cpu_count()
    AVAIL_CORES = 2  # os.cpu_count()  # Typically pseudo-4 on many laptops
    stride = int(prime_window_size / AVAIL_CORES)
    window_start = limit - prime_window_size
 
    numbered_results = []
    with futures.ProcessPoolExecutor(AVAIL_CORES) as executor:
        result = (executor.submit(del_non_primes, core_index, AVAIL_CORES,
                  prime_window_size, limit) for core_index in range(AVAIL_CORES))
        for future in futures.as_completed(result):
            res = future.result()
            numbered_results.append(res)
 
    is_prime_arrays = np.zeros([AVAIL_CORES, stride], dtype=bool)
    numbered_results = sorted(numbered_results)
    for index, result in enumerate(numbered_results):
        is_prime_arrays[index] = result[1]
 
    # Generator: calculate each prime from its array position:
    for core_result in range(AVAIL_CORES):
        for array_index in range(1, stride, 2):
            try:
                if is_prime_arrays[core_result][array_index]:
                    n = window_start + (core_result * stride) + array_index
                    yield (n)
            except IndexError:
                break
    return


def main():
    PRIME_WINDOW_SIZE = 1000
    upper_limit = 1

    question = "\nNear what power of 10 do you want to find the primes?\n"
    question += "Note: it will take about 3 times longer for each additional\n"
    question += "power of 10. Enter an integer greater than 6: "

    while upper_limit < 10**6:
        try:
            ten_power = int(input(question))
            upper_limit = 10**ten_power
        except ValueError:
            upper_limit = 1

    print("Searching for the primes in the last {:,} numbers up to {:.1e}...".
          format(PRIME_WINDOW_SIZE, upper_limit))
    if timing_it:
        print("Starting the search at",
              datetime.datetime.now().strftime("%H:%M:%S"))
        start_time = timeit.default_timer()

    prime_set = list(primes_in_window_below(upper_limit,
                                        prime_window_size=PRIME_WINDOW_SIZE))
    if not prime_set:
        print ("There were no primes found in the last 1,000 numbers below {:,}".
                format(upper_limit))

    elif listing_primes:
        print ("\nThe last 20 primes are:\n")
        for prime1, prime2 in zip(prime_set[-20::][::2], prime_set[-20::][1::2]):
            print ("{:<35,}{:<,}".format(prime1, prime2))
    else:
        prime_max = max(prime_set)
        print("The largest prime found was {:,d}".format(prime_max))

    if timing_it:
        prime_time = timeit.default_timer() - start_time
        days, hours = divmod(prime_time, 86400)
        hours, mins = divmod(hours, 3600)
        mins, secs = divmod(mins, 60)
        print(
            '\nCompleted the search in {:,} days {:,} hours {:,} mins {:0,.1f} seconds.'.format(
                int(days), int(hours), int(mins), secs))
    return

             
if __name__ == '__main__':
    main()

