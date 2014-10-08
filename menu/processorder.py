import codecs
from datetime import datetime
from random import randint
import math
def menu_generate(station_selection):
	nameofjoint=["SRK da dhaba","Sallu ki eatery","Saif food","Akshay ke pakwan","Is baar Narendra Modi Sarkar","Dev Anand's classic","Aamir's joint"]
	avgorder=[120,100,150,180,100,200,140]
	minorder=[100,110,120,140,130,90,150]
	jain=['Y','N','Y','N','Y','N','Y']
	fi=codecs.open('stationlist','r',encoding='utf-8')
	f=fi.read()
	fi.close()
	f=f.split("\n")
	a=str(datetime.now())
	#print a
	a=a.split(" ")[1]
	a=a.split(":")[0]
	a=float(a)
	a=math.floor(a)
	#print a
	status="lunch"
	if a>10 and a <=16 :
		status="lunch"
	elif a > 16 and a<23:
		status="dinner"
	else:
		status="Nothing available right now,please try later"
	input_=station_selection
	input_=input_.lower()
	stationfound="yes"
	name=''
	desc='NA'
	price=''
	type_dish=''
	menu_list=[]
	for index2,i in enumerate(f):
		if index2!=len(f)-1:
			temp=i.split(',')
			code=temp[1]
			name=''
			type='north'
			if code==input_:
				type=temp[2]
				name=temp[0]
				if type=='north':
					gi=codecs.open("menu.csv","r",encoding="utf-8")
					g=gi.read()
					gi.close()
					g=g.replace('"','')
					g=g.split("\n")
					for index,i in enumerate(g):
						if index!=len(g)-1:
							i=i.split(",")
							name=i[0]
							desc='NA'
							if i[1]=='':
								desc='NA'
							else:
								desc=i[1]
							price=i[3]
							type_dish=i[2]
							#print(name + desc + price + type_dish + " "+nameofjoint[randint(0,6)]+str(avgorder[randint(0,6)])+str(minorder[randint(0,6)])+jain[randint(0,6)])
							menu_list.append((name,desc,price,type_dish))
				elif type=='south':
					gi=codecs.open("southindianmenu.csv","r",encoding="utf-8")
					g=gi.read()
					gi.close()
					g=g.replace('"','')
					g=g.split("\n")
					for index,i in enumerate(g):
						if index!=len(g)-1:
							i=i.split(",")
							name=i[0]
							desc='NA'
							if i[1]=='':
								desc='NA'
							else:
								desc=i[1]
							price=i[3]
							type_dish=i[2]
							#print(name + desc + price + type_dish + " "+nameofjoint[randint(0,6)]+str(avgorder[randint(0,6)])+str(minorder[randint(0,6)])+jain[randint(0,6)])
							menu_list.append((name,desc,price,type_dish))
				elif type=='west':
					gi=codecs.open("westmenu.csv","r",encoding="utf-8")
					g=gi.read()
					gi.close()
					g=g.replace('"','')
					g=g.split("\n")
					for index,i in enumerate(g):
						if index!=len(g)-1:
							i=i.split(",")
							name=i[0]
							desc='NA'
							if i[1]=='':
								desc='NA'
							else:
								desc=i[1]
							price=i[3]
							type_dish=i[2]
							#print(name + desc + price + type_dish + " "+nameofjoint[randint(0,6)]+str(avgorder[randint(0,6)])+str(minorder[randint(0,6)])+jain[randint(0,6)])
							menu_list.append((name,desc,price,type_dish))
				elif type=='east':
					gi=codecs.open("eastmenu.csv","r",encoding="utf-8")
					g=gi.read()
					gi.close()
					g=g.replace('"','')
					g=g.split("\n")
					for index,i in enumerate(g):
						if index!=len(g)-1:
							i=i.split(",")
							name=i[0]
							desc='NA'
							if i[1]=='':
								desc='NA'
							else:
								desc=i[1]
							price=i[3]
							type_dish=i[2]
							#print(name + desc + price + type_dish + " "+nameofjoint[randint(0,6)]+str(avgorder[randint(0,6)])+str(minorder[randint(0,6)])+jain[randint(0,6)])
							menu_list.append((name,desc,price,type_dish))
				#else:
					#print "Sorry,we don't serve at this station yet. Please come back later!"
		else:
			stationfound="no"
	return status,nameofjoint[randint(0,6)],avgorder[randint(0,6)],minorder[randint(0,6)],jain[randint(0,6)],menu_list
#a,b,c,d,e,f,g=menu_generate()
#print g
