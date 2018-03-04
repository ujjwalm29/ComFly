
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/ujjwal/chromedriver") 

driver.get('https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_06-03-2018?contains=false&remove=')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html_page = driver.page_source
driver.quit()

soup=BeautifulSoup(html_page,"html.parser")
tags=soup('span')
c=soup.find_all("span",{"class":"block logo_name hidden-xs visible-stb light_gray flt_number_less600 ng-binding ng-scope"}) #flNumber
d=soup.find_all("span",{"class":"num ng-binding"}) #price

handle=open('random.txt','w')

for i in c:
	handle.write("%s\n" % i.contents)
for i in d:
	handle.write("%s\n" % i.contents)

handle.close()
	