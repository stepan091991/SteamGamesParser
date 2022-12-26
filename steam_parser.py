import requests
from bs4 import BeautifulSoup
teg = {"Гонки":"racing","Экшен":"action","Головоломка":"puzzle_matching","Симулятор":"simulation","Аниме":"anime","Города":"strategy_cities_settlements","Спортивные":"sports","Новелла":"visual_novel","Ролевые":"rpg"}
print("Гонки,Экшен,Головоломка,Симулятор,Аниме.Города,Спортивные,Новелла,Ролевые")
i_ = input("Выберите жанр:")
for i in teg:
    if i == i_:
        html =  requests.get("https://store.steampowered.com/category/"+teg[i])
        soup = BeautifulSoup(html.text, 'lxml')
        text = soup.find("div",id="application_config")
        text1 = text.prettify().split("data-ch_main_list_data=")[1]
        text1 = text1.split("data-ch_newshub=")[0]
        text1 = text1.strip("'")
        text1 = text1.replace("}","}|")
        text1 = text1.replace('"apps":[]}',"")
        text1 = text1.replace('{"id":"featured",',"")
        text1 = text1.split("|")
        prefix = 0
        for i in text1:
            i = i.replace(",","",1)
            i = i.replace("[", "")
            i = i.replace("{", "")
            i = i.replace("}", "")
            i = i.split(",")
            if len(i) > 2:
                i.pop(0)
            if len(i) > 1:
                prefix += 1
                answer = requests.get("https://store.steampowered.com/api/appdetails?appids="+i[1].replace('"id":',""))
                answer = answer.text.split('"name":')[1]
                answer = answer.split(',"dlc"')[0]
                answer = answer.split(',"detailed_description"')[0]
                answer = answer.split(',"controller_support"')[0]
                answer = answer.replace(',"steam_appid"'," ID")
                answer = answer.replace(',"required_age"', " Ограничение")
                answer = answer.replace(',"is_free":false', "+ Платная")
                answer = answer.replace(',"is_free":true', "+ Бесплатная")
                print(str(prefix)+"|"+answer)