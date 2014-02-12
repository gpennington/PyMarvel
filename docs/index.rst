PyMarvel
========

Python wrapper for the Marvel API

.. toctree::
    :maxdepth: 3

    index    
    reference/marvel
    reference/core
    reference/character

   

How's it work?
--------------

Create a Marvel instance using your public and private api keys::

   from marvel.marvel import Marvel
   
   m = Marvel("abc123...", "def456...")

And use it to retrieve information about ::
    
    characters = m.get_characters(orderBy="name,-modified", limit="10", offset="15")
    for character in characters.data.results:
        print character.name
        print character.description


Documentation
-------------

Read the full `documentation <https://readthedocs.org/projects/PyMarvel/>`__.


Installation
------------
Use pip::

    pip install PyMarvel

or::

    easy_install PyMarvel

`Python Package Index <https://pypi.python.org/pypi/PyMarvel>`__.

Contributing
------------

Clone the repo at `http://github.com/gpennington/PyMarvel <http://github.com/gpennington/PyMarvel>`__.

Feel free to log issues in Github or, better yet submit a Pull Request against the ``develop`` branch.

Licensing
---------

PyMarvel is distributed under the MIT License.
    
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

