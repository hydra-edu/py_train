#!/usr/bin/env python3

##create a dictionary
switch = {'hostname':'sw1','ip':'10.0.1.1','version':'1.2','vendor':'cisco'}

##display a couple parts of the dictionary
#print(switch['hostname'])
#print(switch['ip'])

##request a nonexistent key
#print(switch['lynx'])

##request a nonexistent key with the .get() method
#print("First test - .get()")
#print(switch.get('lynx'))

#print("Second test - .get()")
#print(switch.get('lynx',"KEY ELSEWHERE"))

#print("third test - .get()")
#print(switch.get('version'))

#print("fourth test - .keys()")
#print(switch.keys())

#print("fifth test - .values()")
#print(switch.values())

print("sixth test - .pop()")
switch.pop('version')
print(switch.keys(), switch.values())

print("seventh test - add a new value")
switch['adminlogin']='potatooo'
print(switch.keys(), switch.values())

print("eighth test - add a new value")
switch['password']='qwerty'
print(switch.keys(),switch.values())
