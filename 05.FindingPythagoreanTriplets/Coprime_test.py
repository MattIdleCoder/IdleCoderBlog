#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finds all of Euclid's Pythagorean triplets that result in a prime hyptotenuse,
up to triangles of sides 500 units long. Yields primes up to 500,000.

Created on Sat Sep  9 07:18:09 2017

@author: matta_idlecoder@protonmail.com
"""

from math import sqrt
import sys
import timeit

def is_prime(Number, return_first_factor=False):
    """Returns True if Number is prime, else False

    Its job is not to find all the factors, only to see if a factor exists
    """
    if type(Number) != int:
        print ("Error in function is_prime() - it was passed a non-int.")
        sys.exit(0)

    elif Number < 2:
        print ("Error in function is_prime() - it was passed a number less than 2.")
        sys.exit(0)

    elif (Number == 2) or (Number == 3):
        return (True, Number) if return_first_factor else True

    elif Number % 2 == 0:
        return (False, 2) if return_first_factor else False

    elif Number % 3 == 0:
        return (False, 3) if return_first_factor else False

    # if you're here, Number >= 5, an int, odd, and not a multiple of 3:
    go_no_further = int(round(sqrt(Number), 0))

    for poss_factor in range(3, go_no_further+2, 2):
        if Number % poss_factor == 0:
            # finds first factor of Number, don't care which:
            return (False, poss_factor) if return_first_factor else False

    return (True, 1) if return_first_factor else True


def get_prime_list_to_half(number):
    """returns a set of the primes up the square root of number (if whole)
    """
    prime_list = []
    if number > 2:
        prime_list.append(2)

    for poss_prime in range(3, int(number/2)+1, 2):
        if is_prime(poss_prime):
            prime_list.append(poss_prime)

    return prime_list


def co_prime(x, y, primes):
    """Returns True if x and y share any factors

    Algoirthm is first to check if one is not a factor of the other, then
    to see that they share no factors from the list of primes.
    """
    if x == y:
        print ("Error in function co_prime() - has been passed the same 2 numbers.")
        sys.exit(0)
    elif x % y == 0 or y % x == 0:
        return False

    for prime in primes:
        if (x % prime == 0) and (y % prime == 0):
            return False
    return True



def main():
    """Main function
    """
    Max_N = 500

    prime_list = get_prime_list_to_half(Max_N)

    SumSquares = []
    for i in range (2, Max_N+1, 1):
        for j in range (i, Max_N+1, 1):

            if i == j:
                continue

            if (i % 2 == 1) and (j % 2 == 1):
                # if i and j are both odd:
                continue

            if (i % 2 == 0) and (j % 2 == 0):
                # if i and j are both even:
                continue

            if not co_prime(i, j, prime_list):
                continue

            SumSquares.append([i, j, (i**2 + j**2)])

    SumSquares_copy = SumSquares[:]  
    for sq_set in SumSquares_copy:
        sum_sq = sq_set[2]
        if sum_sq % 5 == 0:
            SumSquares.remove(sq_set)
        elif (sum_sq - int(sqrt(sum_sq))**2) == 0:
            # remove any perfect squares:
            SumSquares.remove(sq_set)

    MaxPrime = 1
    non_prime_count  = 0
    SumSquares_copy = SumSquares[:] 
    for index, sq_set in enumerate(SumSquares_copy):
        if not is_prime(sq_set[2]):
            non_prime_count += 1
            SumSquares[index].append([is_prime(sq_set[2], return_first_factor=True)[1]])
        else:
            MaxPrime = sq_set[2] if sq_set[2] > MaxPrime else MaxPrime

    square_total = len(SumSquares)
    prime_total = square_total - non_prime_count
    print ("\nCounting up to {}, {:,d} out of the {:,d} Euclid's co-prime square-sums are prime, or about {:.0%}.".
           format(Max_N, prime_total, square_total, prime_total/square_total))

    print ("\nThe largest prime found was {:,d}".format(MaxPrime))
    return


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    stop_time = timeit.default_timer()
    prime_time = stop_time - start_time
    print ('\nThat took', round(prime_time, 1), 'seconds.')


