# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List

class CreatorList(List):
    """
    CreatorList object
    """

    @property
    def items(self):
        """
        Returns List of CharacterSummary objects
        """
        return self.list_to_instance_list(self.dict['items'], CreatorSummary)

class CreatorSummary(Summary):
    """
    CreatorSummary object
    """
        
    @property
    def role(self):
        return self.dict['role']