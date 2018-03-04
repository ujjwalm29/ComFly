import traceback, warnings
from selenium import webdriver
from datetime import datetime

warnings.filterwarnings("ignore")
import time

from flask import Flask,render_template, request
app = Flask(__name__)

cities=['kullu', 'colombo', 'guwahati', 'pondicherry', 'jaipur', 'pantnagar', 'raipur', 'amritsar', 'puttaparthi', 'coimbatore', 'chennai', 'khajuraho', 'dibrugarh', 'tirupati', 'jammu', 'dehradun', 'shillong', 'allahabad', 'cochin', 'dubai', 'gwalior', 'belgaum', 'surat', 'tiruchirapally', 'pathankot', 'madurai', 'hubli', 'sholapur', 'silchar', 'visakhapatnam', 'calicut', 'goa', 'leh', 'udaipur', 'bhopal', 'tezpur', 'shimla', 'bhubaneshwar', 'bangkok', 'port blair', 'porbandar', 'diu', 'vijaywada', 'bangalore', 'pune', 'lucknow', 'mumbai', 'bhuj', 'nanded', 'hyderabad', 'bagdogra', 'agatti island', 'kanpur', 'gorakhpur', 'agartala', 'ujjain', 'kandla', 'dharamshala', 'latur', 'agra', 'ranchi', 'jamnagar', 'lilabari', 'jaisalmer', 'patna', 'chandigarh', 'ludhiana', 'rajkot', 'jabalpur', 'tuticorin', 'ahmedabad', 'vidyanagar', 'gaya', 'indore', 'kolhapur', 'mangalore', 'rajahmundry', 'jamshedpur', 'salem', 'aizawl', 'new delhi', 'varanasi', 'mysore', 'vadodara', 'kolkata', 'dimapur', 'jodhpur', 'satna', 'jorhat', 'nasik', 'trivandrum', 'aurangabad', 'srinagar', 'bhavnagar', 'nagpur', 'rewa', 'bellary', 'imphal']
city_code = {'kullu': 'KUU', 'colombo': 'CMB', 'guwahati': 'GAU', 'pondicherry': 'PNY', 'jaipur': 'JAI', 'pantnagar': 'PGH', 'raipur': 'RPR', 'amritsar': 'ATQ', 'puttaparthi': 'PUT', 'coimbatore': 'CJB', 'chennai': 'MAA', 'khajuraho': 'HJR', 'dibrugarh': 'DIB', 'tirupati': 'TIR', 'jammu': 'IXJ', 'dehradun': 'DED', 'shillong': 'SHL', 'allahabad': 'IXD', 'cochin': 'COK', 'dubai': 'DXB', 'gwalior': 'GWL', 'belgaum': 'IXG', 'surat': 'STV', 'tiruchirapally': 'TRZ', 'pathankot': 'IXP', 'madurai': 'IXM', 'hubli': 'HBX', 'sholapur': 'SSE', 'silchar': 'IXS', 'visakhapatnam': 'VTZ', 'calicut': 'CCJ', 'goa': 'GOI', 'leh': 'IXL', 'udaipur': 'UDR', 'bhopal': 'BHO', 'tezpur': 'TEZ', 'shimla': 'SLV', 'bhubaneshwar': 'BBI', 'bangkok': 'BKK', 'port blair': 'IXZ', 'porbandar': 'PBD', 'diu': 'DIU', 'vijaywada': 'VGA', 'bangalore': 'BLR', 'pune': 'PNQ', 'lucknow': 'LKO', 'mumbai': 'BOM', 'bhuj': 'BHJ', 'nanded': 'NDC', 'hyderabad': 'HYD', 'bagdogra': 'IXB', 'agatti island': 'AGX', 'kanpur': 'KNU', 'gorakhpur': 'GOP', 'agartala': 'IXA', 'ujjain': 'UJJ', 'kandla': 'IXY', 'dharamshala': 'DHM', 'latur': 'LTU', 'agra': 'AGR', 'ranchi': 'IXR', 'jamnagar': 'JGA', 'lilabari': 'IXI', 'jaisalmer': 'JSA', 'patna': 'PAT', 'chandigarh': 'IXC', 'ludhiana': 'LUH', 'rajkot': 'RAJ', 'jabalpur': 'JLR', 'tuticorin': 'TCR', 'ahmedabad': 'AMD', 'vidyanagar': 'VDY', 'gaya': 'GAY', 'indore': 'IDR', 'kolhapur': 'KLH', 'mangalore': 'IXE', 'rajahmundry': 'RJA', 'jamshedpur': 'IXW', 'salem': 'SXV', 'aizawl': 'AJL', 'new delhi': 'DEL', 'varanasi': 'VNS', 'mysore': 'MYQ', 'vadodara': 'BDQ', 'kolkata': 'CCU', 'dimapur': 'DMU', 'jodhpur': 'JDH', 'satna': 'TNI', 'jorhat': 'JRH', 'nasik': 'ISK', 'trivandrum': 'TRV', 'aurangabad': 'IXU', 'srinagar': 'SXR', 'bhavnagar': 'BHU', 'nagpur': 'NAG', 'rewa': 'REW', 'bellary': 'BEP', 'imphal': 'IMF'}
@app.route('/')
def hello_world():
	return render_template('home.html',cities=cities)
