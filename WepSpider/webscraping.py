import requests
from bs4 import BeautifulSoup

url="http://www.ntnu.no/studier/emner/TDT4186/2015#tab=timeplan"
url2="http://folk.ntnu.no/mahamudh/V%C3%A5r2015/REACT%20SYS/table.html"
r= requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

#links= soup.find_all("a")

g_data=soup.find_all("div",{"id":"timeplan"})
item_list=[]
#print g_data
for item in g_data:
    print item.contents[1][0].text



