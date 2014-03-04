API
===

Python wrapper for the Marvel API


Marvel API to PyMarvel
----------------------

    get /v1/public/characters
        Fetches lists of characters.
    
        Marvel.get_characters()

    get /v1/public/characters/{characterId}
        Fetches a single character by id.
    
        Marvel.get_character()

    get /v1/public/characters/{characterId}/comics
        Fetches lists of comics filtered by a character id.
    
        Character.get_comics()

    get /v1/public/characters/{characterId}/events
        Fetches lists of events filtered by a character id.
    
        Character.get_events()

    get /v1/public/characters/{characterId}/series
        Fetches lists of series filtered by a character id.

        Character.get_series()

    get /v1/public/characters/{characterId}/stories
        Fetches lists of stories filtered by a character id.
    
        Character.get_stories()

    get /v1/public/comics
        Fetches lists of comics.
    
        X Marvel.get_comics()

    get /v1/public/comics/{comicId}
        Fetches a single comic by id.
    
        X Marvel.get_comic()

    get /v1/public/comics/{comicId}/characters
        Fetches lists of characters filtered by a comic id.
    
        Comic.get_characters()

    get /v1/public/comics/{comicId}/creators
        Fetches lists of creators filtered by a comic id.
    
        Comic.get_creators()

    get /v1/public/comics/{comicId}/events
        Fetches lists of events filtered by a comic id.
    
        Comic.get_events()

    get /v1/public/comics/{comicId}/stories
        Fetches lists of stories filtered by a comic id.
    
        Comic.get_stories()

    get /v1/public/creators
        Fetches lists of creators.
    
        Marvel.get_creators()

    get /v1/public/creators/{creatorId}
        Fetches a single creator by id.
    
        Marvel.get_creator()

    get /v1/public/creators/{creatorId}/comics
        Fetches lists of comics filtered by a creator id.
    
        Creator.get_comics()

    get /v1/public/creators/{creatorId}/events
        Fetches lists of events filtered by a creator id.
    
        Creator.get_events()

    get /v1/public/creators/{creatorId}/series
        Fetches lists of series filtered by a creator id.
    
        Creator.get_series()

    get /v1/public/creators/{creatorId}/stories
        Fetches lists of stories filtered by a creator id.

        Creator.get_stories()

    get /v1/public/events
        Fetches lists of events.
    
        Marvel.get_events()

    get /v1/public/events/{eventId}
        Fetches a single event by id.
    
        Marvel.get_event()

    get /v1/public/events/{eventId}/characters
        Fetches lists of characters filtered by an event id.
    
        Event.get_characters()

    get /v1/public/events/{eventId}/comics
        Fetches lists of comics filtered by an event id.
    
        Event.get_comics()

    get /v1/public/events/{eventId}/creators
        Fetches lists of creators filtered by an event id.
    
        Event.get_creators()

    get /v1/public/events/{eventId}/series
        Fetches lists of series filtered by an event id.
    
        Event.get_series()

    get /v1/public/events/{eventId}/stories
        Fetches lists of stories filtered by an event id.
    
        Event.get_stories()

    get /v1/public/series
        Fetches lists of series.
    
        Marvel.get_series()

    get /v1/public/series/{seriesId}
        Fetches a single comic series by id.
    
        Marvel.get_series()

    get /v1/public/series/{seriesId}/characters
        Fetches lists of characters filtered by a series id.
    
        Series.get_characters()

    get /v1/public/series/{seriesId}/comics
        Fetches lists of comics filtered by a series id.
    
        Series.get_comics()

    get /v1/public/series/{seriesId}/creators
        Fetches lists of creators filtered by a series id.
    
        Series.get_creators()

    get /v1/public/series/{seriesId}/events
        Fetches lists of events filtered by a series id.
    
        Series.get_events()

    get /v1/public/series/{seriesId}/stories
        Fetches lists of stories filtered by a series id.
    
        Series.get_stories()

    get /v1/public/stories
        Fetches lists of stories.
    
        Marvel.get_stories()

    get /v1/public/stories/{storyId}
        Fetches a single comic story by id.
    
        Marvel.get_story()

    get /v1/public/stories/{storyId}/characters
        Fetches lists of characters filtered by a story id.
    
        Story.get_characters()

    get /v1/public/stories/{storyId}/comics
        Fetches lists of comics filtered by a story id.
    
        Story.get_comics()

    get /v1/public/stories/{storyId}/creators
        Fetches lists of creators filtered by a story id.
    
        Story.get_creators()

    get /v1/public/stories/{storyId}/events
        Fetches lists of events filtered by a story id.
    
        Story.get_events()


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

