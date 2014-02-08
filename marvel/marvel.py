# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

import urllib
import json
import hashlib
import datetime

import requests

from .character import Character

DEFAULT_API_VERSION = 'v1'

class Marvel(object):
    """
    main Marvel class
    """

    def __init__(self, public_key, private_key):
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
        
        print "url:"
        print url
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
        #characters/:id/
        url = "%s/%s" % (Character.resource_url(), id)
        response = json.loads(self._call(url).text)
        
        #create Character from first item in 'results'
        return Character( self,  response['data']['results'][0] )

    def get_characters(self, *args, **kwargs):
        #characters/
        characters = []
        #pass url string and params string to _call
        response = json.loads(self._call(Character.resource_url(), self._params(kwargs)).text)
        for character in response['data']['results']:
            characters.append(Character(self, character))
            
        return characters