@app.route('/home', methods=['POST'])
def main():
	lit = request.form['inputFrom']
	to = request.form['inputTo']
	code1 = city_code[lit]
	code2 = city_code[to]
	departDate = request.form['inputDepart']
	noOfPassengers = request.form['inputPassengers']
	import re
	from selenium import webdriver
	print(noOfPassengers)
	driver = webdriver.Chrome(executable_path="/home/ujjwal/chromedriver")
	#driver.set_window_position(-3000, 0)
	print(departDate)
	oldformat = departDate
	datetimeobject = datetime.strptime(oldformat,'%Y-%m-%d')
	newformat = datetimeobject.strftime('%d-%m-%Y')
	newformat2 = datetimeobject.strftime('%d/%m/%Y')
	newformat3 = datetimeobject.strftime('%Y%m%d')
	print(newformat,newformat2)

	url1 = 'https://flight.yatra.com/air-search-ui/dom2/trigger?ADT='+noOfPassengers+'&CHD=0&INF=0&class=Economy&destination='+code2+'&destinationCountry=IN&flexi=0&flight_depart_date='+newformat2+'&noOfSegments=1&origin='+code1+'&originCountry=IN&source=fresco-home&type=O&version=1.15&viewName=normal' 

	driver.get(url1 )


	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	import ssl

	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	#serviceurl='https://www.makemytrip.com/'

	#url='https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_06-03-2018?contains=false&remove='
	html_page_yatra = driver.page_source

	#********************************************************************************
	url2 = 'https://flights.makemytrip.com/makemytrip/search/O/O/E/'+noOfPassengers+'/0/0/S/V0/'+code1+'_'+code2+'_'+newformat+'?contains=false&remove='

	driver.get(url2)
	html_page_mmt = driver.page_source

	driver.quit()

	#********************************************************************************

	soup=BeautifulSoup(html_page_yatra,"html.parser")
	tags=soup('span')
	#a=soup.find_all("span",{"class":"block city_name hidden-xs visible-stb ng-binding"})
	airlin=soup.find_all("small",{"class":"fs-sm gray fl ml5 name carrier-name"})
	dept_tim=soup.find_all("span",{"class":"time-color","ng-bind":"flt.dd"})
	arr_tim=soup.find_all("span",{"class":"time-color","ng-bind":"flt.ad"})
	flt_n=soup.find_all("small",{"class":"fs-10 ltr-gray fl ml5 nowrap"})
	price=soup.find_all("del",{"class":"fs-sm lt-gray block ng-hide"})
	journey=soup.find_all("small",{"class":"fs-10 ltr-gray block stop-tooltip three-dot"})

	tempo=list() #wefe
	finalpric=list() #qwew
	airline=list() 
	dept_time=list()
	arr_time=list()
	flt_no=list()
	finalprice=list()
	journey_type=list()

	#handle=open('random.txt','w')



	for i in airlin:
		#handle.write("%s\n" % i.contents)
		tempo.append(i.contents)
	for i in tempo:
		airline.append(i[0])
	del tempo[:]


	for i in dept_tim:
		#handle.write("%s\n" % i.contents)
		tempo.append(i.contents)
	for i in tempo:
		dept_time.append(i[0])
	del tempo[:]
	#handle.write("******\n")

	for i in arr_tim:
		#handle.write("%s\n" % i.contents)
		tempo.append(i.contents)
	for i in tempo:
		arr_time.append(i[0])
	del tempo[:]
	#handle.write("******\n")


	for i in flt_n:
		#handle.write("%s\n" % i.contents)
		tempo.append(i.contents)
	for i in tempo:
		flt_no.append(i[0])
	del tempo[:]

	yatNo=list()
	for i in flt_no:
		i=i.rstrip()
		var=i.split()
		yatNo.append(var[0]+var[1]+var[2])



	for i in price:
		t=str(i)
		temp=re.findall(r'[0-9][0-9,]+',t)
		finalpric.append(temp)
	finalpric = [v for i, v in enumerate(finalpric) if i % 2 == 0]

	for i in finalpric:
		#handle.write("%s\n" % i)
		tempo.append(i)
	for i in tempo:
		finalprice.append(i[0])

	for i in journey:
		#handle.write("%s\n" % i)
		tempo.append(i.contents)
	for i in tempo:
		journey_type.append(i[0].rstrip())

	#print(airline)
	#print(dept_time)
	#print(arr_time)
	#print(flt_no)
	#print(finalprice)
	#print(journey_type)

	#**************************************************************************************
	print("######################")

	soup=BeautifulSoup(html_page_mmt,"html.parser")
	#tags=soup('span')
	#a=soup.find_all("span",{"class":"block city_name hidden-xs visible-stb ng-binding"})
	#b=soup.find_all("span",{"class":"block timeCa RobotoRegular ng-binding"})
	f_no=soup.find_all("span",{"class":"block logo_name hidden-xs visible-stb light_gray flt_number_less600 ng-binding ng-scope"})
	cost=soup.find_all("span",{"class":"num ng-binding"})

	tempor=list()
	mmt_f_n=list()
	mmt_cost=list()

	for i in f_no:
		#print(i.contents)
		#handle.write("%s\n" % i.contents)
		tempor.append(i.contents)
	for i in tempor:
		mmt_f_n.append(i[0])
	del tempor[:]

	for i in cost:
		#print(i.contents)
		#handle.write("%s\n" % i.contents)
		tempor.append(i.contents)
	for i in tempor:
		mmt_cost.append(i[0])
	del tempor[:]

	#**********************************************IBIBO************************************************

	import urllib.request, urllib.parse, urllib.error
	import json
	url3='http://developer.goibibo.com/api/search/?app_id=9395d693&app_key=e3dd1bc5ccffc93928fbe7d046f168e2&format=json&source='+code1+'&destination='+code2+'&dateofdeparture='+newformat3+'&seatingclass=E&adults=1&children=0&infants=0&counter=100'
	uh = urllib.request.urlopen(url3)
	data = uh.read().decode()
	try:
		js = json.loads(data)
	except:
	    js = None



	#airlin=list()
	ibiNo=list()
	#dept_time=list()
	#arr_time=list()
	ibiboPrice=list()
	#journey_type=list()
	journey_duration=list()
	#journey_through=list()
	#print(json.dumps(js, indent=4))
	temp=js["data"]["onwardflights"]
	for item in temp:
	#	airlin.append(item["airline"])
		ibiNo.append(item["carrierid"]+"-"+item["flightcode"])
	#	dept_time.append(item["deptime"])
	#	arr_time.append(item["arrtime"])
		journey_duration.append(item["duration"])
		ibiboPrice.append(item["fare"]["grossamount"])


	#print(mmt_f_n)
	#print(mmt_cost)
	yatPrice=list()
	finAir=list()
	finName=list()
	finDept=list()
	finArr=list()
	finMmt=list()

	for i,x in zip(mmt_f_n,mmt_cost):
		for j,k,l,m,n,o in zip(yatNo,finalprice,yatNo,airline,dept_time,arr_time):
			if i==j and k!=0:
				yatPrice.append(k)
				finAir.append(l)
				finName.append(m)
				finDept.append(n)
				finArr.append(o)
				finMmt.append(x)
				k=0
				print(k,i)
				break

	newNo = list()
	newName = list()
	ibiPrice = list()
	newDept = list()
	newArr = list()
	dur = list()
	updYat = list()
	updMmt = list()


	for a,b in zip(ibiNo,ibiboPrice):
		for c,d,e,f,g,h,i,j in zip(finAir,yatPrice,finName,finDept,finArr,journey_duration,finMmt,yatPrice):
			if a==c and d!=0:
				newNo.append(a)
				newName.append(e)
				newDept.append(f)
				newArr.append(g)
				ibiPrice.append(b)
				dur.append(h)
				updMmt.append(i)
				updYat.append(j)


	journ1=list()
	journ2=list()

	for v in journey_type:
		v=v.rstrip()
		qar=v.split()
		if len(qar)==1:
			journ2.append(qar[0])
		else:
			journ1.append(qar[0]+qar[1])
		#journey.append(qar[0]+qar[1])
	print(journ1)
	#print(var)

	cheapest = list()

	for i,j,k in zip(updYat,updMmt,ibiPrice):
		qar1=i.split(',')
		temp1=qar1[0]+qar1[1]
		qar2=j.split(',')
		temp2=qar2[0]+qar2[1]
		print(temp1+"   "+temp2)
		if int(temp1)<=int(temp2) and int(temp1)<=k:
			cheapest.append(i)
		elif int(temp2)<=int(temp1) and int(temp2)<=k:
			cheapest.append(j)
		else:
			cheapest.append(k)

	lent = len(newNo)

	if yatPrice:
		return render_template('results.html',airlines=newName,dept_time=newDept,arr_time=newArr,mmt_f_n=newNo,mmt_cost=updMmt,yatPrice=updYat,srcs=code1,dests=code2,cheapest=cheapest,journey_type=journ1,lent=lent,ibiPrice=ibiPrice,dur=dur,url1=url1,url2=url2,url3=url3,newformat=newformat)
	else:
		return 'asdjioashn'
if __name__ == '__main__':
   app.run(debug=True)