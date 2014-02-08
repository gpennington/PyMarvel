# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject

class Comic(MarvelObject):
    """
    Comic object
    Takes a dict of character attrs
    """
    _resource_url = 'comics'


    @property
    def id(self):
        return self.dict['id']

    @property
    def title(self):
        return self.dict['title']

    @property
    def description(self):
        return self.dict['description']
