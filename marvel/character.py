# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

import json
from datetime import datetime

from .core import MarvelObject, DataWrapper, DataContainer
from .comic import Comic, ComicList

class CharacterDataWrapper(DataWrapper):
    @property
    def data(self):
        return CharacterDataContainer(self.marvel, self.dict['data'])

class CharacterDataContainer(DataContainer):
    @property
    def results(self):
        characters = []
        for character in self.dict['results']:
            characters.append(Character(self.marvel, character))
            
        return characters


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
    def modified(self):
        """ Converts '2013-11-20T17:40:18-0500' to 'datetime' object """
        #Hacked off %z timezone because reasons
        return datetime.strptime(self.dict['modified'][:-6], '%Y-%m-%dT%H:%M:%S')

    @property
    def modified_raw(self):
        return self.dict['modified']

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def urls(self):
        return self.dict['urls']

    @property
    def wiki(self):
        for item in self.dict['urls']:
            if item['type'] == 'wiki':
                return item['url']
        return None

    @property
    def detail(self):
        for item in self.dict['urls']:
            if item['type'] == 'detail':
                return item['url']
        return None

    @property
    def thumbnail(self):
        return "%s.%s" % (self.dict['thumbnail']['path'], self.dict['thumbnail']['extension'] )


    """
    comics (ComicList, optional): A resource list containing comics which feature this character.,
    stories (StoryList, optional): A resource list of stories in which this character appears.,
    events (EventList, optional): A resource list of events in which this character appears.,
    series (SeriesList, optional): A resource list of series in which this character appears.
    """

    @property
    def comics(self):
        """
        Returns ComicList object
        """
        return ComicList(self.marvel, self.dict['comics'])
        
        
        
    def get_comics(self):
        """
        Returns list of Comic objects
        """
        response = json.loads(self.marvel._call("%s/%s/%s" % (self._resource_url, self.id, Comic.resource_url())).text)
        comics = []
        for comic in response['data']['results']:
            comics.append(Comic(self.marvel, comic))
        return comics