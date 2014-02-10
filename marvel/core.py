# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'


class MarvelObject(object):
    """
    Base class for all Marvel API classes
    """

    def __init__(self, marvel, dict):
        """
        init
        marvel - instance of Marvel class caller
        dict - dict of object, used to create MarvelObject
        
        """
        self.marvel = marvel
        self.dict = dict
        
    def __unicode__(self):
        return self.dict['name']
    
    def to_dict(self):
        return self.dict
        
    @classmethod
    def resource_url(cls):
        return cls._resource_url

class DataWrapper(object):
    """
    DataWrapper object
    """

    def __init__(self, marvel, dict, params=None):
        """
        init
        marvel - instance of Marvel class caller
        dict - dict of object, used to create MarvelObject
        params - dict of query params passed to original call
        
        """
        self.marvel = marvel
        self.dict = dict
        self.params = params


    @property
    def code(self):
        return self.dict['code']

    @property
    def status(self):
        return self.dict['status']

    @property
    def etag(self):
        return self.dict['etag']

class DataContainer(object):
    """
    DataContainer object
    """

    def __init__(self, marvel, dict):
        """
        init
        marvel - instance of Marvel class caller
        dict - dict of object, used to create MarvelObject

        """
        self.marvel = marvel
        self.dict = dict


    @property
    def offset(self):
        return self.dict['offset']

    @property
    def limit(self):
        return self.dict['limit']

    @property
    def total(self):
        return self.dict['total']
    
    @property
    def count(self):
        return self.dict['count']