# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List

class SeriesDataWrapper(DataWrapper):
    @property
    def data(self):
        return SeriesDataContainer(self.marvel, self.dict['data'])

class SeriesDataContainer(DataContainer):
    @property
    def results(self):
        return self.list_to_instance_list(self.dict['results'], Series)

class Series(MarvelObject):
    """
    Series object
    Takes a dict of character attrs
    """
    _resource_url = 'series'

    @property
    def id(self):
        return self.dict['id']

    @property
    def title(self):
        return self.dict['title']

    @property
    def description(self):
        """
        :returns:  str -- A description of the series.
        """
        return self.dict['description']

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def urls(self):
        return self.dict['urls']

    @property
    def startYear(self):
        return int(self.dict['startYear'])
    
    @property
    def endYear(self):
        return int(self.dict['endYear'])

    @property
    def rating(self):
        return self.dict['rating']

    @property
    def modified(self):
        return str_to_datetime(self.dict['modified'])

    @property
    def modified_raw(self):
        return self.dict['modified']

    @property
    def thumbnail(self):
        return Image(self.marvel, self.dict['thumbnail'])


    @property
    def comics(self):
        from .comic import ComicList
        return ComicList(self.marvel, self.dict['comics'])

    @property
    def stories(self):
        from .story import StoryList
        return StoryList(self.marvel, self.dict['stories'])

    @property
    def events(self):
        from .event import EventList
        return EventList(self.marvel, self.dict['events'])

    @property
    def characters(self):
        from .character import CharacterList
        return CharacterList(self.marvel, self.dict['characters'])

    @property
    def creators(self):
        from .creator import CreatorList
        return CreatorList(self.marvel, self.dict['creators'])

    @property
    def next(self):
        return SeriesSummary(self.marvel, self.dict['next'])

    @property
    def previous(self):
        return SeriesSummary(self.marvel, self.dict['previous'])
        
    def get_creators(self, *args, **kwargs):
        """
        Returns a full CreatorDataWrapper object for this series.

        /series/{seriesId}/creators

        :returns:  CreatorDataWrapper -- A new request to API. Contains full results set.
        """
        from .creator import Creator, CreatorDataWrapper
        return self.get_related_resource(Creator, CreatorDataWrapper, args, kwargs)

    def get_characters(self, *args, **kwargs):
        """
        Returns a full CharacterDataWrapper object for this series.

        /series/{seriesId}/characters

        :returns:  CreatorDataWrapper -- A new request to API. Contains full results set.
        """
        from .character import Character, CharacterDataWrapper
        return self.get_related_resource(Character, CharacterDataWrapper, args, kwargs)

    def get_comics(self, *args, **kwargs):
        """
        Returns a full ComicDataWrapper object for this series.

        /series/{seriesId}/comics

        :returns:  ComicDataWrapper -- A new request to API. Contains full results set.
        """
        from .comic import Comic, ComicDataWrapper        
        return self.get_related_resource(Comic, ComicDataWrapper, args, kwargs)

    def get_events(self, *args, **kwargs):
        """
        Returns a full EventDataWrapper object for this series.

        /series/{seriesId}/events

        :returns:  EventDataWrapper -- A new request to API. Contains full results set.
        """
        from .event import Event, EventDataWrapper
        return self.get_related_resource(Event, EventDataWrapper, args, kwargs)
        
    def get_stories(self, *args, **kwargs):
        """
        Returns a full StoryDataWrapper object for this series.

        /series/{seriesId}/stories

        :returns:  StoriesDataWrapper -- A new request to API. Contains full results set.
        """
        from .story import Story, StoryDataWrapper
        return self.get_related_resource(Story, StoryDataWrapper, args, kwargs)


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
