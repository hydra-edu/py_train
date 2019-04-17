# python3 -m pip install pyexcel
# python3 -m pip install pyexcel-xls

myexcelvalue = { }

## dump excel spreadsheet to a record format friendly to python
excelrecords = pyexcel.iget_records(file_name="portsservice.xls")

for x in excelrecords: 
	totalsocket = x['ip'] + ":" + str(x['port'])
	myexcelval.update({x['service']:totalsocket])
	## adds a new IP and driver key:value pair to our dictionary

print(myexcelval)
