from bs4 import BeautifulSoup
import requests
import json


def scrao_top_list():
    url=" https://www.imdb.com/india/top-rated-indian-movies/"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    main_div=soup.find("div",class_="lister")
    tbody= main_div.find("tbody",class_="lister-list")
    trs = tbody.find_all('tr')
    movie_urls=[]
    number=0
    for tr in trs:
        number+=1
        title= tr.find ("td",class_="titleColumn").a.get_text()
        year= tr.find ("td",class_="titleColumn").span.get_text()[1:5]
        year1=int(year)
        imdb_rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        imdb_rating_float = float(imdb_rating)
        link=tr.find ("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        details={"position":number,"name":title,"year":year1,'imbd_rating':imdb_rating_float,'link':movie_link}
        movie_urls.append(details)
        with open("pihu_data.json","w") as f:
            json.dump(movie_urls,f,indent=4) 
    return movie_urls
scrao_top_list()




    
