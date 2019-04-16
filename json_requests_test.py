#!/usr/bin/python3
"""this code tests the results module's usage parsing json"""
import requests

def main():
	"""main function"""
	majortom = requests.get('http://api.open-notify.org/astros.json')
	helmetson = majortom.json()
	for astro in helmetson['people']:
		print(astro['name'])

main()
