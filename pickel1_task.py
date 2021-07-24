from bs4 import BeautifulSoup
import requests
import json

def scraop_top_list():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    age=requests.get(url)
    soup1=BeautifulSoup(age.text,"html.parser")
    main_div1=soup1.find("div",class_="_1gX7").span.get_text()
    pihu=main_div1.split()
    b=int(pihu[1])
    a=b//32+1
    list=[]
    # print(a)
    p=1
    while p<=a:
        api="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(p)
        page=requests.get(api)
        soup=BeautifulSoup(page.text,"html.parser")
        main_div=soup.find("div",class_="_3RA-")
        # print(main_div)
        pickel_name=main_div.find_all("div",class_="UGUy")
        # print(pickel_name)
        pickel_ret=main_div.find_all("div",class_="_1kMS")
        # print(pickel_ret)
        pickel_urls=main_div.find_all("div",class_="_3WhJ") 
        # printckel_urls=main_div.find_all("div",class_="_3WhJ")
        # print(pickel_urls)
        i=1
        while i<len(pickel_name):
            pickel_name1=pickel_name[i].get_text( )
            # print(pickel_name1)
            pickel_ret2= pickel_ret[i].span.get_text()
            # print(pickel_ret2)
            pickel_urls3="https://paytmmall.com"+pickel_urls[i].a['href']
            details={"position":i,"name":pickel_name1,"price":pickel_ret2,"link":pickel_urls3}
            # print(pickel_urls3)
            list.append(details.copy())
            i=i+1
        p=p+1
    with open("pickel1_data.json","w") as f:
        json.dump(list,f,indent=4)
    return list
scraop_top_list()