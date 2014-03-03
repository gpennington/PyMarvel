[![Build Status](https://travis-ci.org/gpennington/PyMarvel.png?branch=master)](https://travis-ci.org/gpennington/PyMarvel)

PyMarvel
========

Python wrapper for Marvel API
http://developer.marvel.com/

Why is this useful?
===================

PyMarvel takes care of authorization and provides convenient methods calling the API. PyMarvel automatically decodes Marvel's JSON response into Python objects and primitives.

Basic Usage
===========

    >>> m = Marvel(public_key, private_key)
    >>> character_data_wrapper = m.get_characters(orderBy="name,-modified", limit="5", offset="15")
    >>> print character_data_wrapper.status
    Ok
    >>> print character_data_wrapper.data.total
    1402
    >>> for character in character_data_wrapper.data.results
    >>>     print character.name
    Aginar
    Air-Walker (Gabriel Lan)
    Ajak
    Ajaxis
    Akemi


Calling methods
===============

Find Stan Lee's comics:

    stan_lee = m.get_creator(30).data.result
    comics = stan_lee.get_comics()
    

You can chain methods into one line:

    comics = m.get_creator(30).data.result.get_comics()

or even:

    events = self.m.get_series(characters="1009718").data.result.get_characters().data.result.get_comics().data.results.get_creators().data.result.get_events()

would be the equivalent to calling:

    http://gateway.marvel.com/v1/public/series?characters=100971
    http://gateway.marvel.com/v1/public/series/15276/characters
    http://gateway.marvel.com/v1/public/characters/1009351/comics
    http://gateway.marvel.com/v1/public/comics/50372/creators
    http://gateway.marvel.com/v1/public/creators/4600/events
    

Pagination
==========

    >>> xmen = m.get_single_series(403).get_characters(limit=5)
    >>> for xm in xmen.data.results:
    ...     print xm.name
    
    Archangel
    Banshee
    Beast
    Bishop
    Black Panther
    
    >>> more_xmen = xmen.next()
    >>> for xm in more_exmen.data.results:
    ...     print xm.name
    
    Cable
    Cannonball
    Colossus
    Cyclops
    Emma Frost
    
