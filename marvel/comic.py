# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer

class ComicDataWrapper(DataWrapper):
    @property
    def data(self):
        return ComicDataContainer(self.marvel, self.dict['data'])

class ComicDataContainer(DataContainer):
    @property
    def results(self):
        comics = []
        for comic in self.dict['results']:
            comics.append(Comic(self.marvel, comic))
        return comics

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

class ComicList(MarvelObject):
    """
    ComicList object
    """

    @property
    def available(self):
        return self.dict['available']

    @property
    def returned(self):
        return self.dict['returned']

    @property
    def collectionURI(self):
        return self.dict['collectionURI']

    @property
    def items(self):
        """
        Returns List of ComicSummary objects
        """
        items = []
        for index, item in enumerate(self.dict['items']):
            items.append(ComicSummary(self.marvel, self.dict['items'][index]))
        return items

class ComicSummary(MarvelObject):
    """
    CommicSummary object
    """

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def name(self):
        return self.dict['name']
