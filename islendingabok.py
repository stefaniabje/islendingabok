#!/usr/bin/env python
#encoding: utf-8

import requests


class APIError(Exception):
	pass


class ClientError(Exception):
	pass


class IslendingabokAPI(object):
	API_PATH = "http://www.islendingabok.is/ib_app/"

	def __init__(self, username, password):
		self.username = username
		self.password = password
		
		self.session = requests.Session()
		self.session_id = None
		self.session_user_id = None
		
		self.login()

	def login(self):
		login_response = self.api_response("login", user=self.username, pwd=self.password)
		self.session_id, self.session_user_id = login_response.content.split(",")

	def me(self):
		return self.person(self.session_user_id)

	def person(self, person_id=None):
		return self.call_api("get", id=person_id)

	def find(self, name=None, birth_year=None, birth_month=None, birth_day=None):
		if name:
			name = name.encode("iso-8859-1")
			
		date_of_birth = self._parse_date_of_birth(name, birth_year, birth_month, birth_day)

		return self.call_api("find", name=name, dob=date_of_birth)

	def _parse_date_of_birth(self, name=None, birth_year=None, birth_month=None, birth_day=None):
		date_of_birth = None

		seperator = "." if name else ""

		if not name and (not birth_day or not birth_month):
			raise ClientError("Missing part of date of birth.")

		if birth_year:
			date_of_birth = str(birth_year)

			if birth_month:
				date_of_birth = ("%02d" % birth_month) + seperator + date_of_birth

				if birth_day:
					date_of_birth = ("%02d" % birth_day) + seperator + date_of_birth					

		return date_of_birth

	def whois(self, stranger_session_id):
		response = self.api_response("whois", session=self.session_id, stranger=stranger_session_id)
		return response.text

	def __getattr__(self, attr_name):
		if attr_name in ["get", "siblings", "children", "mates", "ancestors", "trace"]:
			return self._build_endpoint(attr_name)
		else:
			return super(IslendingabokAPI, self).__getattr__(attr_name)

	def _build_endpoint(self, endpoint):
		def _endpoint(person_id=None):
			if person_id is None:
				person_id = self.session_user_id

			return self.call_api(endpoint, id=person_id)

		return _endpoint

	def call_api(self, endpoint, **parameters):
		parameters["session"] = self.session_id

		response = self.api_response(endpoint, **parameters)

		try:
			return response.json()
		except ValueError:
			raise APIError(response.text.encode('utf-8'))


	def api_response(self, endpoint, **parameters):
		return self.session.get(self.API_PATH + endpoint, 
			params=parameters)



# /* This program is free software. It comes without any warranty, to
#      * the extent permitted by applicable law. You can redistribute it
#      * and/or modify it under the terms of the Do What The Fuck You Want
#      * To Public License, Version 2, as published by Sam Hocevar. See
#      * http://www.wtfpl.net/ for more details. */

