
from bs4 import BeautifulSoup
import requests
import json

def scraop_top_list():
    
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    main_div=soup.find("div",class_="_3RA-")
    # print(main_div)
    pickel_name=main_div.find_all("div",class_="UGUy")
    # print(pickel_name)
    pickel_ret=main_div.find_all("div",class_="_1kMS")
    # print(pickel_ret)
    pickel_urls=main_div.find_all("div",class_="_3WhJ")
    # print(pickel_urls)
    i=0
    list=[]
    while i<len(pickel_name):
        pickel_name1=pickel_name[i].get_text()
        # print(pickel_name1)
        pickel_ret2= pickel_ret[i].span.get_text()
        # print(pickel_ret2)
        pickel_urls3="https://paytmmall.com"+pickel_urls[i].a['href']
        print(pickel_urls3)
        i=i+1
        details={"position":i,"name":pickel_name1,"price":pickel_ret2,"link":pickel_urls3}
        list.append(details)
    with open("pickel_data.json","w") as f:
        json.dump(list,f,indent=4)
    return list
scraop_top_list()