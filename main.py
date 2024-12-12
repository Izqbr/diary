from flet import *
from flet_route import Routing, path

from Home import home
from Schedule import schedule
from Menu import menupage
from Diary import diarypage
from Testpage import testpage

async def main(page: Page):
    # page.padding = 0,
    # page.spacing =0,
    page.window.width = 300
    page.window.height = 600
    # page.add(SafeArea(Text("Hello, Flet!")))
    
    define_routes = [
        path(url= "/", view=home, clear=True),
        path(url= "/schedule", view=schedule, clear=True),
        path(url= "/menupage", view=menupage, clear=False),
        path(url= "/diarypage", view=diarypage, clear=False),
        path(url= "/testpage", view=testpage, clear=False),
    ]
    Routing(page=page,app_routes=define_routes)
    page.go("/")

if __name__ == "__main__":
    app(main, assets_dir="assets")
# 