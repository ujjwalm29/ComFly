import traceback, warnings
from selenium import webdriver

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
	returnDate = request.form['inputReturn']
	noOfPassengers = request.form['inputPassengers']
	import re
	from selenium import webdriver

	driver = webdriver.Chrome(executable_path="/home/ujjwal/chromedriver") 

	driver.get('https://flight.yatra.com/air-search-ui/dom2/trigger?ADT=1&CHD=0&INF=0&class=Economy&destination=BOM&destinationCountry=IN&flexi=0&flight_depart_date=26/02/2018&noOfSegments=1&origin=DEL&originCountry=IN&source=fresco-home&type=O&version=1.15&viewName=normal')


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

	driver.get('https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_06-03-2018?contains=false&remove=')
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

	tempo=list()
	finalpric=list()
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

	print(airline)
	print(dept_time)
	print(arr_time)
	print(flt_no)
	print(finalprice)
	print(journey_type)

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

	print(mmt_f_n)
	return render_template('hello.html',code1=code1,code2=code2)#'hello.html',lit=lit,to=to,departDate=departDate,returnDate=returnDate,noOfPassengers=noOfPassengers)
if __name__ == '__main__':
   app.run(debug=True)