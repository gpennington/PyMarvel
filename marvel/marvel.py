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

    def _call(self, resource_url):
        """
        Calls Marvel API
        Returns Requests reponse
        """
        url = "%s%s%s" % (self._endpoint(), resource_url, self._auth())
        print "url:"
        print url
        return requests.get(url)


    def _auth(self):
        print "auth:"
        ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        print ts
        hash_string = hashlib.md5("%s%s%s" % (ts, self.private_key, self.public_key)).hexdigest()
        print hash_string
        print ""
        return "?ts=%s&apikey=%s&hash=%s" % (ts, self.public_key, hash_string)

    def get_character(self, id):
        #character/:id/
        url = "%s%s" % (Character.resource_url(), id)
        return Character( self, json.loads(self._call(url).text) )


