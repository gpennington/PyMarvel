# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, List, Summary, TextObject, Image
 

class ComicDataWrapper(DataWrapper):
    @property
    def data(self):
        return ComicDataContainer(self.marvel, self.dict['data'])

class ComicDataContainer(DataContainer):
    @property
    def results(self):
        return self.list_to_instance_list(self.dict['results'], Comic)

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
    def digitalId(self):
        return int(self.dict['digitalId'])

    @property
    def title(self):
        return self.dict['title']

    @property
    def issueNumber(self):
        return float(self.dict['issueNumber'])

    @property
    def variantDescription(self):
        return self.dict['description']

    @property
    def description(self):
        """
        :returns:  str -- The preferred description of the comic.
        """
        return self.dict['description']

    @property
    def modified(self):
        return str_to_datetime(self.dict['modified'])

    @property
    def modified_raw(self):
        return self.dict['modified']

    @property
    def isbn(self):
        return self.dict['isbn']

    @property
    def upc(self):
        return self.dict['upc']

    @property
    def diamondCode(self):
        return self.dict['diamondCode']

    @property
    def ean(self):
        return self.dict['ean']

    @property
    def issn(self):
        return self.dict['issn']

    @property
    def format(self):
        return self.dict['format']

    @property
    def pageCount(self):
        return int(self.dict['pageCount'])

    @property
    def textObjects(self):
        """
        :returns: list -- List of TextObjects
        """
        return self.list_to_instance_list(self.dict['textObjects'], TextObject)

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def urls(self):
        return self.dict['urls']

    @property
    def series(self):
        return self.dict['series']

    @property
    def variants(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['variants'], ComicSummary)
                    
    @property
    def collections(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['collections'], ComicSummary)

    @property
    def collectedIssues(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['collectedIssues'], ComicSummary)

    @property
    def dates(self):
        return self.list_to_instance_list(self.dict['dates'], ComicDate)

    @property
    def prices(self):
        return self.list_to_instance_list(self.dict['prices'], ComicPrice)

    @property
    def thumbnail(self):
        return Image(self.marvel, self.dict['thumbnail'])

    @property
    def images(self):
        return self.list_to_instance_list(self.dict['images'], Image)

    @property
    def creators(self):
        return self.dict['creators']

    @property
    def characters(self):
        return self.dict['characters']

    @property
    def stories(self):
        return self.dict['stories']
        
    @property
    def events(self):
        return self.dict['events']
        

"""
id (int, optional): The unique ID of the comic resource.,
digitalId (int, optional): The ID of the digital comic representation of this comic. Will be 0 if the comic is not available digitally.,
title (string, optional): The canonical title of the comic.,
issueNumber (double, optional): The number of the issue in the series (will generally be 0 for collection formats).,
variantDescription (string, optional): If the issue is a variant (e.g. an alternate cover, second printing, or director’s cut), a text description of the variant.,
description (string, optional): The preferred description of the comic.,
modified (Date, optional): The date the resource was most recently modified.,
isbn (string, optional): The ISBN for the comic (generally only populated for collection formats).,
upc (string, optional): The UPC barcode number for the comic (generally only populated for periodical formats).,
diamondCode (string, optional): The Diamond code for the comic.,
ean (string, optional): The EAN barcode for the comic.,
issn (string, optional): The ISSN barcode for the comic.,
format (string, optional): The publication format of the comic e.g. comic, hardcover, trade paperback.,
pageCount (int, optional): The number of story pages in the comic.,
textObjects (Array[TextObject], optional): A set of descriptive text blurbs for the comic.,
resourceURI (string, optional): The canonical URL identifier for this resource.,
urls (Array[Url], optional): A set of public web site URLs for the resource.,
series (SeriesSummary, optional): A summary representation of the series to which this comic belongs.,
variants (Array[ComicSummary], optional): A list of variant issues for this comic (includes the "original" issue if the current issue is a variant).,
collections (Array[ComicSummary], optional): A list of collections which include this comic (will generally be empty if the comic's format is a collection).,
collectedIssues (Array[ComicSummary], optional): A list of issues collected in this comic (will generally be empty for periodical formats such as "comic" or "magazine").,
dates (Array[ComicDate], optional): A list of key dates for this comic.,
prices (Array[ComicPrice], optional): A list of prices for this comic.,
thumbnail (Image, optional): The representative image for this comic.,
images (Array[Image], optional): A list of promotional images associated with this comic.,
creators (CreatorList, optional): A resource list containing the creators associated with this comic.,
characters (CharacterList, optional): A resource list containing the characters which appear in this comic.,
stories (StoryList, optional): A resource list containing the stories which appear in this comic.,
events (EventList, optional): A resource list containing the events in which this comic appears.
"""

class ComicList(List):
    """
    ComicList object
    """

    @property
    def items(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['items'], ComicSummary)

class ComicSummary(Summary):
    """
    CommicSummary object
    """

class ComicDate(MarvelObject):
    """
    ComicDate object
    """
    @property
    def type(self):
        return self.dict['type']

    @property
    def date(self):
        return self.str_to_datetime(self.dict['date'])

class ComicPrice(MarvelObject):
    """
    ComicPrice object
    """
    @property
    def type(self):
        return self.dict['type']

    @property
    def price(self):
        return float(self.dict['price'])
