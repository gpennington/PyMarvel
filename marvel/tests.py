import json
import os
import unittest

from .marvel import Marvel
from .character import CharacterDataWrapper, CharacterDataContainer, Character
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

        assert type(cdw) is CharacterDataWrapper
        assert type(cdw.data) is CharacterDataContainer
        assert type(cdw.data.results) is list

        for c in characters.data.results:
            print "%s - %s" % (c.id, c.name)

        
if __name__ == '__main__':
    unittest.main()
