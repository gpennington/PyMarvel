# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

import urllib
import json
import hashlib
import datetime

import requests

from .character import Character, CharacterDataWrapper
from .comic import ComicDataWrapper, Comic
from .creator import CreatorDataWrapper, Creator
from .event import EventDataWrapper, Event
from .series import SeriesDataWrapper, Series
from .story import StoryDataWrapper, Story

DEFAULT_API_VERSION = 'v1'

class Marvel(object):
    """Marvel API class

    This class provides methods to interface with the Marvel API

    >>> m = Marvel("acb123....", "efg456...")

    """

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        
    def _endpoint(self):
        return "http://gateway.marvel.com/%s/public/" % (DEFAULT_API_VERSION)

    def _call(self, resource_url, params=None):
        """
        Calls the Marvel API endpoint

        :param resource_url: url slug of the resource
        :type resource_url: str
        :param params: query params to add to endpoint
        :type params: str
        
        :returns:  response -- Requests response
        """
        
        url = "%s%s" % (self._endpoint(), resource_url)
        if params:
            url += "?%s&%s" % (params, self._auth())
        else:
            url += "?%s" % self._auth()
        return requests.get(url)

    def _params(self, params):
        """
        Takes dictionary of parameters and returns
        urlencoded string

        :param params: Dict of query params to encode
        :type params: dict
        
        :returns:  str -- URL encoded query parameters
        """
        return urllib.urlencode(params)

    def _auth(self):
        """
        Creates hash from api keys and returns all required parametsrs
        
        :returns:  str -- URL encoded query parameters containing "ts", "apikey", and "hash"
        """
        ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        hash_string = hashlib.md5("%s%s%s" % (ts, self.private_key, self.public_key)).hexdigest()
        return "ts=%s&apikey=%s&hash=%s" % (ts, self.public_key, hash_string)





    #public methods
    def get_character(self, id):
        """Fetches a single character by id.

        get /v1/public/characters

        :param id: ID of Character
        :type params: int
        
        :returns:  CharacterDataWrapper

        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_character(1009718)
        >>> print cdw.data.count
        1
        >>> print cdw.data.results[0].name
        Wolverine

        """
        url = "%s/%s" % (Character.resource_url(), id)
        response = json.loads(self._call(url).text)
        return CharacterDataWrapper(self, response)
        
    def get_characters(self, *args, **kwargs):
        """Fetches lists of comic characters with optional filters.

        get /v1/public/characters/{characterId}

        :returns:  CharacterDataWrapper

        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_characters(orderBy="name,-modified", limit="5", offset="15")
        >>> print cdw.data.count
        1401
        >>> for result in cdw.data.results:
        ...     print result.name
        Aginar
        Air-Walker (Gabriel Lan)
        Ajak
        Ajaxis
        Akemi
        
        """
        #pass url string and params string to _call
        response = json.loads(self._call(Character.resource_url(), self._params(kwargs)).text)
        return CharacterDataWrapper(self, response, kwargs)

    def get_comic(self, id):
        """Fetches a single comic by id.
        
        get /v1/public/comics/{comicId}
        
        :param id: ID of Comic
        :type params: int
        
        :returns:  ComicDataWrapper

        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_comic(1009718)
        >>> print cdw.data.count
        1
        >>> print cdw.data.result.name
        Some Comic
        """
        
        url = "%s/%s" % (Comic.resource_url(), id)
        response = json.loads(self._call(url).text)
        return ComicDataWrapper(self, response)
                
    def get_comics(self, *args, **kwargs):
        """
        Fetches list of comics.

        get /v1/public/comics
                
        :returns:  ComicDataWrapper
        
        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_comics(orderBy="issueNumber,-modified", limit="10", offset="15")
        >>> print cdw.data.count
        10
        >>> print cdw.data.results[0].name
        Some Comic

        """

        response = json.loads(self._call(Comic.resource_url(), self._params(kwargs)).text)
        return ComicDataWrapper(self, response)
        
        
    def get_creator(self, id):
        """Fetches a single creator by id.

        get /v1/public/creators/{creatorId}

        :param id: ID of Creator
        :type params: int
        
        :returns:  CreatorDataWrapper

        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_creator(30)
        >>> print cdw.data.count
        1
        >>> print cdw.data.result.fullName
        Stan Lee
        """

        url = "%s/%s" % (Creator.resource_url(), id)
        response = json.loads(self._call(url).text)
        return CreatorDataWrapper(self, response)

        
    def get_creators(self, *args, **kwargs):
        """Fetches lists of creators.
        
        get /v1/public/creators
        
        :returns:  CreatorDataWrapper

        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_creators(lastName="Lee", orderBy="firstName,-modified", limit="5", offset="15")
        >>> print cdw.data.total
        25
        >>> print cdw.data.results[0].fullName
        Alvin Lee
        """
        
        response = json.loads(self._call(Creator.resource_url(), self._params(kwargs)).text)
        return CreatorDataWrapper(self, response)
        
        
    def get_event(self, id):
        """Fetches a single event by id.

        get /v1/public/event/{eventId}

        :param id: ID of Event
        :type params: int
        
        :returns:  EventDataWrapper

        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_event(253)
        >>> print response.data.result.title
        Infinity Gauntlet
        """

        url = "%s/%s" % (Event.resource_url(), id)
        response = json.loads(self._call(url).text)
        return EventDataWrapper(self, response)
        
        
    def get_events(self, *args, **kwargs):
        """Fetches lists of events.

        get /v1/public/events

        :returns:  EventDataWrapper

        >>> #Find all the events that involved both Hulk and Wolverine
        >>> #hulk's id: 1009351
        >>> #wolverine's id: 1009718
        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_events(characters="1009351,1009718")
        >>> print response.data.total
        38
        >>> events = response.data.results
        >>> print events[1].title
        Age of Apocalypse
        """

        response = json.loads(self._call(Event.resource_url(), self._params(kwargs)).text)
        return EventDataWrapper(self, response)
        
        
    def get_single_series(self, id):
        """Fetches a single comic series by id.

        get /v1/public/series/{seriesId}

        :param id: ID of Series
        :type params: int
        
        :returns:  SeriesDataWrapper
        
        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_single_series(12429)
        >>> print response.data.result.title
        5 Ronin (2010)
        """

        url = "%s/%s" % (Series.resource_url(), id)
        response = json.loads(self._call(url).text)
        return SeriesDataWrapper(self, response)


    def get_series(self, *args, **kwargs):
        """Fetches lists of events.

        get /v1/public/events
        
        :returns:  SeriesDataWrapper
        
        >>> #Find all the series that involved Wolverine
        >>> #wolverine's id: 1009718
        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_series(characters="1009718")
        >>> print response.data.total
        435
        >>> series = response.data.results
        >>> print series[0].title
        5 Ronin (2010)
        """

        response = json.loads(self._call(Series.resource_url(), self._params(kwargs)).text)
        return SeriesDataWrapper(self, response)

    def get_story(self, id):
        """Fetches a single story by id.

        get /v1/public/stories/{storyId}

        :param id: ID of Story
        :type params: int
        
        :returns:  StoryDataWrapper
        
        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_story(29)
        >>> print response.data.result.title
        Caught in the heart of a nuclear explosion, mild-mannered scientist Bruce Banner finds himself...
        """

        url = "%s/%s" % (Story.resource_url(), id)
        response = json.loads(self._call(url).text)
        return StoryDataWrapper(self, response)


    def get_stories(self, *args, **kwargs):
        """Fetches lists of stories.

        get /v1/public/stories
        
        :returns:  StoryDataWrapper
        
        >>> #Find all the stories that involved both Hulk and Wolverine
        >>> #hulk's id: 1009351
        >>> #wolverine's id: 1009718
        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_stories(characters="1009351,1009718")
        >>> print response.data.total
        4066
        >>> stories = response.data.results
        >>> print stories[1].title
        Cover #477
        """

        response = json.loads(self._call(Story.resource_url(), self._params(kwargs)).text)
        return StoryDataWrapper(self, response)