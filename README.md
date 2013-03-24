islendingabok: Library for Islendingabok API
============================================

islendingabok is a [WTFPL](http://www.wtfpl.net/about/) Licensed client library for [Islendingabok](http://islendingabok.is/) API ([official documentation](http://islendingaapp.is/api/)), written in Python. 


The API is supposed to return json but most of the time it does not (e.g. the keys are not double quoted, missing commas between list items, stray double quotes, etc.). This results in an unreliable API which this client library tries its best to fix. However, some errors still need to be fixed on the server end.

All endpoints have been implemented, except the 'whois' endpoint, which is still a mystery and we haven't figured out how it works exactly. We've tried using the session id as well as the session user id as 'stranger' but neither gives a usable individual's id of the stranger.


Example
-------

	>>> from islendingabok import IslendingabokAPI
	>>> username = "your_username"
	>>> password = "your password"
	>>> 
	>>> api = IslendingabokAPI(username, password)
	>>> 
	>>> user_info = api.me()
	>>> print user_info['name']
	Ólafur Ragnar Grímsson
	>>> 
	>>> results = api.find(u'Vigdís Finnbogadóttir')
	>>> for person_info in results:
	...     print person_info['name'], person_info['dob']
	... 
	Vigdís Finnbogadóttir 19300415
	Vigdís Finnbogadóttir 19830617
	Vigdís Guðrún Finnbogadóttir 19220825
	Kristjana Vigdís Finnbogadóttir Arndal 19390607


Installation
------------

To install the required packages to use this library:

	pip install -r requirements.txt


Authors
-------
Stefanía Bjarney Ólafsdóttir and Jóhann Þorvaldur Bergþórsson.

