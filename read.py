'''
This method is supposed to read the csv
'''
import csv
import requests

with open ('input.csv', newline='') as csvfile: 
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader: 
		print(', '.join(row))

proj_name = row[0]
form_name = row[1]
# url = row[2]

from datetime import datetime
now = datetime.now() # current date and time
ofname_date = now.strftime("%Y.%m.%d_%H%M") # e.g.: '2022.08.11_1229'


r = requests.get(row[2])
open(ofname_date+"_"+proj_name+" -"+form_name+".json", "wb").write(r.content)

