islendingabok: Library for Islendingabok API
============================================

islendingabok is a [WTFPL](http://www.wtfpl.net/about/) Licensed client library for the [Islendingabok](http://islendingabok.is/) API ([official documentation](http://islendingaapp.is/api/)), written in Python. 


All endpoints have been implemented.


Note that when name is specified in 'find' then search can be further defined stepwise: by year, by month and year, and by day, month and year - but when name is not specified in 'find', then searching by date of birth must contain year, month and day of month.


Example
-------

Login with your username and password:

	>>> from islendingabok import IslendingabokAPI
	>>> api = IslendingabokAPI(username, password)
	>>> user_info = api.me()
	>>> print user_info['name']
	Ólafur Ragnar Grímsson

Obtain search results by name and look at the results:

	>>> results = api.find(u'Vigdís Finnbogadóttir')
	>>> for person_info in results:
	...     print person_info['name'], person_info['dob'], person_info['id']
	... 
	Vigdís Finnbogadóttir 19300415 11183155
	Vigdís Finnbogadóttir 19830617 10331225
	Vigdís Guðrún Finnbogadóttir 19220825 2756144
	Kristjana Vigdís Finnbogadóttir Arndal 19390607 10489669

Make your search more detailed:

	>>> oli_stef = api.find(u'Ólafur Indriði Stefánsson', 1973, 07)
	>>> oli_stef_id = oli_stef[0]["id"]
	>>> siblings_of_oli_stef = api.siblings(oli_stef_id)
	>>> for sibling in siblings_of_oli_stef:
	...     print sibling["name"]
	... 
	Guðrún Lilja Tryggvadóttir
	Agnar Björn Tryggvason
	Hildur Jakobína Tryggvadóttir
	Stefanía Stefánsdóttir
	Eggert Stefánsson
	Jón Arnór Stefánsson



Installation
------------

To install the required packages to use this library:

	pip install -r requirements.txt


Authors
-------
Stefanía Bjarney Ólafsdóttir and Jóhann Þorvaldur Bergþórsson.

