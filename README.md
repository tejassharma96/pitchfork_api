# pitchfork_api
An unofficial python API for [pitchfork.com](http://www.pitchfork.com) reviews. A maintained version of @michalczaplinski's pitchfork package.

Apologies for the confusing naming - pypi doesn't allow the use of underscores in package names, while python doesn't allow dashes in module names. As a result, the package name is `pitchfork-api`, but it is `pitchfork_api` everywhere else.


[![Build Status](https://travis-ci.org/tejassharma96/pitchfork_api.svg?branch=master)]()
[![PyPI version](https://img.shields.io/pypi/v/pitchfork-api.svg)](https://pypi.python.org/pypi/pitchfork-api/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pitchfork-api.svg?maxAge=2592000)]()
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)


Installation
------------

You can get it from the [python package index](https://pypi.python.org/pypi):

```sh
pip install pitchfork-api
```

You can also clone the repository, but note that ``pitchfork_api`` depends on ``beautifulsoup4`` for HTML parsing so you first have to install ``beautifulsoup4`` yourself:

```sh
git clone https://github.com/tejassharma96/pitchfork_api.git
cd pitchfork_api
pip install -r requirements.txt
```


Usage
-----

```python
>> import pitchfork_api

>> p = pitchfork_api.search('kanye west', 'my beautiful') # the title is autocompleted
>> p.album() # the full album title
u'My Beautiful Dark Twisted Fantasy'

>> p.label()
u'Def Jam / Roc-A-Fella'

>> p.editorial()[:100] # get the first 100 characters of the review.
u"Kanye West's 35-minute super-video,\xa0Runaway, peaks with a parade. Fireworks flash while red hoods ma"

# the link to the album cover image
>> p.cover()
'http://cdn4.pitchfork.com/albums/15935/homepage_large.831179e9.jpg'

>> p.score()
10.0
```

Tests
-----

You can run the basic tests located in the ``tests`` directory with:
```sh
$ cd path/to/tests
$ python -m unittest discover
```

License
-------
MIT


Contributions
-------------
If you want to add a new feature, suggest improvement or whatnot you're welcome to message me or send a pull request!
