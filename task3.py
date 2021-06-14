import json
from task1 import scrao_top_list
from task2 import group_by_year
scarpped=scrao_top_list()
d=group_by_year(scarpped)
def group_by_decade(movies):
    moviedec={}
    list1=[]
    for i in movies:
        mod= i%10
        decade= i-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10= i+ 9
        for x in movies:
            if x <=dec10 and x>=i:
                for p in movies[x]:
                    moviedec[i].append(p)
                    with open("movies_data.json","w") as f:
                        json.dump(moviedec,f,indent=4)
    return(moviedec)
group_by_decade(d)
