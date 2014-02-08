# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

import json

from .core import MarvelObject

class Character(MarvelObject):
    """
    Character object
    Takes a dict of character attrs
    """
    _resource_url = 'characters/'

    """
    @property
    def id(self):
        return self.dict['id']

    @property
    def name(self):
        return self.dict['name']
    """