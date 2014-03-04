import json
import os
import unittest

from .marvel import Marvel
from .core import TextObject, Image
from .creator import CreatorList, CreatorSummary
from .character import CharacterDataWrapper, CharacterDataContainer, Character, CharacterList, CharacterSummary
from .story import StoryList, StorySummary, Story
from .event import EventList, EventSummary, Event
from .comic import ComicDataWrapper, ComicDataContainer, Comic, ComicSummary, ComicDate, ComicPrice
from .config import *

class PyMarvelTestCase(unittest.TestCase):

    def setUp(self):
        self.m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
        
        #Character
        self.character_dw = self.m.get_character(1009718)
        self.character = self.character_dw.data.result
        
        #Comic
        #TODO: Need a comic with everything
        self.comic_dw = self.m.get_comic(17731)
        self.comic = self.comic_dw.data.result
                
        #Creators
        #Grab Stan the Man
        self.creator_dw = self.m.get_creator(30)
        self.creator = self.creator_dw.data.result

        #Series
        self.series_dw = self.m.get_single_series(12429)
        self.series = self.series_dw.data.result

        #Story
        self.story_dw = self.m.get_story(29)
        self.story = self.story_dw.data.result


    def tearDown(self):
        pass

    #Character Tests
    def test_get_character(self):

        assert self.character_dw.code == 200
        assert self.character_dw.status == 'Ok'
        assert self.character.name == "Wolverine"

        print "\nMarvel.get_character(): \n"
        print self.character.name

    def test_character_get_comics(self):

        comic_dw = self.character.get_comics()

        assert comic_dw.code == 200
        assert comic_dw.status == 'Ok'
        
        print "\nCharacter.get_comics(): \n"
        for c in comic_dw.data.results:
            print "%s - %s" % (c.id, c.title)

        comic_dw_params = self.character.get_comics(format="comic", formatType="comic", hasDigitalIssue=True, orderBy="title", limit=10, offset=30)

        assert comic_dw_params.code == 200
        assert comic_dw_params.status == 'Ok'
        
        print "\nCharacter.get_comics(params): \n"
        for c in comic_dw_params.data.results:
            print "%s - %s" % (c.id, c.title)

    def test_character_get_events(self):

        events_dw = self.character.get_events()

        assert events_dw.code == 200
        assert events_dw.status == 'Ok'

        print "\nCharacter.get_events(): \n"
        for e in events_dw.data.results:
            print "%s - %s" % (e.id, e.title)

        events_dw_params = self.character.get_events(orderBy="startDate", limit=10)

        assert events_dw_params.code == 200
        assert events_dw_params.status == 'Ok'

        print "\nCharacter.get_events(params): \n"
        for e in events_dw_params.data.results:
            print "%s - %s" % (e.id, e.title)

    def test_get_characters(self):
        
        characters_dw = self.m.get_characters(orderBy="name,-modified", limit="10", offset="15")

        assert characters_dw.code == 200
        assert characters_dw.status == 'Ok'

        assert characters_dw.data.count > 0
        assert characters_dw.data.offset == 15
        assert characters_dw.data.limit == 10
        assert len(characters_dw.data.results) > 0

        assert type(characters_dw) is CharacterDataWrapper
        assert type(characters_dw.data) is CharacterDataContainer
        assert type(characters_dw.data.results) is list

        print "\nMarvel.get_characters():\n"
        for c in characters_dw.data.results:
            print "%s - %s" % (c.id, c.name)

    def test_get_characters_next(self):
        
        characters_dw = self.m.get_characters(orderBy="name,-modified", limit="10", offset="15")
        new_cdw = characters_dw.next()

        assert new_cdw.code == 200

        #poor test?
        assert new_cdw.data.offset == characters_dw.data.offset + characters_dw.data.limit





    #Comic Tests
    def test_get_comic(self):

        assert self.comic_dw.code == 200
        assert self.comic_dw.status == 'Ok'

        assert self.comic_dw.data.count > 0
        assert self.comic_dw.data.offset == 0
        assert len(self.comic_dw.data.results) > 0

        assert type(self.comic_dw) is ComicDataWrapper
        assert type(self.comic_dw.data) is ComicDataContainer
        assert type(self.comic_dw.data.results) is list

        #properties
        #textObjects
        #assert len(self.comic_dw.data.result.textObjects) > 0
        #assert isinstance(self.comic_dw.data.result.textObjects[0], TextObject)
        #collections
        assert isinstance(self.comic_dw.data.result.collections[0], ComicSummary)
        #prices/dates
        assert isinstance(self.comic_dw.data.result.prices[0], ComicPrice)
        assert isinstance(self.comic_dw.data.result.dates[0], ComicDate)
        #images
        assert isinstance(self.comic_dw.data.result.thumbnail, Image)
        assert isinstance(self.comic_dw.data.result.images[0], Image)
        #lists
        assert isinstance(self.comic_dw.data.result.creators, CreatorList)
        assert isinstance(self.comic_dw.data.result.creators.items[0], CreatorSummary)
        assert isinstance(self.comic_dw.data.result.characters, CharacterList)
        assert isinstance(self.comic_dw.data.result.characters.items[0], CharacterSummary)
        assert isinstance(self.comic_dw.data.result.stories, StoryList)
        assert isinstance(self.comic_dw.data.result.stories.items[0], StorySummary)
        #TODO: Need a test case with an Event
        #assert isinstance(cdw.data.result.events, EventList)
        #assert isinstance(cdw.data.result.events.items[0], EventSummary)


        print "\nMarvel.get_comic(): \n"
        print self.comic.title


    def test_comic_get_events(self):

        events_dw = self.comic.get_events()

        assert events_dw.code == 200
        assert events_dw.status == 'Ok'

        print "\nComic.get_events(): \n"
        for e in events_dw.data.results:
            print "%s - %s" % (e.id, e.title)

        events_dw_params = self.comic.get_events(orderBy="startDate", limit=1)

        assert events_dw_params.code == 200
        assert events_dw_params.status == 'Ok'

        print "\nComic.get_events(params): \n"
        for e in events_dw_params.data.results:
            print "%s - %s" % (e.id, e.title)

        
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
            

    def test_get_creator(self):

        assert self.creator_dw.code == 200
        assert self.creator_dw.status == 'Ok'
        assert self.creator.firstName == "Stan"
        assert self.creator.lastName == "Lee"

    def test_creator_get_comics(self):
        
        comic_dw = self.creator.get_comics()

        assert comic_dw.code == 200
        assert comic_dw.status == 'Ok'
        
        print "\nCreator.get_comics(): \n"
        for c in comic_dw.data.results:
            print "%s - %s" % (c.id, c.title)

        comic_dw_params = self.creator.get_comics(format="comic", formatType="comic", hasDigitalIssue=True, orderBy="title", limit=10, offset=30)

        assert comic_dw_params.code == 200
        assert comic_dw_params.status == 'Ok'
        
        print "\nCreator.get_comics(params): \n"
        for c in comic_dw_params.data.results:
            print "%s - %s" % (c.id, c.title)

    def test_creator_get_events(self):

        events_dw = self.creator.get_events()

        assert events_dw.code == 200
        assert events_dw.status == 'Ok'

        print "\nCreator.get_events(): \n"
        for e in events_dw.data.results:
            print "%s - %s" % (e.id, e.title)

        events_dw_params = self.creator.get_events(orderBy="startDate")

        assert events_dw_params.code == 200
        assert events_dw_params.status == 'Ok'

        print "\nCreator.get_events(params): \n"
        for e in events_dw_params.data.results:
            print "%s - %s" % (e.id, e.title)




    def test_get_event(self):
        event_dw = self.m.get_event(253)

        assert event_dw.code == 200
        assert event_dw.status == 'Ok'        

        print "\nMarvel.get_event: \n"
        event = event_dw.data.result
        assert isinstance(event, Event)
        assert event.title == "Infinity Gauntlet"
        print event.title
        print event.description


    def test_get_events(self):
        response = self.m.get_events(characters="1009351,1009718")

        assert response.code == 200
        assert response.status == 'Ok'

        assert response.data.total > 0

        print "\nMarvel.get_events(): \n"
        for e in response.data.results:
            print "%s" % e.title

    def test_get_single_series(self):

        assert self.series_dw.code == 200
        assert self.series_dw.status == 'Ok'
        assert self.series.title == "5 Ronin (2010)"

        print "\nMarvel.get_single_series(): \n"
        print self.series.title
        
    def test_get_series(self):

        response = self.m.get_series(characters="1009718", limit=10)

        assert response.code == 200
        assert response.status == 'Ok'

        assert response.data.total > 0

        print "\nMarvel.get_series(): \n"
        for s in response.data.results:
            print "%s" % s.title


    def test_get_story(self):
        
        assert self.story_dw.code == 200
        assert self.story_dw.status == 'Ok'        

        print "\nMarvel.get_story(): \n"
        assert isinstance(self.story, Story)
        print self.story.title

    def test_get_stories(self):
        
        response = self.m.get_stories(characters="1009351,1009718", limit=10)

        assert response.code == 200
        assert response.status == 'Ok'
        assert response.data.total > 0

        print "\nMarvel.get_events(): \n"
        for s in response.data.results:
            print "%s" % s.title


    def test_chain(self):
        print "\nMethod Chaining:\n"
        event = self.m.get_series(characters="1009718").data.result.get_characters().data.results[1].get_comics().data.results[0].get_creators().data.results[0].get_events().data.results[0]
        assert isinstance(event, Event)
        print event.title
        
if __name__ == '__main__':
    unittest.main()

"python -m unittest marvel.tests"