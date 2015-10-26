# -*- coding: utf-8 -*-


class AbstractSeries(object):

    def _series_generator(self):
        pass

    def get_series_element(self, N):
        assert N > 0
        for ii, element in zip(range(N), self._series_generator()):
            pass
        return element

    def get_series_elements_less_than(self, x):
        result = []

        for elem in self._series_generator():
            if elem > x:
                break
            result.append(elem)

        return result

    def get_n_series_elements(self, N):
        result = []

        for ii, element in zip(range(N), self._series_generator()):
            result.append(element)

        return result
