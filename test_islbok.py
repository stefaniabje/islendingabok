#!/usr/bin/env python
#encoding: utf-8


from islendingabok import IslendingabokAPI
import argparse


def main(username, password):
	api = IslendingabokAPI(username, password)
	user_info = api.me()
	
	print user_info['name']

	results = api.find(u'Vigdís Finnbogadóttir')

	for person_info in results:
		print person_info['name'], person_info['dob'], person_info['id']

	oli_stef = api.find(u'Ólafur Indriði Stefánsson', 1973, 07)
	
	oli_stef_id = oli_stef[0]["id"]

	siblings_of_oli_stef = api.siblings(oli_stef_id)

	for sibling in siblings_of_oli_stef:
		print sibling["name"]


def parse_arguments():
	parser = argparse.ArgumentParser(description='Connects to Islendingabok and accesses user data.')
	parser.add_argument('username', 
		help='username on Islendingabok')
	parser.add_argument('password',
	    help='password on Islendingabok')

	return parser.parse_args()


if __name__ == '__main__':
	args = parse_arguments()
	print args.username, args.password

	main(args.username, args.password)