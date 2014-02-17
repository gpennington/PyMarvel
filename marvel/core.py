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
        
    def str_to_datetime(self, _str):
        """ Converts '2013-11-20T17:40:18-0500' format to 'datetime' object """
        #Hacked off %z timezone because reasons
        return datetime.strptime(_str[:-6], '%Y-%m-%dT%H:%M:%S')
        
        
class List(MarvelObject):
    """
    List object
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
        
class Summary(MarvelObject):
    """
    Summary
    """

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def name(self):
        return self.dict['name']
        
class TextObject(MarvelObject):
    """
    TextObject

    type (string, optional): The canonical type of the text object (e.g. solicit text, preview text, etc.).,
    language (string, optional): The IETF language tag denoting the language the text object is written in.,
    text (string, optional): The text.
    """

    @property
    def type(self):
        return self.dict['type']

    @property
    def language(self):
        return self.dict['language']

    @property
    def text(self):
        return self.dict['text']
        

class Image(MarvelObject):
    """
    Image
    """

    @property
    def path(self):
        return self.dict['path']

    @property
    def extension(self):
        return self.dict['extension']

    def __repr__(self):
        return "%s.%s" % (self.path, self.extension)

