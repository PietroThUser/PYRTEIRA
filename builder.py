from flet import *

class Builder:
    dark_mode_button: IconButton = IconButton(
        icon=icons.DARK_MODE
    )

    add_button: ElevatedButton = ElevatedButton(
        text="Adicionar cartão",
        width=40000,
        height=50
    )

    card_container: Container = Container(
        width=10,
        height=160,
        border_radius=30,
        bgcolor=colors.WHITE
    )

    title: Text = Text(
        value="Carteira",
        size=30,
        weight=FontWeight.W_700
    )

    list_cards: ListView = ListView(
        expand=True,
        spacing=15,
        auto_scroll=False
    )

    app: SafeArea = SafeArea(
        Column(
        controls = [
            Row([
                title,
                dark_mode_button
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            Divider(),
            list_cards,
            add_button
        ]),
        expand=True
    )