# -*- coding: utf-8 -*-

from . import _utils


class Fibonacci(_utils.AbstractSeries):
    def _series_generator(self):
            a, b = 0, 1
            while True:
                a, b = b, a + b
                yield b