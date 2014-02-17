import json
import os
import unittest

from .marvel import Marvel
from .core import TextObject, Image
from .character import CharacterDataWrapper, CharacterDataContainer, Character
from .comic import ComicDataWrapper, ComicDataContainer, Comic, ComicSummary, ComicDate, ComicPrice
from .config import *

class PyMarvelTestCase(unittest.TestCase):

    def setUp(self):
        self.m = Marvel(PUBLIC_KEY, PRIVATE_KEY)

    def tearDown(self):
        pass

    def test_get_character(self):
        cdw = self.m.get_character(1009718)

        assert cdw.code == 200
        assert cdw.status == 'Ok'
        assert cdw.data.results[0].name == "Wolverine"

        print "\nGet Character: \n"
        print cdw.data.results[0].name

    def test_get_character_get_comics(self):
        character = self.m.get_character(1009718).data.results[0]
        comic_dw = character.get_comics()

        assert comic_dw.code == 200
        assert comic_dw.status == 'Ok'
        
        print "\nWolverine comics: \n"
        for c in comic_dw.data.results:
            print "%s - %s" % (c.id, c.title)

        comic_dw_params = character.get_comics(format="comic", formatType="comic", hasDigitalIssue=True, orderBy="title", limit=10, offset=30)

        assert comic_dw_params.code == 200
        assert comic_dw_params.status == 'Ok'
        
        print "\nWolverine comics with parameters: \n"
        for c in comic_dw_params.data.results:
            print "%s - %s" % (c.id, c.title)


    def test_get_characters(self):
        cdw = self.m.get_characters(orderBy="name,-modified", limit="10", offset="15")

        assert cdw.code == 200
        assert cdw.status == 'Ok'

        assert cdw.data.count > 0
        assert cdw.data.offset == 15
        assert cdw.data.limit == 10
        assert len(cdw.data.results) > 0

        assert type(cdw) is CharacterDataWrapper
        assert type(cdw.data) is CharacterDataContainer
        assert type(cdw.data.results) is list

        print "\nGet Characters: \n"
        for c in cdw.data.results:
            print "%s - %s" % (c.id, c.name)

    def test_get_characters_next(self):
        cdw = self.m.get_characters(orderBy="name,-modified", limit="20", offset="15")
        new_cdw = cdw.next()

        assert new_cdw.code == 200

        #poor test?
        assert new_cdw.data.offset == cdw.data.offset + cdw.data.limit


    def test_get_comic(self):
        #Need a comic with everything
        cdw = self.m.get_comic(531)

        assert cdw.code == 200
        assert cdw.status == 'Ok'

        assert cdw.data.count > 0
        assert cdw.data.offset == 0
        assert len(cdw.data.results) > 0

        assert type(cdw) is ComicDataWrapper
        assert type(cdw.data) is ComicDataContainer
        assert type(cdw.data.results) is list

        #properties
        #textObjects
        assert len(cdw.data.results[0].textObjects) > 0
        assert isinstance(cdw.data.results[0].textObjects[0], TextObject)
        #collections
        assert isinstance(cdw.data.results[0].collections[0], ComicSummary)
        #prices/dates
        assert isinstance(cdw.data.results[0].prices[0], ComicPrice)
        assert isinstance(cdw.data.results[0].dates[0], ComicDate)
        #images
        assert isinstance(cdw.data.results[0].thumbnail, Image)

        
    def test_get_comics(self):
        cdw = self.m.get_comics(orderBy="issueNumber,-modified", limit="10", offset="15")

        assert cdw.code == 200
        assert cdw.status == 'Ok'

        assert cdw.data.count > 0
        assert cdw.data.offset == 15
        assert cdw.data.limit == 10
        assert len(cdw.data.results) > 0

        assert type(cdw) is ComicDataWrapper
        assert type(cdw.data) is ComicDataContainer
        assert type(cdw.data.results) is list

        for c in cdw.data.results:
            print "%s - %s" % (c.id, c.title)
            
            
if __name__ == '__main__':
    unittest.main()
