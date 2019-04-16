#!/usr/bin/python3

import urllib.request
import json

majortom = urllib.request.urlopen('http://api.open-notify.org/astros.json')

helmetson = majortom.read().decode('utf-8')

groundctrl = json.loads(helmetson)

print(groundctrl)

print(type(groundctrl))

input("Press Enter to continue")
