# -*- coding: utf-8 -*-
from series import _utils

from itertools import count
import math


class Primes(_utils.AbstractSeries):
    """
    >>> p = Primes()
    >>> p.get_series_elements_less_than(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    def _series_generator(self):
        primes = []
        for candidate in count(2):
            cand_sqrt = math.sqrt(candidate)
            isprime = True
            for p in primes:
                if p <= cand_sqrt and candidate % p == 0:
                    isprime = False
                    break
            if isprime:
                primes.append(candidate)
                yield candidate