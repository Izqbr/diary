from flet import *
from flet_route import Params, Basket
import Home 

s=Home.session
h=Home.headers

def schedule(page:Page,params:Params,basket:Basket):
    BGCOLOR = "#E9FCE3"
    BORDERCOLOR = "#00AF0F"
    
    def radiogroup_changed(e):
        print("radio taped")
        # t.value = f"Your favorite color is:  {e.control.value}"
        # page.update()

    data_input = Container(
        content=Row(
            controls=[
                Container(Text("Выбор даты")),
                Container(
                    content=Row(
                        controls=[
                            IconButton(icon=Icons.CHEVRON_LEFT),
                            Container(
                                Text("02.12.2024-08.12.2024"),
                                border_radius=5,
                                border=border.all(1,color="#111111"),
                                padding=padding.only(left=3,right=3),
                                ),
                            IconButton(icon=Icons.CHEVRON_RIGHT),
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
    
    
    learner = Container(
        content=RadioGroup(
            content=Row(
                controls=[
                    Radio(value="Максим",label="Максим"),
                    Radio(value="Лиза",label="Лиза"),
                ]
            ),
            on_change=radiogroup_changed,
        ),
        bgcolor=BGCOLOR,
        border_radius=15,
        border=border.all(2,color=BORDERCOLOR),
    )
    
    

    t = Tabs(
        indicator_color="#0F7501",
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Пн",
                content=Container(
                    content=Text("This is Tab 1"), alignment=alignment.center,
                    bgcolor=BGCOLOR,
                    border_radius=15,
                    border=border.all(2,color=BORDERCOLOR),
                ),
            ),
            Tab(
                text="Вт",
                content=Container(
                    content=Text("This is Tab 2"), alignment=alignment.center,
                    bgcolor=BGCOLOR,
                    border_radius=15,
                    border=border.all(2,color=BORDERCOLOR),
                ),
            ),
            Tab(
                text="Ср",
                content=Container(
                    content=Text("This is Tab 3"), alignment=alignment.center,
                    bgcolor=BGCOLOR,
                    border_radius=15,
                    border=border.all(2,color=BORDERCOLOR),
                ),
            ),
            Tab(
                text="Чт",
                content=Container(
                    content=Text("This is Tab 4"), alignment=alignment.center
                ),
            ),
            Tab(
                text="Пт",
                content=Container(
                    content=Text("This is Tab 5"), alignment=alignment.center
                ),
            ),
            Tab(
                text="Сб",
                content=Container(
                    content=Text("Выходной"), alignment=alignment.center
                ),
            ),
            Tab(
                text="Вс",
                visible=True,
                content=Container(
                    content=Text("Выходной"), 
                    alignment=alignment.center,
                    # label_color="#FF0000"
                ),
            ),
        ],
        tab_alignment=TabAlignment.FILL,
        expand=True,
    )

    def openschedule(e):
        page.go("/menupage")
        page.update()
            
    return View("/schedule",[
        AppBar(
            title=Text("Расписание"),
        center_title=True,
        bgcolor="#63aae1",
        ),
        # ElevatedButton(
        #     text="back",
        #     on_click=openschedule
        # ),
        learner,
        data_input,
        t
    ],
    vertical_alignment=MainAxisAlignment.END,
    foreground_decoration=BoxDecoration(
        image=DecorationImage(
            src="icons/grid-masked2.png",
            repeat=ImageRepeat.REPEAT
            )) 
    )





    



