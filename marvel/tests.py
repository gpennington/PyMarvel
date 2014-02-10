import json
import os
import unittest

from .marvel import Marvel
from .character import CharacterDataWrapper, CharacterDataContainer, Character
from .comic import ComicDataWrapper, ComicDataContainer, Comic
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

        for c in cdw.data.results:
            print "%s - %s" % (c.id, c.name)

    def test_get_comic(self):
        cdw = self.m.get_comic(41530)

        assert cdw.code == 200
        assert cdw.status == 'Ok'

        assert cdw.data.count > 0
        assert cdw.data.offset == 0
        assert len(cdw.data.results) > 0

        assert type(cdw) is ComicDataWrapper
        assert type(cdw.data) is ComicDataContainer
        assert type(cdw.data.results) is list
        
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
