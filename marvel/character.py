# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

import json

from .core import MarvelObject
from .comic import Comic

class Character(MarvelObject):
    """
    Character object
    Takes a dict of character attrs
    """
    _resource_url = 'characters'


    @property
    def id(self):
        return self.dict['id']

    @property
    def name(self):
        return self.dict['name']

    @property
    def description(self):
        return self.dict['description']

    @property
    def comics(self):
        
        comics = self.dict['comics']
        print comics
        #Maybe ComicSummary?
        #Maybe ComicsList?
        return comics
        
    def get_comics(self):
        """
        Returns list of Comic objects
        """
        response = json.loads(self.marvel._call("%s/%s/%s" % (self._resource_url, self.id, Comic.resource_url())).text)
        comics = []
        for comic in response['data']['results']:
            comics.append(Comic(self.marvel, comic))
        return comics