# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, Summary, List

class EventDataWrapper(DataWrapper):
    @property
    def data(self):
        return EventDataContainer(self.marvel, self.dict['data'])

class EventDataContainer(DataContainer):
    @property
    def results(self):
        return self.list_to_instance_list(self.dict['results'], Event)

class Event(MarvelObject):
    """
    Event object
    Takes a dict of character attrs
    """
    _resource_url = 'events'


    @property
    def id(self):
        return self.dict['id']

    @property
    def title(self):
        return self.dict['title']

    @property
    def description(self):
        """
        :returns:  str -- The preferred description of the comic.
        """
        return self.dict['description']

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def urls(self):
        return self.dict['urls']

    @property
    def modified(self):
        return str_to_datetime(self.dict['modified'])

    @property
    def modified_raw(self):
        return self.dict['modified']

    @property
    def start(self):
        return str_to_datetime(self.dict['start'])

    @property
    def start_raw(self):
        return self.dict['start']

    @property
    def end(self):
        return str_to_datetime(self.dict['end'])

    @property
    def end_raw(self):
        return self.dict['end']

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
    def series(self):
        """
        Returns SeriesList object
        """
        from .series import SeriesList
        return SeriesList(self.marvel, self.dict['series'])

    @property
    def characters(self):
        from .character import CharacterList
        return CharacterList(self.marvel, self.dict['characters'])

    @property
    def creators(self):
        from .creator import CreatorList
        return CreatorList(self.marvel, self.dict['creators'])

    @property
    def series(self):
        from .series import SeriesList
        return SeriesList(self.marvel, self.dict['series'])
        
    @property
    def next(self):
        return EventSummary(self.marvel, self.dict['next'])

    @property
    def previoius(self):
        return EventSummary(self.marvel, self.dict['previous'])


    def get_creators(self, *args, **kwargs):
        """
        Returns a full CreatorDataWrapper object for this event.

        /events/{eventId}/creators

        :returns:  CreatorDataWrapper -- A new request to API. Contains full results set.
        """
        from .creator import Creator, CreatorDataWrapper
        return self.get_related_resource(Creator, CreatorDataWrapper, args, kwargs)

    def get_characters(self, *args, **kwargs):
        """
        Returns a full CharacterDataWrapper object for this event.

        /events/{eventId}/characters

        :returns:  CreatorDataWrapper -- A new request to API. Contains full results set.
        """
        from .character import Character, CharacterDataWrapper
        return self.get_related_resource(Character, CharacterDataWrapper, args, kwargs)

    def get_comics(self, *args, **kwargs):
        """
        Returns a full ComicDataWrapper object for this event.

        /events/{eventId}/comics

        :returns:  ComicDataWrapper -- A new request to API. Contains full results set.
        """
        from .comic import Comic, ComicDataWrapper
        return self.get_related_resource(Comic, ComicDataWrapper, args, kwargs)

    def get_series(self, *args, **kwargs):
        """
        Returns a full SeriesDataWrapper object for this event.

        /events/{eventId}/series

        :returns:  SeriesDataWrapper -- A new request to API. Contains full results set.
        """
        from .series import Series, SeriesDataWrapper
        return self.get_related_resource(Series, SeriesDataWrapper, args, kwargs)
        
    def get_stories(self, *args, **kwargs):
        """
        Returns a full StoryDataWrapper object for this event.

        /events/{eventId}/stories

        :returns:  StoriesDataWrapper -- A new request to API. Contains full results set.
        """
        from .story import Story, StoryDataWrapper
        return self.get_related_resource(Story, StoryDataWrapper, args, kwargs)


"""
    Event {
    id (int, optional): The unique ID of the event resource.,
    title (string, optional): The title of the event.,
    description (string, optional): A description of the event.,
    resourceURI (string, optional): The canonical URL identifier for this resource.,
    urls (Array[Url], optional): A set of public web site URLs for the event.,
    modified (Date, optional): The date the resource was most recently modified.,
    start (Date, optional): The date of publication of the first issue in this event.,
    end (Date, optional): The date of publication of the last issue in this event.,
    thumbnail (Image, optional): The representative image for this event.,
    comics (ComicList, optional): A resource list containing the comics in this event.,
    stories (StoryList, optional): A resource list containing the stories in this event.,
    series (SeriesList, optional): A resource list containing the series in this event.,
    characters (CharacterList, optional): A resource list containing the characters which appear in this event.,
    creators (CreatorList, optional): A resource list containing creators whose work appears in this event.,
    next (EventSummary, optional): A summary representation of the event which follows this event.,
    previous (EventSummary, optional): A summary representation of the event which preceded this event.
    }
"""


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