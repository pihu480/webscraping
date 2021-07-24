from bs4 import BeautifulSoup
import requests
import json

def scrao_top_list():
    url="https://webscraper.io/test-sites"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    trs = soup.find_all('h2')
    LIST=[]
    number=0
    for i in trs:
        number=number+1
        Ecomerce_name =i.find("a").get_text()
        Ecomerse_url =i .find("a") ["href"]
        details={"position":number,"name":Ecomerce_name,"link":Ecomerse_url}
        LIST.append(details)
    with open("p_data.json","w") as f:
        json.dump(LIST,f,indent=4)
    return LIST
scrao_top_list()


    