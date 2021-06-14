import json
from task1 import scrao_top_list
scarpped=scrao_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        name=i
        year=i["year"]
        for x in movie_dict:
            if str (x) == str(year):
                movie_dict[x].append(name)
                with open("movie_data.json","w") as f:
                    json.dump(movie_dict,f,indent=4)
    return (movie_dict)
group_by_year(scarpped)

