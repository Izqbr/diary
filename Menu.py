from flet import *
from flet_route import Params, Basket
import Home 

s=Home.session
h=Home.headers
fio = "Фамилия И.О. 8А"


def menupage(page:Page,params:Params,basket:Basket):
    

    

    def openclip(e):
        page.go("/testpage")
        page.update()

    def openschedule(e):
        page.go("/schedule")
        page.update()



    def opendiary(e):
        page.go("/diarypage")
        page.update()

    return View("/menupage",[
        AppBar(
            title=Text("one.astrobl.ru"),
        center_title=True,
        bgcolor="#63aae1",
        ),
        
        GridView(
            expand=False,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
            controls=[
                Container(
                    content=Column([
                      Image(
                            src=f"icons/book-2.png",
                            fit=ImageFit.CONTAIN,
                            repeat=ImageRepeat.NO_REPEAT,
                            border_radius=border_radius.all(10),
                        ),
                        Text("Дневник")   
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                                        
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    # bgcolor="#57FA9B",
                    width=150,
                    height=150,
                    border=border.all(2,color="#57FA9B"),
                    # border=Border.all(10, color="#111111")
                    border_radius=15,
                    ink= True,
                    on_click=opendiary,
                ),
                Container(
                    content=Column([
                      Image(
                            src=f"icons/calendar-2.png",
                            fit=ImageFit.SCALE_DOWN,
                            repeat=ImageRepeat.REPEAT,
                            border_radius=border_radius.all(10),
                        ),
                        Text("Расписание")                           
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                        
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    width=150,
                    height=150,
                    border=border.all(2,color="#57FA9B"),
                    border_radius=15,
                    ink= True,
                    on_click=openschedule,
                ),
                Container(
                    content=Column([
                      Image(
                            src="icons/chat-2.png",
                            fit=ImageFit.SCALE_DOWN,
                            repeat=ImageRepeat.NO_REPEAT,
                            border_radius=border_radius.all(10),
                        ),
                        Text("Расписание")                           
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                        
                    margin=10,
                    padding=10,
                    alignment=alignment.center,
                    width=150,
                    height=150,
                    border=border.all(2,color="#57FA9B"),
                    border_radius=15,
                    ink= True,
                    on_click=openschedule,
                ),
                Container(
                        content=Column([
                            Image(
                                    src=f"icons/clip-2.png",
                                    fit=ImageFit.SCALE_DOWN,
                                    repeat=ImageRepeat.REPEAT,
                                    border_radius=border_radius.all(10),
                                ),
                            Text("Тест")                           
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                        ),
                            
                        margin=10,
                        padding=10,
                        alignment=alignment.center,
                        width=150,
                        height=150,
                        border=border.all(2,color="#57FA9B"),
                        border_radius=15,
                        ink= True,
                        on_click=openclip,
                    ),
            Image(
                src=f"assets/clip-2.png",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            ),
            Image(
                src=f"assets/chat-2.png",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            ),
            Image(
                src=f"assets/application-2.png",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            ),
            Image(
                src=f"assets/chat-2.png",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            ),
            Image(
                src=f"assets/calendar-2.png",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            ),
            Image(
                src=f"assets/new-file-4.png",
                fit=ImageFit.NONE,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10),
            )
        ])
    ],
    foreground_decoration=BoxDecoration(
        image=DecorationImage(
            src="icons/grid-masked2.png",
            repeat=ImageRepeat.REPEAT
            )) 
    )

