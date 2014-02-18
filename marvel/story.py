# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List


class StoryList(List):
    """
    StoryList object
    """

    @property
    def items(self):
        """
        Returns List of StorySummary objects
        """
        return self.list_to_instance_list(self.dict['items'], StorySummary)

class StorySummary(Summary):
    """
    StorySummary object
    """

    @property
    def type(self):
        return self.dict['type']