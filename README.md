PyMarvel
========

Python wrapper for Marvel API
http://developer.marvel.com/

Why is this useful?
===================

PyMarvel takes care of authorization and provides convenient methods calling the API. PyMarvel automatically decodes Marvel's JSON response into Python objects and primitives.

Usage
=====

    m = Marvel(public_key, private_key)
    
    >>> character_data_wrapper = m.get_characters(orderBy="name,-modified", limit="10", offset="15")
    >>> print character_data_wrapper.data.total
    1402
    >>> for character in character_data_wrapper.data.results
    >>>     print character.name
    Aginar
    Air-Walker (Gabriel Lan)
    Ajak
    Ajaxis
    Akemi
    Alain
    Albert Cleary
    Albion
    Alex Power
    Alex Wilder
    
