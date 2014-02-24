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

DEFAULT_API_VERSION = 'v1'

class Marvel(object):
    """Marvel API class

    This class provides methods to interface with the Marvel API

    >>> m = Marvel("acb123....", "efg456...")

    """

    def __init__(self, public_key, private_key):
        """
        Args:
           public_key (str): Public api key available from http://developer.marvel.com
           private (str): Private api key available from http://developer.marvel.com

        Kwargs:
           bar (str): Really, same as foo.

        """
        self.public_key = public_key
        self.private_key = private_key
        
    def _endpoint(self):
        return "http://gateway.marvel.com/%s/public/" % (DEFAULT_API_VERSION)

    def _call(self, resource_url, params=None):
        """
        Calls Marvel API
        Returns Requests reponse
        """
        
        url = "%s%s" % (self._endpoint(), resource_url)
        if params:
            url += "?%s&%s" % (params, self._auth())
        else:
            url += "?%s" % self._auth()
        
        #print "url:"
        #print url
        return requests.get(url)

    def _params(self, params):
        """
        Takes dictionary of parameters and returns
        urlencoded string 
        """
        return urllib.urlencode(params)

    def _auth(self):
        ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        hash_string = hashlib.md5("%s%s%s" % (ts, self.private_key, self.public_key)).hexdigest()
        return "ts=%s&apikey=%s&hash=%s" % (ts, self.public_key, hash_string)





    #public methods
    def get_character(self, id):
        """Fetches a single character by id.
        
        Returns a CharacterDataWrapper object

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
        
        Returns a CharacterDataWrapper object

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
        
        Returns a ComicDataWrapper object

        >>> m = Marvel(public_key, private_key)
        >>> cdw = m.get_comic(1009718)
        >>> print cdw.data.count
        1
        >>> print cdw.data.results[0].name
        Some Comic
        """
        
        url = "%s/%s" % (Comic.resource_url(), id)
        response = json.loads(self._call(url).text)
        return ComicDataWrapper(self, response)
                
    def get_comics(self, *args, **kwargs):
        """
        comics/<?params>
        """
        #pass url string and params string to _call
        response = json.loads(self._call(Comic.resource_url(), self._params(kwargs)).text)
        return ComicDataWrapper(self, response)
        
        
    def get_creator(self, id):
        """Fetches a single creator by id.

        get /v1/public/creators/{creatorId}

        Returns a CreatorDataWrapper object

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
        
        get /v1/public/creators/{creatorId}
        
        Returns a CreatorDataWrapper object

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

        Returns a EventDataWrapper object

        >>> m = Marvel(public_key, private_key)
        >>> response = m.get_event(253)
        >>> print response.data.result.title
        Infinity Gauntlet
        """

        url = "%s/%s" % (Event.resource_url(), id)
        response = json.loads(self._call(url).text)
        return EventDataWrapper(self, response)
