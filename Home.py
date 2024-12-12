from flet import *
from flet_route import Params, Basket
import requests
import json
from requests.exceptions import RequestException
from datetime import date, datetime
import datetime

session = requests.Session()
json_data = {}


data = {
    'login': '191-641-188 74',
    'password': '1245cv89#0',
    'submit': 'submit',
    'returnTo': 'https://one.astrobl.ru'
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=5B60503D09EAFBDB8667FEE2563B6D86; PHPSESSID=1e388935b7b68880c110e2b76bc25f2e',
    'Referer': 'https://one.astrobl.ru/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

link = "https://passport.astrobl.ru/auth/login"
# jsonlink = "https://one.astrobl.ru/edv/index/diary/B8D64CF3C9BF8CBA6872B85CAFFBB2BB?date=02.12.2024"


def home(page:Page,params:Params,basket:Basket):

    input_login = TextField(label="СНИЛС", value="191-641-188 78")
    input_pass = TextField(label="пароль", value="1245cv89#0") 

    # data = {
    #     'login': f'{input_login.value}', # 191-641-188 78
    #     'password': f'{input_pass.value}', # 1245cv89#0
    #     'submit': 'submit',
    #     'returnTo': 'https://one.astrobl.ru'
    # }

    def login_btn(e):
        
        if input_login.value != "" and input_pass.value != "":
            response = session.post(link, data=data, headers=headers)
            # received_cookies = response.cookies

            # for cookie in received_cookies:
            #     print(f"{cookie.name}:{cookie.value}")

            # print(response)
            profile_info = "https://passport.astrobl.ru/auth/user"
            profile_responce = session.get(profile_info,headers=headers).text

            # print(profile_responce)
            # #Вход успешно воспроизведен и мы сохраняем страницу в html файл
            # with open("hh_success.html","w",encoding="utf-8") as f:
            #     f.write(profile_responce)
            # id_ses = "8EC3CC7644995D6F4F215A7FEB80686E"
            # date = "02.12.2024"
            # link2 = f"https://one.astrobl.ru/edv/index/diary/{id_ses}?date={date}" 
            #



            today = datetime.datetime.today()
            mon = today - datetime.timedelta(datetime.datetime.weekday(today))
            mon2=mon.strftime('%d.%m.%Y')
            link3=f"https://one.astrobl.ru/edv/index/diary/B8D64CF3C9BF8CBA6872B85CAFFBB2BB?date={mon2}"

            try:
                resp_dn = session.get(link3, data=data, headers=headers)
                resp_dn.raise_for_status()
                global json_data
                json_data = resp_dn.json()
            except RequestException as e:
                print(f"Проблема с выполнением HTTP-запроса:{e}")    
            except json.JSONDecodeError:
                print("Не удалось декодировать JSON. Пожалуйста, попробуйте ещё раз.")



        # print(json_data) 
        # global js
        # js=json_data

        if response.ok == True:
            page.session.set("session", response)
            page.go("/menupage")
            page.update()
        #else:
            # print(response.ok)
        

    return View("/",[
        AppBar(
            title=Text("one.astrobl.ru"),
            center_title=True,
            bgcolor="#63aae1",
            ),
        # Container(
        #     content=[
        #               
        #     ]
        # ),
        Column([
            Text("Дневник",size=30), 
            input_login,
            input_pass,
            ElevatedButton("Вход", on_click=login_btn) 
            ],
            horizontal_alignment = CrossAxisAlignment.CENTER
        ) 
    ],
    
    vertical_alignment=MainAxisAlignment.CENTER,
    
    # foreground_decoration=BoxDecoration(
    #     image=DecorationImage(
    #         src="icons/groovepaper.png",
    #         repeat=ImageRepeat.REPEAT
    #         )) 
    )