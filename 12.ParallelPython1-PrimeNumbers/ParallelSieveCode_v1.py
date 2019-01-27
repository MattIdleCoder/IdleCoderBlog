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


def init_prime_array(maximum, prime_window_size):
    """Returns list of Boolean numpy arrays, initialised for eliminating primes
 
    Creates a small numpy array, just under the maximum.
    """
    maximum += 1 if (maximum % 2) else 0  # make maximum even
    LastArray = np.ones(prime_window_size, dtype=bool)
    LastArray[0::2] = False
    win_start = maximum - prime_window_size
    return LastArray, win_start


def del_non_primes(sieved_array, root_limit, array_start):
    """Mask out non-primes from the numbers in the array
    """
    for n in range(3, root_limit, 2):
        n2 = n * 2
        rem_2n = array_start %  n2
        rem_2n += n if (rem_2n <= n) else -n
        start_index = n2 - rem_2n
        sieved_array[start_index : : n2] = False
    # Note how the function returns the value represented by
    # array_slice[0] as a marker for which array it is. This is
    # needed to sort the results as them come back:
    return array_start, sieved_array


def primes_in_window_below(limit, prime_window_size=1000):
    """An offset odd sieve for finding primes, using a Generator
    """
    # creates a blank boolean array with all the evens preset to False:
    is_prime, window_start = init_prime_array(limit, prime_window_size)
    root_limit = int(limit ** 0.5 + 1.5)
 
    # prep to slice up the problem into the the number of cores you want to use.
    AVAIL_CORES = 1  # os.cpu_count()  # Typically pseudo-4 on many laptops
    stride = int(prime_window_size / AVAIL_CORES)
 
    # This code creates a mask of slice_pts, eg for 4 CPUs and a list 20 long,
    # it would create slice_pts of  [(0, 5), (5, 10), (10, 15), (15, 20)]:
    slices = list(zip(range(0, prime_window_size - stride + 1, stride),
                      range(stride, prime_window_size + 1, stride)))
 
    # Use the mask to slice up the Numpy array into the number of cores:
    is_prime_slices = [is_prime[slice_pt[0]: slice_pt[1]] for slice_pt in slices]
 
    # parallel bit:
    this_array_start, numbered_results = window_start, []
    with futures.ProcessPoolExecutor(AVAIL_CORES) as executor:
        result = (executor.submit(del_non_primes, array_slice, root_limit, 
                    this_array_start + (slice_num * stride)) 
                    for slice_num, array_slice in enumerate(is_prime_slices))
        for future in futures.as_completed(result):
            res = future.result()
            numbered_results.append(res)
 
    # Create an array for the results:
    is_prime_arrays = np.zeros([AVAIL_CORES, stride], dtype=bool)
    # sort the results into order by first item (= this_array_start):
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

