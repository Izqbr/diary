from flet import * 
from flet_route import Params, Basket
import Home 
from Components import *
from datetime import date, datetime
import datetime
import requests
import json
from requests.exceptions import RequestException


def diarypage(page:Page,params:Params,basket:Basket):
    j=Home.json_data
    # print(f'j=Home.json_data = {id(j)}')
    s=Home.session
    dt=Home.data
    h=Home.headers

    t1= Text()
    t2 = Text()

    def tabs_builder(dict):
        

        week_list = list(dict["data"]["diary"].keys())

        monday = dict["data"]["diary"][f"{week_list[0]}"]
        tuesday = dict["data"]["diary"][f"{week_list[1]}"]
        wednesday = dict["data"]["diary"][f"{week_list[2]}"]
        thursday = dict["data"]["diary"][f"{week_list[3]}"]
        friday = dict["data"]["diary"][f"{week_list[4]}"]
        # Saturday = j["data"]["diary"][f"{week_list[5]}"]
        # Sunday = j["data"]["diary"][f"{week_list[6]}"] 

        def get_color(val):
            if val == "5" or val == "4":
                return "#72FF8A"
            if val == "3":
                return "#FDAD52"
            if val == "2":
                return "#F75353"
            if val == "":
                return None
    
        def get_lessonTime(day, count):
            if day == week_list[0]:
                lessonTime = monday[count-1]["lessonTime"]
                return lessonTime
            if day == week_list[0]:
                lessonTime = thursday[count-1]["lessonTime"]
                return lessonTime
            if day == week_list[0]:
                lessonTime = wednesday[count-1]["lessonTime"]
                return lessonTime
            if day == week_list[0]:
                lessonTime = tuesday[count-1]["lessonTime"]
                return lessonTime
            if day == week_list[0]:
                lessonTime = friday[count-1]["lessonTime"]
                return lessonTime

        def get_teacher(day, count):
            if day == week_list[0]:
                teacher = monday[count-1]["teacher"]
                return teacher
            if day == week_list[0]:
                teacher = thursday[count-1]["teacher"]
                return teacher
            if day == week_list[0]:
                teacher = wednesday[count-1]["teacher"]
                return teacher
            if day == week_list[0]:
                teacher = tuesday[count-1]["teacher"]
                return teacher
            if day == week_list[0]:
                teacher = friday[count-1]["teacher"]
                return teacher

        def get_mark(day, count):
            if day==week_list[0]:
                m = monday[count-1]["marksRaw"]
                m2= str(m)
                m3 =m2.replace("['","")
                mark= m3.replace("']","")
                if mark != "[]":
                    return mark
                else:
                    return None
                
            if day==week_list[1]:
                m = tuesday[count-1]["marksRaw"]
                m2= str(m)
                m3 =m2.replace("['","")
                mark= m3.replace("']","")
                if mark != "[]":
                    return mark
                else:
                    return None
            if day==week_list[2]:
                m = wednesday[count-1]["marksRaw"]
                m2= str(m)
                m3 =m2.replace("['","")
                mark= m3.replace("']","")
                if mark != "[]":
                    return mark
                else:
                    return None
            if day==week_list[3]:
                m = thursday[count-1]["marksRaw"]
                m2= str(m)
                m3 =m2.replace("['","")
                mark= m3.replace("']","")
                if mark != "[]":
                    return mark
                else:
                    return None
            if day==week_list[4]:
                m = friday[count-1]["marksRaw"]
                m2= str(m)
                m3 =m2.replace("['","")
                mark= m3.replace("']","")
                if mark != "[]":
                    return mark
                else:
                    return None
        
        def get_homework(day, count):
            p="   "
            if day==week_list[0]:
                homework = monday[count-1]["previousHomework"]["homework"]
                return f"{p}{homework}"
            if day==week_list[1]:
                homework = tuesday[count-1]["previousHomework"]["homework"]
                return f"{p}{homework}"
            if day==week_list[2]:
                homework = wednesday[count-1]["previousHomework"]["homework"]
                return f"{p}{homework}"
            if day==week_list[3]:
                homework = thursday[count-1]["previousHomework"]["homework"]
                return f"{p}{homework}"
            if day==week_list[4]:
                homework = friday[count-1]["previousHomework"]["homework"]
                return f"{p}{homework}"
            
        def get_theme(day, count):
            p="   "
            if day==week_list[0]:
                theme = monday[count-1]["topic"]
                return f"{p}{theme}"
            if day==week_list[1]:
                theme = tuesday[count-1]["topic"]
                return f"{p}{theme}"
            if day==week_list[2]:
                theme = wednesday[count-1]["topic"]
                return f"{p}{theme}"
            if day==week_list[3]:
                theme = thursday[count-1]["topic"]
                return f"{p}{theme}"
            if day==week_list[4]:
                theme = friday[count-1]["topic"]
                return f"{p}{theme}"
            
        def getlesson(day, count):
            if day==week_list[0]:
                lesson = monday[count-1]["subject"]
                return lesson
            if day==week_list[1]:
                lesson = tuesday[count-1]["subject"]
                return lesson
            if day==week_list[2]:
                lesson = wednesday[count-1]["subject"]
                return lesson
            if day==week_list[3]:
                lesson = thursday[count-1]["subject"]
                return lesson
            if day==week_list[4]:
                lesson = friday[count-1]["subject"]
                return lesson         
            
        def get_coutn_lesson(day):
            return len(dict["data"]["diary"][f"{day}"])
        
        def items(day, count):
            itemsrow = Column()
            # count = get_coutn_lesson(day)
            for i in range(1, count + 1):
                itemsrow.controls.append(
                    Column(
                        controls=[
                            Row([
                                Container(
                                    content=Row([
                                        Container(
                                            Text(f"{i}",weight=FontWeight.BOLD),
                                            
                                            ),
                                        Container(
                                            Text(value=getlesson(day, i ),weight=FontWeight.BOLD, size=16),
                                            Text("Учитель"),
                                            
                                            
                                            )
                                    ])
                                ),
                                Container(
                                    content=Text(value=get_mark(day,i)),
                                    bgcolor=get_color(get_mark(day,i)),# "#47BE5B",
                                    height=20,
                                    width=20,
                                    alignment=alignment.center,
                                    border_radius=border_radius.all(5),
                                ),
                            ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            ),
                            Row(
                                controls=[
                                    Text(value=get_lessonTime(day, i)),
                                    Text(value=get_teacher(day, i)), 
                                ]
                                
                            ),
                            Column([
                                    Text("Тема урока"),
                                    Container(
                                        Text(value=get_theme(day,i),expand=1),
                                        bgcolor="#FFEDB0",
                                        padding=padding.only(left=5,right=5),
                                        # border="#C5E46F",
                                        border_radius=7,
                                        ),
                                    Text("Домашнее задание"),
                                    Container(
                                        Text(value=get_homework(day,i),expand=4),
                                        bgcolor="#C0E9D9",
                                        padding=padding.only(left=5,right=5),
                                        # border="#C5E46F",
                                        border_radius=7,
                                    ),
                                ],
                                # wrap=True,
                            ),
                            Divider(thickness=1),
                            # Container(height=2,bgcolor="#9C0B0B"),
                        ],
                    )
                )
            return itemsrow
            
        def my_screen(day):
            c = get_coutn_lesson(day)
            return Column(
                scroll="auto",
                controls=[
                   Container(
                        Text(
                            value=f"{day}", 
                            weight=FontWeight.BOLD, 
                            size=18
                            ),
                        alignment=alignment.center,
                        ),
                        
                    items(day,c)
                    ]
                )
       
        return Tabs(
            indicator_color="#0F7501",
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    text="Пн",
                    content=Container(
                        content=my_screen(week_list[0]),
                        bgcolor=BGCOLOR,
                        border_radius=15,
                        border=border.all(2,color=BORDERCOLOR),
                        padding=padding.only(left=5,top=20,bottom=20,right=5),
                    ),
                ),
                Tab(
                    text="Вт",
                    content=Container(
                        content=my_screen(week_list[1]),
                        bgcolor=BGCOLOR,
                        border_radius=15,
                        border=border.all(2,color=BORDERCOLOR),
                        padding=padding.only(left=5,top=20,bottom=20,right=5),
                    ),
                ),
                Tab(
                    text="Ср",
                    content=Container(
                        content=my_screen(week_list[2]),
                        bgcolor=BGCOLOR,
                        border_radius=15,
                        border=border.all(2,color=BORDERCOLOR),
                        padding=padding.only(left=5,top=20,bottom=20,right=5),
                    ),
                ),
                Tab(
                    text="Чт",
                    content=Container(
                        content=my_screen(week_list[3]),
                        bgcolor=BGCOLOR,
                        border_radius=15,
                        border=border.all(2,color=BORDERCOLOR),
                        padding=padding.only(left=5,top=20,bottom=20,right=5),
                    ),
                ),
                Tab(
                    text="Пт",
                    content=Container(
                        content=my_screen(week_list[4]),
                        bgcolor=BGCOLOR,
                        border_radius=15,
                        border=border.all(2,color=BORDERCOLOR),
                        padding=padding.only(left=5,top=20,bottom=20,right=5),
                    ),
                ),
                Tab(
                    text="Сб",
                    content=Container(
                        content=Text(j), alignment=alignment.center
                    ),
                ),
                Tab(
                    text="Вс",
                    visible=True,
                    content=Container(
                        content=Text(t2), 
                        alignment=alignment.center,
                        # label_color="#FF0000"
                    ),
                ),
            ],
            tab_alignment=TabAlignment.FILL,
            expand=True,
        )

    def up(e):
        
        page.clean()
        page.update()

    def get_json(d):
        global j
        link3=f"https://one.astrobl.ru/edv/index/diary/B8D64CF3C9BF8CBA6872B85CAFFBB2BB?date={d}"

        try:
            resp_dn = s.get(link3, data=dt, headers=h )
            resp_dn.raise_for_status()
            # global json_data
            json_data = resp_dn.json()
        except RequestException as e:
            print(f"Проблема с выполнением HTTP-запроса:{e}")
            t1.value = f"Проблема с выполнением HTTP-запроса:{e}"    
        except json.JSONDecodeError:
            print("Не удалось декодировать JSON. Пожалуйста, попробуйте ещё раз.")
        # t2.value 
        # return 
        # j = json_data
        t2.value = json_data
        # print(f'j=json_data = {id(j)}')
        return json_data
    
    today = datetime.datetime.today()
    # curret_days = today
    print(today)
   
    mon = today - datetime.timedelta(datetime.datetime.weekday(today))
    mon2=mon.strftime('%d.%m.%Y')
    
    sun = today + datetime.timedelta(6 - datetime.datetime.weekday(today))
    sun2=sun.strftime('%d.%m.%Y')
    
    string_to_screen = f"{mon2} - {sun2}"
    print(string_to_screen)

    week_to_screen = Text(value=string_to_screen, weight="bold")

    def week_enc(e):
        
        mon3 = (mon + datetime.timedelta(days=7))
        mon2=mon3.strftime('%d.%m.%Y')
        sun3 = (mon3 + datetime.timedelta(days=6))
        sun2= sun3.strftime('%d.%m.%Y')
        week_to_screen.value=f"{mon2}-{sun2}" 
        
        
        print(mon)
        print("Press enc")
        page.update()

    def week_dec(e):
        mon3 = (mon - datetime.timedelta(days=7))
        mon2=mon3.strftime('%d.%m.%Y')
        sun3 = (mon3 - datetime.timedelta(days=6))
        sun2= sun3.strftime('%d.%m.%Y')
        week_to_screen.value=f"{mon2}-{sun2}" 
        print(mon)
        print("Press dec")
        page.update()  
    
    def dropdown_changed(e):
        # t.value = f"Dropdown changed to {dd.value}"
        page.update()

    def handle_change(e):
        t1.value = f"Выбранная дата: {e.control.value.strftime('%d.%m.%Y')}"
        curret_days = e.control.value

        mon = curret_days - datetime.timedelta(datetime.datetime.weekday(curret_days))
        mon2=mon.strftime('%d.%m.%Y')
        
        sun = curret_days + datetime.timedelta(6 - datetime.datetime.weekday(curret_days))
        sun2=sun.strftime('%d.%m.%Y')

        week_to_screen.value=f"{mon2} - {sun2}"
        tabs_builder(get_json(mon2))

        # page.clean_async()
        # page.update_async()
        page.clean()
        page.update()
    
    def handle_dismissal(e):
        t2.value = f"DatePicker dismissed"
        page.update()
   
    
        
    b2 = IconButton(
        icon=Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
                DatePicker(
                    first_date=datetime.datetime(year=2024, month=9, day=1),
                    last_date=datetime.datetime(year=2035, month=6, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
    )

    data_input = Container(
        content=Row(
            controls=[
                Container(Text("Выбор даты")),
                Container(
                    content=Row(
                        controls=[
                            IconButton(icon=Icons.CHEVRON_LEFT,
                                on_click=week_dec
                            ),
                            Container(
                                # Text("02.12.2024-08.12.2024"),
                                b2,
                                border_radius=5,
                                # border=border.all(1,color="#111111"),
                                padding=padding.only(left=3,right=3),
                                ),
                            IconButton(icon=Icons.CHEVRON_RIGHT,
                                on_click=week_enc
                            ),
                        ]
                    )
                )
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=padding.only(left=10,right=10),
        bgcolor=BGCOLOR,
        border_radius=15,
        border=border.all(2,color=BORDERCOLOR),
    )
           
    dd_learner = Dropdown(
        border_width=2,
        # border_color=BORDERCOLOR,
        bgcolor=BGCOLOR,
        border_radius=15,
        border=InputBorder.NONE,
        on_change=dropdown_changed,
        options=[
            dropdown.Option("Максим"),
            dropdown.Option("Лиза"),
            
        ],
        width=200,
    )  

    top_line = Container(
        content=Row(
            controls=[
                dd_learner,
                week_to_screen
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=padding.only(left=10,right=10),
        bgcolor=BGCOLOR,
        border_radius=15,
        border=border.all(2,color=BORDERCOLOR),
    )
 
    
    
    
    
    return View("/diarypage",[
        AppBar(
            title=Text("one.astrobl.ru"),
            center_title=True,
            bgcolor="#63aae1",
        ),
        top_line,
        data_input,
        t1,
        IconButton(
            icon=Icons.REFRESH,
            on_click=up
        ),
        tabs_builder(j)
    ],
    vertical_alignment=MainAxisAlignment.END,
    foreground_decoration=BoxDecoration(
        image=DecorationImage(
            src="icons/grid-masked2.png",
            repeat=ImageRepeat.REPEAT
            )
        ) 
    )