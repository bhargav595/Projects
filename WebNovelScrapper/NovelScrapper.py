from tkinter import W
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        churl=self.site
        CHhtml = requests.get(churl).content
        parser = "html.parser"
        CHsoup = BeautifulSoup(CHhtml, parser)
        table = CHsoup.findAll("div", attrs={'class' : "post-body entry-content float-container"})
        paragraph = []
        chtext = ""
        for x in table:
                paragraph.append(x.find("p").text)
                chtext= x.find("p").text
        #print(chtext)
        #Storing the data in a file 
        file_name= CHsoup.title.text +".txt"
        with open(file_name, W, encoding="utf-8") as f:
            f.write(chtext)
        
novelhome = "https://www.koreanmtl.online/p/carnivorous-hunter.html"
result = requests.get(novelhome)
#print(result.status_code)
html = result.content
parser = "html.parser"
soup = BeautifulSoup(html, parser)
links = soup.find_all("a")
url=[]
for tag in links:
    if "CH" in tag.text:
        url.append(tag.attrs['href'])
chcnt=1
for churl in url:
        if chcnt==4:
            break
        else:
            Scraper(churl.strip()).scrape()
            chcnt+=1
