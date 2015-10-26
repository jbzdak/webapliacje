# -*- coding: utf-8 -*-


def _fib_generator():
    a, b = 0, 1
    while True: 
        a, b = b, a + b
        yield b


def fib(n):
    """
    Zwraca N-tą liczbę Fibonacciego
    """
    r = 0
    for ii, r in zip(range(n), _fib_generator()):
        pass
    return r


def fib2(n): # return Fibonacci series up to n
    result = []
    r = 0
    for r in _fib_generator():        
        if r > n: 
            return result
        result.append(r)