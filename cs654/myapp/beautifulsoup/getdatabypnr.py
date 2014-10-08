import pycurl
import codecs
import re
import json
from pprint import pprint
from bs4 import BeautifulSoup
import StringIO
def getdatabypnr(pnr):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, "http://pnrdekho.com/api_getPnrStatus.php?pnr="+str(pnr))
	#http://runningstatus.in/status/12045-yesterday
	#http://runningstatus.in/status/12015
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	#print b.getvalue()
	#output=b.getvalue()
	#a=re.search('"trainNo": "',output)
	#print a
	data = json.loads(b.getvalue())#2619574234
	#print data
	if data['passengers']!=[]:
		data['trainJourney']=data['trainJourney'].replace(" ","")
		#print "Train number : "+data['trainNo']
		#print "Journey date : "+data['trainJourney']
		#print "Train name : " + data['trainName']
		#print "Boarded train at : " + data['trainBoard']
		#print "Journey till : "+ data['trainEmbark']
	return data['trainNo']
