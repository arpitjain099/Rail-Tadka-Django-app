import pycurl
import codecs
from bs4 import BeautifulSoup

def route(trainnumber):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, "http://runningstatus.in/status/"+str(trainnumber))
	#http://runningstatus.in/status/12045-yesterday
	#http://runningstatus.in/status/12015
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	import StringIO
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	#print b.getvalue()
	html_doc=b.getvalue()
	html_doc2=html_doc
	soup = BeautifulSoup(html_doc)
	#print(soup.prettify())
	#mydivs = soup.findAll("div", { "class" : "runningstatus-widget-content" })
	#print mydivs
	#print soup.find_all("div", class_="runningstatus-widget-title")
	a= soup.find_all("table")
	#print len(a)
	temp_dict=[]
	for i in a:
		#print i
		i=str(i)
		i=i.split("<tr>")
		for index,station in enumerate(i):
			if index>1 and index<len(i)-2:

				#print station
				name=""
				sc_arrival=""
				sc_departure=""
				#act_arrival_departure=""
				status='NA'
				delay='NA'
			
				station=station.replace(' colspan="2"',"")
				station=station.replace('</tbody>\n<tfoot>\n',"")
				#station=station.replace("</tr>","")
				#station=station.replace('<td colspan="2">','')
				#print station
				station=station.split("<td>")
				for index2,t in enumerate(station):
					#t=t.replace("E.T.A.:","")
					#print t+"reall?"
				
					if index2==1:
						t=t.replace("</td>\n","")
						name=str(t)
					elif index2==2:
						t=t.replace("</td>\n","")
						sc_arrival=t
					elif index2==3:
						t=t.replace("</td>","")
						sc_departure=t
					#elif index2==4:
					#	t=t.replace("</td>\n</tr> ","")
					
					#	act_arrival_departure=t
					elif index2==5:
						if t!='':
							#print t
							t=t.split(" / ")
							t[0]=t[0].replace('<font color="green">','')
							t[0]=t[0].replace('</font>','')
							t[1]=t[1].replace('<font color="green">','')
							t[1]=t[1].replace('</font></td>\n</tr>','')
							t[0]=t[0].replace('\n','')
							t[0]=t[0].replace('<b>','')
							t[0]=t[0].replace('</b>','')
							t[1]=t[1].replace('\n','')
							t[1]=t[1].replace('<font color="red">','')
							status=t[0]
							delay=t[1]
				temp_dict.append((name,sc_arrival,sc_departure,status,delay))
	#print temp_dict
	html_doc2=html_doc2.split('<span><h1 align="center">')
	html_doc2=html_doc2[1]
	html_doc2=html_doc2.split("\n")
	html_doc2=html_doc2[0]
	html_doc2=html_doc2.replace(" Running Train Status</h1></span>","")
	#print "Name of train is "+html_doc2
	return temp_dict#,"Name of train is "+html_doc2
def trainname(trainnumber):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, "http://runningstatus.in/status/"+str(trainnumber))
	#http://runningstatus.in/status/12045-yesterday
	#http://runningstatus.in/status/12015
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])
	import StringIO
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	#print b.getvalue()
	html_doc=b.getvalue()
	html_doc2=html_doc
	soup = BeautifulSoup(html_doc)
	#print(soup.prettify())
	#mydivs = soup.findAll("div", { "class" : "runningstatus-widget-content" })
	#print mydivs
	#print soup.find_all("div", class_="runningstatus-widget-title")
	a= soup.find_all("table")
	#print len(a)
	temp_dict=[]
	for i in a:
		#print i
		i=str(i)
		i=i.split("<tr>")
		for index,station in enumerate(i):
			if index>1 and index<len(i)-2:

				#print station
				name=""
				sc_arrival=""
				sc_departure=""
				#act_arrival_departure=""
				status='NA'
				delay='NA'
			
				station=station.replace(' colspan="2"',"")
				station=station.replace('</tbody>\n<tfoot>\n',"")
				#station=station.replace("</tr>","")
				#station=station.replace('<td colspan="2">','')
				#print station
				station=station.split("<td>")
				for index2,t in enumerate(station):
					#t=t.replace("E.T.A.:","")
					#print t+"reall?"
				
					if index2==1:
						t=t.replace("</td>\n","")
						name=str(t)
					elif index2==2:
						t=t.replace("</td>\n","")
						sc_arrival=t
					elif index2==3:
						t=t.replace("</td>","")
						sc_departure=t
					#elif index2==4:
					#	t=t.replace("</td>\n</tr> ","")
					
					#	act_arrival_departure=t
					elif index2==5:
						if t!='':
							#print t
							t=t.split(" / ")
							t[0]=t[0].replace('<font color="green">','')
							t[0]=t[0].replace('</font>','')
							t[1]=t[1].replace('<font color="green">','')
							t[1]=t[1].replace('</font></td>\n</tr>','')
							t[0]=t[0].replace('\n','')
							t[0]=t[0].replace('<b>','')
							t[0]=t[0].replace('</b>','')
							t[1]=t[1].replace('\n','')
							t[1]=t[1].replace('<font color="red">','')
							status=t[0]
							delay=t[1]
				temp_dict.append((name,sc_arrival,sc_departure,status,delay))
	#print temp_dict
	html_doc2=html_doc2.split('<span><h1 align="center">')
	html_doc2=html_doc2[1]
	html_doc2=html_doc2.split("\n")
	html_doc2=html_doc2[0]
	html_doc2=html_doc2.replace(" Running Train Status</h1></span>","")
	#print "Name of train is "+html_doc2
	return "Name of train is "+html_doc2
print route(14153)
print trainname(14153)
