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
		print person_info['name'], person_info['dob']
	


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