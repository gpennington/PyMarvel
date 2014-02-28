# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List


class SeriesList(List):
    """
    SeriesList object
    """

    @property
    def items(self):
        """
        Returns List of SeriesSummary objects
        """
        return self.list_to_instance_list(self.dict['items'], SeriesSummary)

class SeriesSummary(Summary):
    """
    SeriesSummary object
    """

    @property
    def type(self):
        return self.dict['type']