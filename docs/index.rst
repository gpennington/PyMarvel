PyMarvel
========

Python wrapper for the Marvel API

.. toctree::
    :maxdepth: 2
    
    api
    Reference: Marvel <reference/marvel>
    Reference: Core <reference/core>
    Reference: Character <reference/character>
    Reference: Comic <reference/comic>
    Reference: Creator <reference/creator>
    Reference: Story <reference/story>
    Reference: Series <reference/series>
    Reference: Event <reference/event>

    
Documentation
-------------

Read the full `documentation <http://pymarvel.readthedocs.org>`__.


Installation
------------
Use pip::

    pip install PyMarvel

or::

    easy_install PyMarvel

`Python Package Index <https://pypi.python.org/pypi/PyMarvel>`__.


Basic Usage
-----------

Create a Marvel instance using your public and private api keys:

    >>> from marvel.marvel import Marvel
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


Response Anatomy
----------------

Requesting a resource returns a DataWrapper, which containers information about the the success of response. The ``data`` property of a DataWrapper is a DataContainer, which contains information about the set of resources returned.  The ``results`` property of a DataContainer is a List of Resources (Character, Comic, Event, etc).

.. note::

   The ``results`` property returns a List, even if only one item is returned.  You can use ``result`` property to retrieve the first (or only) item in the list.  This is useful for methods like ``get_comic(some_comic_id)`` where only only Comic is expected.  ``result`` is equivalent to ``results[0]``.

::

    >>> m = Marvel(public_key, private_key)
    >>> character_data_wrapper = m.get_characters(limit="10", offset="700")
    >>> print(character_data_wrapper)
    <marvel.character.CharacterDataWrapper object>
    >>> print(character_data_wrapper.data)
    <marvel.character.CharacterDataContainer object>
    >>> print(character_data_wrapper.data.results[0])
    <marvel.character.Character object>

The json response maps like this::

    {                                                     __ 
    "code": 200,                                            |
    "status": "Ok",                                         |---- CharacterDataWrapper
    "etag": "e59a70a964ab45cc40948dcd3fb7faa0783bcae7",     |
    "data":                                               __|
        {                                                 __          \/
        "offset": 700,                                      |
        "limit": 10,                                        |
        "total": 1402,                                      |---- CharacterDataContainer
        "count": 10,                                        |
        "results": [                                      __|
            {                                             __          \/
            "id": 1017477,                                  |
            "name": "Magneto (X-Men: Battle of the Atom)",  |---- Character
            "description": "",                              |
            "modified": "2014-01-15T19:43:09-0500",       __|
            ...

Related Resources
-----------------

Find Stan Lee's comics:

    >>> stan_lee = m.get_creator(30).data.result
    >>> comics = stan_lee.get_comics()

You can chain methods into one line:

    >>> comics = m.get_creator(30).data.result.get_comics()

or even:

    >>> events = self.m.get_series(characters="1009718").data.result.get_characters().data.result.get_comics().data.results.get_creators().data.result.get_events()

would be the equivalent to calling::

    http://gateway.marvel.com/v1/public/series?characters=100971
    http://gateway.marvel.com/v1/public/series/15276/characters
    http://gateway.marvel.com/v1/public/characters/1009351/comics
    http://gateway.marvel.com/v1/public/comics/50372/creators
    http://gateway.marvel.com/v1/public/creators/4600/events
    

Pagination
----------
::

    >>> xmen = m.get_single_series(403).data.result.get_characters(limit=5)
    >>> for xm in xmen.data.results:
    ...     print xm.name
    
    Archangel
    Banshee
    Beast
    Bishop
    Black Panther
    
    >>> more_xmen = xmen.next()
    >>> for xm in more_xmen.data.results:
    ...     print xm.name
    
    Cable
    Cannonball
    Colossus
    Cyclops
    Emma Frost




Contributing
------------

Clone the repo at `http://github.com/gpennington/PyMarvel <http://github.com/gpennington/PyMarvel>`__.

Feel free to log issues in Github or, better yet, submit a Pull Request against the ``develop`` branch.

Licensing
---------

PyMarvel is distributed under the MIT License.
    
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

