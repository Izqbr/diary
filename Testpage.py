from flet import *
from flet_route import Params, Basket
import datetime
# import Home 

# s=Home.session
# h=Home.headers

def testpage(page:Page,params:Params,basket:Basket):
    
    def handle_change(e):
        t1.value = f"Date changed: {e.control.value.strftime('%d.%m.%Y')}"
        # page.add(Text(f"Date changed: {e.control.value.strftime('%Y.%m.%d')}"))
        page.update()

    def handle_dismissal(e):
        t2.value = f"DatePicker dismissed"
        page.update()

    t1= Text()
    t2 = Text()
    b=ElevatedButton(
            "Pick date",
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
    
    test = Column(
        
        controls=[
            Container(Text("one text")),
            Column(
                scroll=ScrollMode.AUTO,
                controls=[
                    Container(
                                Text(value=f"111", weight=FontWeight.BOLD, size=18),
                                alignment=alignment.center,
                                ),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                    Text("Text"),
                ]
            )
        ]
    )
    
    
    learner = RadioGroup(
        content=Column(
            controls=[
                Radio(label="Максим"),
                Radio(label="Лиза"),
            ]
        )
    ),
    nav_bar = BottomAppBar(
        height=50,
        bgcolor="#B3E8FD",
        shape=NotchShape.CIRCULAR,
        
        content=Row(
            alignment=MainAxisAlignment.SPACE_EVENLY,
            controls=[
                
                Container(Text("Mo")),
                Container(Text("Mo")),
                Container(Text("Mo")),
                Container(Text("Mo")),
                Container(Text("Mo")),
                Container(Text("Mo")),
                Container(Text("Mo")),

            ]
        ),
    )
    
    def back(e):
        page.go("/menupage")
        page.update()
            
    return View("/testpage",[
        AppBar(
            title=Text("TestPage"),
        center_title=True,
        bgcolor="#63aae1",
        ),
        ElevatedButton(
            text="back",
            on_click=back
        ),
        b,
        t1,
        t2,
        # test,
        nav_bar,
    ],
    vertical_alignment=MainAxisAlignment.END,
    foreground_decoration=BoxDecoration(
        image=DecorationImage(
            src="icons/grid-masked2.png",
            repeat=ImageRepeat.REPEAT
            )) 
    )

