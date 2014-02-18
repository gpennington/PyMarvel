# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

import json

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List

class CreatorDataWrapper(DataWrapper):
    @property
    def data(self):
        return CreatorDataContainer(self.marvel, self.dict['data'])

    """
    def next(self):

        Returns new CreatorDataWrapper
        TODO: Don't raise offset past count - limit

        self.params['offset'] = str(int(self.params['offset']) + int(self.params['limit']))
        return self.marvel.get_characters(self.marvel, (), **self.params)

    def previous(self):

        Returns new CreatorDataWrapper
        TODO: Don't lower offset below 0

        self.params['offset'] = str(int(self.params['offset']) - int(self.params['limit']))
        return self.marvel.get_characters(self.marvel, (), **self.params)
    """

class CreatorDataContainer(DataContainer):
    @property
    def results(self):
        return self.list_to_instance_list(self.dict['results'], Creator)


class Creator(MarvelObject):
    """
    Creator object
    Takes a dict of creator attrs
    """
    _resource_url = 'creators'


    @property
    def id(self):
        return int(self.dict['id'])

    @property
    def firstName(self):
        return self.dict['firstName']

    @property
    def middleName(self):
        return self.dict['middleName']

    @property
    def lastName(self):
        return self.dict['lastName']

    @property
    def suffix(self):
        return self.dict['suffix']

    @property
    def fullName(self):
        return self.dict['fullName']


    @property
    def modified(self):
        return str_to_datetime(self.dict['modified'])

    @property
    def modified_raw(self):
        return self.dict['modified']

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def urls(self):
        return self.dict['urls']

    """
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
    """

    @property
    def thumbnail(self):
        return "%s.%s" % (self.dict['thumbnail']['path'], self.dict['thumbnail']['extension'] )

    @property
    def series(self):
        from .series import SeriesList
        return SeriesList(self.marvel, self.dict['series'])

    @property
    def stories(self):
        from .story import StoryList
        return StoryList(self.marvel, self.dict['stories'])

    @property
    def comics(self):
        from .comic import ComicList
        """
        Returns ComicList object
        """
        return ComicList(self.marvel, self.dict['comics'])

    @property
    def events(self):
        from .event import EventList
        return EventList(self.marvel, self.dict['events'])
        

        
    def get_comics(self, *args, **kwargs):
        """
        Returns a full ComicDataWrapper object this character.
        
        /characters/{characterId}/comics
        
        :returns:  ComicDataWrapper -- A new request to API. Contains full results set.
        """
        url = "%s/%s/%s" % (Creator.resource_url(), self.id, Comic.resource_url())
        response = json.loads(self.marvel._call(url, self.marvel._params(kwargs)).text)
        return ComicDataWrapper(self, response)


class CreatorList(List):
    """
    CreatorList object
    """

    @property
    def items(self):
        """
        Returns List of CreatorSummary objects
        """
        return self.list_to_instance_list(self.dict['items'], CreatorSummary)

class CreatorSummary(Summary):
    """
    CreatorSummary object
    """
        
    @property
    def role(self):
        return self.dict['role']