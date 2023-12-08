from flet import *
import builder as Builder
import sqlite3 as sql
import random   

con = sql.connect("itens.db")
cursor = con.cursor()
cursor.execute("""  
                CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY AUTOINCREMENT, ncard TEXT)
                """)
               

class App:
    DARKMODE = True


    def __init__(self, 
                 BGCOLOR, 
                 PADDING, 
                 HEIGHT,
                 WIDTH,
                 TITLE,
                 COLORS) -> None:
        
        self.BGCOLOR = BGCOLOR
        self.PADDING = PADDING
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.TITLE = TITLE
        self.COLORS = COLORS




    def main(self, page: Page) -> None:
        page.bgcolor = self.BGCOLOR
        page.padding = self.PADDING
        page.window_height = self.HEIGHT
        page.window_width = self.WIDTH
        page.title = self.TITLE
        page.route = "/"
        page.theme = Theme(
            color_scheme=ColorScheme(
                primary=colors.AMBER_700
            )
        )

        if page.route == "/":
            pass
            


        class Functions:
            def change_theme_mode(e: TapEvent):
                if App.DARKMODE:
                    App.DARKMODE = False
                    Builder.Builder.dark_mode_button.icon = icons.DARK_MODE_OUTLINED
                    Builder.Builder.dark_mode_button.icon_color = colors.BLACK
                    Builder.Builder.title.color = colors.BLACK
                    page.bgcolor = colors.GREY_100
                    page.theme_mode = "light"
                    page.update()

                else:
                    page.bgcolor = "#1C1B1B"
                    page.theme_mode = "dark"
                    App.DARKMODE = True
                    Builder.Builder.dark_mode_button.icon = icons.DARK_MODE
                    Builder.Builder.dark_mode_button.icon_color = colors.WHITE
                    Builder.Builder.title.color = colors.WHITE

                    page.update()

            class add_geral:
                def route_add_card(e):
                    page.route = "/add_card"
                    page.controls.clear()
                    page.controls.append(Builder.BuilderAddCard.app)
                    page.bgcolor = "#1C1B1B"
                    page.update()

                def add_card_function(e: TapEvent):
                    Builder.Builder.list_cards.controls.append(ListTile(title=Container(
                                                        content=Text("Olá"),
                                                        width=100,
                                                        bgcolor=self.COLORS[0],
                                                        border_radius=30,
                                                        height=100
                                                        )))
                    
                    page.update()



        
        Builder.Builder.dark_mode_button.on_click = Functions.change_theme_mode
        Builder.Builder.add_button.on_click = Functions.add_geral.route_add_card
        page.add(Builder.Builder.app)


COLORS = [
    "#C4DFDF",
    "#D2E9E9"
]



if __name__ == '__main__':
    target = App(BGCOLOR="#1C1B1B", 
                 PADDING=30,
                 WIDTH=400,
                 HEIGHT=680,
                 TITLE="Pyrteira",
                 COLORS=colors)

    app(target=target.main)