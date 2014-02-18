# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List


class EventList(List):
    """
    EventList object
    """

    @property
    def items(self):
        """
        Returns List of EventSummary objects
        """
        return self.list_to_instance_list(self.dict['items'], EventSummary)

class EventSummary(Summary):
    """
    EventSummary object
    """
    